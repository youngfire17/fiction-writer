# Fiction Writer

An autonomous fiction-book generation capability for Claude Code. Give it a premise, get a full-length novel (or series).

## Status: Brainstorming / Design Phase

This repo is being scaffolded. The knowledge library, skill, and workflow have not been built yet — we're nailing down the design.

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

## Open questions (pick up here)

1. **Series vs standalone state tracking** — How is series state tracked across books? Series bible files (markdown)? A continuity database (Supabase)? Both?
2. **Output format** — Markdown chapters, single manuscript file, EPUB export, all of them?
3. **Length control** — How does the system know when a book is "done"? Target word count? Plot completion? Both? Per-genre defaults?
4. **Subagent breakdown** — Which specific subagents? Initial idea: `plotter`, `world-builder`, `character-designer`, `drafter`, `line-editor`, `continuity-checker`, `voice-scrubber`. Confirm or trim.
5. **First book test case** — Once the system is built, what's the first book we generate to validate it? Genre + rough premise?

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
