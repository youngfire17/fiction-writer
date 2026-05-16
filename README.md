# Fiction Writer

An autonomous fiction-book generation capability for Claude Code. Give it a premise, get a full-length novel (or series).

## Status: Brainstorming / Design Phase

This repo is being scaffolded. The knowledge library, skill, and workflow have not been built yet — we're still nailing down the design.

### Decisions locked in

- **Use case:** Autonomous book generator. Give it a premise → full book out.
- **Research depth:** Hybrid — build the bulk from Claude's training knowledge of major craft sources (King, Sanderson, McKee, Save the Cat, Snowflake, Hero's Journey, etc.), then layer in web research (Firecrawl) for famous-author style guides, lectures, and craft essays.
- **Genre scope:** All major fiction genres — fantasy, sci-fi, thriller, mystery, romance, literary, horror, historical, YA. Genre-specific craft sections in the library.

### Open questions (next session picks up here)

1. **Structure of the capability** — Is this:
   - (a) A reference library of markdown docs in this repo, that Claude reads when writing fiction?
   - (b) A custom Claude Code skill at `~/.claude/skills/fiction-writer/` that wraps the library?
   - (c) A full subagent workflow — separate agents for plotting, drafting, character design, line-editing, continuity-checking?
   - (d) All of the above — library lives here, skill is the interface, subagents do specialized work?
2. **Voice / anti-AI prose** — How do we prevent the prose from sounding like AI? Specific author voice imitation? Style rules library? A prose-critique pass that flags AI tells (em-dash overuse, "It's not X, it's Y" patterns, etc.)?
3. **Series vs standalone** — How is series state tracked? Series bible files? Continuity DB?
4. **Output format** — Markdown chapters, single manuscript, EPUB export, all of them?
5. **Length control** — How does the system know when a book is "done"? Target word count? Plot completion? Both?

## Goals (from the original ask)

- Full-length novels (300–600 pages, or whatever is standard for the genre)
- Master story craft: arcs, character creation + development, mystery, adventure, pain/suffering, cadence, tone, dialogue
- Do NOT sound like AI — study and emulate the writing style of the most famous fiction writers
- Capability for standalone books AND multi-book series
- Full world/universe building
- Capture readers, engage emotions, deliver cliffhangers

## Repo layout (planned, not built yet)

```
/library         knowledge base — craft references organized by topic
/skill           Claude Code skill that orchestrates the writing workflow
/templates       book outline templates, series bibles, character sheets
/books           generated books live here, one folder per project
```
