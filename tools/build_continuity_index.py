#!/usr/bin/env python3
"""Build the SQLite continuity index from a book project's markdown bible.

Usage: python tools/build_continuity_index.py books/<slug>

Reads:
  books/<slug>/series-bible/world/*.md
  books/<slug>/series-bible/characters/*.md
  books/<slug>/series-bible/timeline/*.md
  books/<slug>/plot/setup-payoff.md
  books/<slug>/chapters/*.md (for footer-flagged events)

Writes:
  books/<slug>/continuity.db

The markdown is the source of truth. This script never writes back to markdown.
"""

import re
import sqlite3
import sys
from pathlib import Path


SCHEMA = """
CREATE TABLE characters (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT UNIQUE NOT NULL,
  aliases TEXT,
  role TEXT,
  pov INTEGER,
  arc TEXT,
  first_appearance INTEGER,
  status TEXT,
  location TEXT,
  knowledge TEXT,
  raw_path TEXT
);

CREATE TABLE locations (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT UNIQUE NOT NULL,
  region TEXT,
  description TEXT,
  raw_path TEXT
);

CREATE TABLE events (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  chapter INTEGER,
  scene INTEGER,
  in_world_time TEXT,
  summary TEXT,
  characters_present TEXT,
  raw_path TEXT
);

CREATE TABLE threads (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  thread_id TEXT UNIQUE NOT NULL,
  type TEXT,
  description TEXT,
  chapter_introduced INTEGER,
  chapter_resolved INTEGER,
  status TEXT,
  notes TEXT
);

CREATE TABLE world_rules (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  rule TEXT,
  source TEXT,
  scope TEXT
);
"""


KV_LINE = re.compile(r"^([a-z][a-z0-9 _-]*?)\s*:\s*(.+?)\s*$", re.IGNORECASE)


def parse_kv_block(text: str) -> dict:
    """Pull simple `key: value` lines out of the top of a markdown file."""
    out = {}
    for line in text.splitlines():
        if line.strip().startswith("#") or line.strip().startswith("-"):
            continue
        m = KV_LINE.match(line)
        if m:
            out[m.group(1).strip().lower()] = m.group(2).strip()
    return out


def parse_section(text: str, heading: str) -> str | None:
    """Return the body of a `## <heading>` section, or None."""
    pattern = re.compile(
        rf"^##\s+{re.escape(heading)}\s*$(.*?)(?=^##\s|\Z)",
        re.MULTILINE | re.DOTALL | re.IGNORECASE,
    )
    m = pattern.search(text)
    return m.group(1).strip() if m else None


def load_characters(bible_dir: Path, conn: sqlite3.Connection) -> None:
    char_dir = bible_dir / "characters"
    if not char_dir.exists():
        return
    for path in sorted(char_dir.glob("*.md")):
        if path.name == "cast-index.md":
            continue
        text = path.read_text(encoding="utf-8")
        # name from first H1
        name_match = re.search(r"^#\s+(.+?)\s*$", text, re.MULTILINE)
        if not name_match:
            continue
        name = name_match.group(1).strip()
        kv = parse_kv_block(text)
        first_app = kv.get("first-appearance") or kv.get("first appearance")
        first_app_n = None
        if first_app:
            m = re.search(r"\d+", first_app)
            if m:
                first_app_n = int(m.group())
        conn.execute(
            "INSERT OR REPLACE INTO characters (name, aliases, role, pov, arc, first_appearance, status, location, knowledge, raw_path) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                name,
                kv.get("aliases"),
                kv.get("role"),
                1 if kv.get("pov", "").lower() == "yes" else 0,
                kv.get("arc"),
                first_app_n,
                kv.get("status"),
                kv.get("location"),
                parse_section(text, "Knowledge"),
                str(path),
            ),
        )


def load_locations(bible_dir: Path, conn: sqlite3.Connection) -> None:
    geo = bible_dir / "world" / "geography.md"
    if not geo.exists():
        return
    text = geo.read_text(encoding="utf-8")
    # match `### <Name>\n[kv lines]\n<description>`
    blocks = re.split(r"^###\s+", text, flags=re.MULTILINE)[1:]
    for block in blocks:
        head, _, rest = block.partition("\n")
        name = head.strip()
        kv = parse_kv_block(rest)
        desc_lines = [
            ln for ln in rest.splitlines() if ln and not KV_LINE.match(ln)
        ]
        desc = " ".join(desc_lines).strip()
        conn.execute(
            "INSERT OR REPLACE INTO locations (name, region, description, raw_path) VALUES (?, ?, ?, ?)",
            (name, kv.get("region"), desc, str(geo)),
        )


def load_threads(book_dir: Path, conn: sqlite3.Connection) -> None:
    payoff_file = book_dir / "plot" / "setup-payoff.md"
    if not payoff_file.exists():
        return
    text = payoff_file.read_text(encoding="utf-8")
    # parse the markdown table
    row_re = re.compile(r"^\|\s*(S-\d+|P-\d+)\s*\|(.+?)\|\s*$", re.MULTILINE)
    for m in row_re.finditer(text):
        thread_id = m.group(1).strip()
        cells = [c.strip() for c in m.group(2).split("|")]
        # Schema: | id | description | type | planted (ch, ...) | payoff (ch, ...) | status | notes |
        if len(cells) < 6:
            continue
        description, ttype, planted_cell, payoff_cell, status = cells[:5]
        notes = cells[5] if len(cells) > 5 else ""
        ch_in = _first_int(planted_cell)
        ch_out = _first_int(payoff_cell)
        conn.execute(
            "INSERT OR REPLACE INTO threads (thread_id, type, description, chapter_introduced, chapter_resolved, status, notes) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (thread_id, ttype, description, ch_in, ch_out, status, notes),
        )


def load_events_from_chapter_footers(book_dir: Path, conn: sqlite3.Connection) -> None:
    chapters_dir = book_dir / "chapters"
    if not chapters_dir.exists():
        return
    for path in sorted(chapters_dir.glob("chapter-*.md")):
        text = path.read_text(encoding="utf-8")
        m = re.search(r"<!--(.*?)-->", text, re.DOTALL)
        if not m:
            continue
        footer = m.group(1)
        ch_match = re.search(r"chapter-(\d+)", path.name)
        chapter_n = int(ch_match.group(1)) if ch_match else None
        summary_match = re.search(r"knowledge-gained:\s*(.+)", footer)
        present_match = re.search(r"characters-present:\s*(.+)", footer)
        time_match = re.search(r"in-world-time:\s*(.+)", footer)
        conn.execute(
            "INSERT INTO events (chapter, scene, in_world_time, summary, characters_present, raw_path) VALUES (?, ?, ?, ?, ?, ?)",
            (
                chapter_n,
                None,
                time_match.group(1).strip() if time_match else None,
                summary_match.group(1).strip() if summary_match else None,
                present_match.group(1).strip() if present_match else None,
                str(path),
            ),
        )


def _first_int(s: str) -> int | None:
    m = re.search(r"\d+", s)
    return int(m.group()) if m else None


def main(book_path_str: str) -> int:
    book_dir = Path(book_path_str)
    if not book_dir.exists() or not book_dir.is_dir():
        print(f"error: {book_dir} is not a directory", file=sys.stderr)
        return 1
    bible_dir = book_dir / "series-bible"
    if not bible_dir.exists():
        print(f"warn: {bible_dir} missing — index will be empty for bible tables")

    db_path = book_dir / "continuity.db"
    if db_path.exists():
        db_path.unlink()
    conn = sqlite3.connect(db_path)
    conn.executescript(SCHEMA)

    if bible_dir.exists():
        load_characters(bible_dir, conn)
        load_locations(bible_dir, conn)
    load_threads(book_dir, conn)
    load_events_from_chapter_footers(book_dir, conn)

    conn.commit()
    counts = {
        t: conn.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
        for t in ("characters", "locations", "events", "threads", "world_rules")
    }
    conn.close()
    print(f"built {db_path}: {counts}")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: build_continuity_index.py books/<slug>", file=sys.stderr)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
