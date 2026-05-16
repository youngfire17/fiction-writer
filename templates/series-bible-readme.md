# Series Bible — README

The series bible is **markdown-canonical**. Everything load-bearing for the book or series lives here as plain markdown, hand-editable, diffable in git. A SQLite index (`continuity.db`) is derived from these files via `tools/build_continuity_index.py` and gives subagents fast structured lookup.

## Directory layout

```
series-bible/
  world/
    core-rule.md            the one-line premise that makes this world not Earth-now
    magic-system.md         (if applicable) laws, costs, limits
    geography.md            regions/places, one paragraph each
    cultures.md             each culture with values, taboos, politics
    history.md              timeline of past events that matter
    iceberg.md              background canon NOT surfaced on-page but binding
  characters/
    <slug-name>.md          one file per major named character (template: templates/character-sheet.md)
    cast-index.md           table of every character with role + first appearance
  timeline/
    in-world-calendar.md    (optional) how the world tracks time
    book-N-timeline.md      events per book in in-world time
  threads/
    open-questions.md       narrative questions/unresolved threads tracked across books
```

## Who owns what

| File / area | Owner | Notes |
|-------------|-------|-------|
| `world/*` | world-builder | only the world-builder edits canonical world facts |
| `characters/<name>.md` (everything except Knowledge) | character-designer | initial state |
| `characters/<name>.md` Knowledge section | continuity-checker | updated chapter-by-chapter after drafting begins |
| `timeline/*` | continuity-checker | reflects in-world dates as established by drafted chapters |
| `threads/*` | foreshadowing-tracker | open narrative debts across the series |

## How to query

For fast lookups, query `continuity.db` (rebuild via `python tools/build_continuity_index.py books/<slug>`):

```bash
sqlite3 books/<slug>/continuity.db "SELECT name, location, knowledge FROM characters WHERE name = 'Mira';"
sqlite3 books/<slug>/continuity.db "SELECT * FROM threads WHERE status = 'armed';"
```

For human-edit, open the markdown files directly. The next index rebuild will pick up the change.

## Rules for adding canon

1. **Don't add what the book doesn't need.** Worldbuilder's disease bloats the bible and slows every subagent. Park speculative material in `world/sketch/` (not parsed into the index).
2. **Mark changes in commits.** Every world / character file change should commit with a one-line justification. Avoids silent canon drift.
3. **For series book N>1**: read existing bible first, add to it. Never overwrite previous-book canon without explicit user approval — it's a continuity break across the series.
