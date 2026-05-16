# Fiction Writer

An autonomous fiction-book generation capability for Claude Code. Give it a premise, get a full-length novel (or series).

## Status: Scaffolded — Ready to Outline the First Book

All 11 design decisions locked. The knowledge library, 8 subagent definitions, skill, templates, continuity-index builder, and first book project (`books/the-forgetting-wing/`) are scaffolded and the index builder is smoke-tested. The earlier `books/the-cartographer/` candidate is archived under `books/_archive/`. Chapter 1 of *The Forgetting Wing* has been drafted end-to-end through the full pipeline.

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
| 11 | First test book | **Anime-style psychological thriller, open-ended series book 1, ~80k words.** Project: `books/the-forgetting-wing/`. Premise: in a State that erases one day of memory from every citizen each year, a seventeen-year-old wakes with three missing days she somehow remembers and a dead Wing employee at her feet; the Wing's sixteen-year-old Inquisitor, fitted with a polygraph implant, is assigned to find her. Dual alternating close-3rd POV, past tense, biotech-grounded (strictly no paranormal). Craft DNA from Death Note, Attack on Titan, Demon Slayer: visceral, set-piece-built, deep dual-POV character development, mystery + suffering + cat-and-mouse. Earlier candidate (epic-fantasy cartographer, ~140k) archived under `books/_archive/`. |

## Build state (what's in the repo)

| Piece | State | Path |
|-------|-------|------|
| Repo layout scaffold | done | `/library`, `/skill`, `/subagents`, `/templates`, `/tools`, `/books` |
| Anti-AI tells catalog + scrub rules | done | `library/anti-ai/{tells-catalog,scrub-rules}.md` |
| Story-structure references | done | `library/story-structure/` (4 files) |
| Character craft references | done | `library/character/` (4 files) |
| Prose craft references | done | `library/prose/` (4 files) |
| World-building references | done | `library/world-building/` (4 files) |
| Genre cheat-sheets | done | `library/genre/` (8 files — all major genres) |
| Author voice profiles | done | `library/voice/` (6 authors: King, McCarthy, Sanderson, Le Guin, GRRM, Tartt) + `anime-thriller.md` register profile for the test book |
| 8 subagent definitions | done | `subagents/*.md` |
| Skill entry document | done | `skill/SKILL.md` |
| Templates | done | `templates/{intent,character-sheet,chapter-brief,series-bible-readme}.md` |
| Continuity-index builder | done + smoke-tested | `tools/build_continuity_index.py` |
| Test book project (`the-forgetting-wing`) | scaffolded + intent.md written | `books/the-forgetting-wing/` (prior `the-cartographer` archived to `books/_archive/`) |
| Skill + agents installed | done in this container | `~/.claude/skills/fiction-writer/` and `~/.claude/agents/*.md` symlinked back to repo |

## Next steps

1. **Run the outline pass on `books/the-forgetting-wing/`**: world-builder → character-designer → plotter, in that order. Stop for human review of the world bible (the State, the Wing, the city, the biotech), the cast (especially Maren and Sael with full sheets and distinct voices), the beat sheet, and the setup→payoff graph.
2. **Iterate on the library** as gaps surface during outlining — additional anti-AI tells specific to this register, refinements to `library/voice/anime-thriller.md`, a thriller-genre note we missed.
3. **Draft chapter 1.** First end-to-end pipeline run: plotter brief → drafter → voice-scrubber → line-editor → continuity-checker → foreshadowing-tracker. Use what breaks to refine the subagents and the voice profile.
4. **Scale up.** Drift toward full-book completion; run `revise-to-target` (80k band) and `export` at the end.

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
