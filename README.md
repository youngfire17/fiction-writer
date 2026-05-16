# Fiction Writer

An autonomous fiction-book generation capability for Claude Code. Give it a premise, get a full-length novel (or series).

## Status: Design Locked — Ready to Build

All 11 design decisions are locked in below. The knowledge library, skill, subagents, and the first test book have not been built yet — next session is the implementation kickoff.

---

## How to resume from another device

1. Open **claude.ai/code** (Claude Code on the web) on your phone or another machine.
2. Connect it to this repo: `youngfire17/fiction-writer`.
3. Tell Claude: *"Continue the fiction-writer brainstorming. Read the README for full context and pick up at the next open question."*
4. Claude will read the decisions below and ask you the next question.

Each time you wrap a session, commit and push the README updates so the next session has the latest state.

---

## Decisions locked in

| # | Question | Decision |
|---|----------|----------|
| 1 | Use case | **Autonomous book generator** — give it a premise, get a full book out. |
| 2 | Research depth | **Hybrid** — bulk built from Claude's training knowledge of major craft sources (King, Sanderson, McKee, Save the Cat, Snowflake, Hero's Journey, etc.), then layered with Firecrawl web research for famous-author style guides, lectures, and craft essays. |
| 3 | Genre scope | **All major genres** — fantasy, sci-fi, thriller, mystery, romance, literary, horror, historical, YA. Genre-specific craft sections in the library. |
| 4 | Architecture | **Library + Skill + Subagents.** Knowledge library lives in this repo. A Claude Code skill at `~/.claude/skills/fiction-writer` wraps it. Specialized subagents handle plotting, drafting, character design, line-editing, continuity. |
| 5 | Voice strategy | **All four stacked:** (a) anti-AI-tells library + scrub pass, (b) author-voice imitation profiles, (c) genre-baseline voice rules, (d) read-aloud cadence pass. |
| 6 | Series state tracking | **Both, markdown is canonical.** Series bible lives as hand-editable markdown files (characters, world, timeline, unresolved threads) in each project's folder. A derived SQLite index is rebuilt on demand to give the continuity-checker and other subagents fast structured lookup. |
| 7 | Output formats | **Per-chapter markdown (canonical) + stitched manuscript + PDF.** Drafting lives in `chapter-NN.md` files. A `manuscript.md` is stitched from chapters for end-to-end reads. Final delivery exports to PDF via pandoc. EPUB skipped for now. |
| 8 | Length control | **Plot first, then trim/expand to target.** Draft the outline to plot completion without a word-count gate, then run a revision pass that expands thin sections and tightens bloated ones to land in the genre band (or user-specified target). Two-stage so plot integrity isn't sacrificed for length. |
| 9 | Whole-book continuity | **First-class requirement, not a single pass.** The story must hold together from page 1 to the final line — causality, character knowledge, timeline, foreshadowing/payoff, world rules. Enforced by: (a) the markdown series bible + SQLite index as ground truth, (b) the plotter producing a beat sheet with explicit setup/payoff links before drafting, (c) the drafter receiving a per-chapter "what's known to whom, what's been set up, what must pay off" brief, (d) a continuity-checker pass after each chapter and a full-book pass before finalization. |
| 10 | Subagent roster | **8 agents:** `plotter`, `world-builder`, `character-designer`, `drafter`, `line-editor`, `continuity-checker` (facts/timeline/character knowledge), `foreshadowing-tracker` (setup→payoff graph, Chekhov's guns, planted clues, character promises), `voice-scrubber` (anti-AI-tells + cadence). |
| 11 | First test book | **Epic fantasy, book 1 of a series, ~140k words.** Premise: *a disgraced cartographer is hired to map a continent that rewrites itself every generation.* Exercises every part of the system on the first run — world-building, magic-system rigor, series-state tracking, foreshadowing across a multi-book arc, and voice over a long form. Highest-ambition validation case; if it works here it works anywhere. |

## Next steps (implementation kickoff)

1. **Scaffold the repo layout** below (`/library`, `/skill`, `/subagents`, `/templates`, `/books`).
2. **Seed the knowledge library** from training-data craft sources first (King, Sanderson, McKee, Save the Cat, Snowflake, Hero's Journey, genre conventions, anti-AI tells, author voice profiles). Defer Firecrawl-sourced material to a second pass.
3. **Write the 8 subagent definitions** (plotter, world-builder, character-designer, drafter, line-editor, continuity-checker, foreshadowing-tracker, voice-scrubber) with clear inputs/outputs and the continuity contract from row 9.
4. **Build the skill** at `~/.claude/skills/fiction-writer` — entry points for `new-book`, `outline`, `draft-chapter`, `continuity-pass`, `revise-to-target`, `export`.
5. **Build the markdown↔SQLite continuity index** (rebuild-on-demand, used by continuity-checker and foreshadowing-tracker).
6. **Generate the test book** (row 11) end-to-end; treat anything that breaks as a library/subagent gap to fix.

## Original goals (from the user's ask)

- Full-length novels (300–600 pages, or whatever is standard for the genre)
- Master story craft: arcs, character creation + development, mystery, adventure, pain/suffering, cadence, tone, dialogue
- Do NOT sound like AI — study and emulate the writing style of the most famous fiction writers
- Capability for standalone books AND multi-book series
- Full world/universe building
- Capture readers, engage emotions, deliver cliffhangers

## Planned repo layout (not built yet)

```
/library         knowledge base — craft references organized by topic
  /story-structure       arcs, beats, three-act, hero's journey, save-the-cat, etc.
  /character             creation, development, voice, arcs
  /prose                 sentence craft, dialogue, scene/sequel, POV
  /world-building        magic systems, geography, cultures, history
  /genre                 conventions and craft notes per genre
  /voice                 author profiles (King, McCarthy, Sanderson, GRRM, etc.)
  /anti-ai               AI-tells catalog and scrub rules
/skill           Claude Code skill at ~/.claude/skills/fiction-writer
/subagents       agent definitions: plotter, drafter, line-editor, continuity, etc.
/templates       book outline templates, series bibles, character sheets
/books           generated books live here, one folder per project
```
