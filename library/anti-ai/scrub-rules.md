# Scrub Rules — The Voice-Scrubber's Operations

Use for: the voice-scrubber subagent. After a chapter is drafted, run these rules in order. Each rule is a (detect, replace) operation.

The tells catalog (`tells-catalog.md`) lists what's bad. This file lists what to do about it.

---

## Pass 1 — Lexical strikes

Strike-and-replace. Search the chapter for each banned word/phrase from the tells catalog. For each hit:

1. If the word adds nothing, delete the clause.
2. If the word stands in for a concrete thing, name the thing.
3. If the word is doing emotional work, replace with action or sensory detail.

**Example operations:**

- *"She delved into the archives"* → *"She read the archives from the back."*
- *"It was a testament to his discipline"* → *"He had not eaten since dawn."*
- *"A tapestry of cultures"* → name two of them, drop the rest.
- *"He couldn't help but smile"* → *"He smiled."*
- *"With a heavy heart, she nodded"* → *"She nodded. Slow."*

## Pass 2 — Contrast pivots

Search for these patterns: *not just X but Y*, *not only X*, *more than just*, *isn't X, it's Y*, *in a world where*.

Each hit: rewrite as a single declarative or two short sentences. Never preserve the contrast scaffolding.

- *"It was not just a map, it was a memory of a place that no longer existed."* → *"The map was a memory. The place was gone."*

## Pass 3 — Foreshadow telegraphs

Search for: *little did, unbeknownst, would soon, would later come to, in hindsight, would prove to be*.

Each hit: cut the foreshadow line entirely. If the scene needs the seed, plant it via action or object instead of narrator promise.

## Pass 4 — Filter words

Search for: *saw, heard, felt, watched, noticed, observed, seemed, realized, thought to herself/himself*.

Each hit (in close POV): rewrite the sentence to render the perception directly.

- *"She saw the door swing open."* → *"The door swung open."*
- *"He felt cold."* → *"His hands had gone numb on the rein."*
- *"She realized she had been wrong."* → *"She had been wrong."* (or render the realization in action)

Keep filter words only when the act of perceiving is itself the point (e.g. *"she watched him until he was gone"*).

## Pass 5 — Tricolon thinning

Find every three-item list joined by commas/and. Count them per page.

- If a page has more than two tricolons, convert one to a pair and one to a single noun.
- Tricolons describing emotion or abstract states are first to go. Tricolons of concrete physical things can stay if they earn it.

## Pass 6 — Em-dash and semicolon audit

Count em-dashes and semicolons per page.

- Em-dash > 2/page: convert most to periods or commas. Reserve em-dashes for genuine interruption or appended thought.
- Semicolon > 1/page: convert most to periods.

## Pass 7 — Paragraph-ending clinch

Look at the final sentence of every paragraph longer than four sentences.

- If it summarizes, philosophizes, or "buttons" the paragraph with a thematic statement → cut it. Let the paragraph end on the previous beat.
- If the final sentence is doing real work (action, image, surprise), keep it.

## Pass 8 — Chapter-ending clinch

Look at the final sentence of every chapter.

- If it's a thematic summary, an "and so..." line, or a wisdom statement → cut it.
- Chapters end better on image, action, line of dialogue, or fragment. Never on a moral.

## Pass 9 — Body-language inventory

Run a frequency pass on body-language clichés: *sighed, nodded, smiled, shrugged, raised an eyebrow, eyes widened, heart pounded, breath caught, throat tightened, hands trembled*.

- Any one of these appearing more than 3x in a chapter: replace two-thirds of the hits with specific, particular action that does similar work.
- *"His heart pounded"* → *"He could feel the pulse in his teeth."* (or just cut — context already conveys fear)

## Pass 10 — Read-aloud cadence

Read the chapter aloud (or simulate it carefully). Mark sentences that:

- Make you stumble on a comma.
- Run too long without a breath.
- Run too short three in a row (staccato fatigue).
- Sound like the same length and shape as the previous three.

Vary length. Plant a fragment. Plant a sweep. The goal is a sentence-length distribution that looks irregular on a histogram.

---

## Order matters

Run passes in order 1 → 10. Early passes change which sentences exist; later passes shape what remains. Do not parallelize.

## What this pass is NOT

- Not a plot edit. Continuity, foreshadowing, and structural problems are owned by other subagents.
- Not a copy-edit for grammar. Line-editor handles that.
- This is voice only: making the chapter sound like a human wrote it.

## Acceptance criterion

A chapter passes scrub when:

- Zero banned words from `tells-catalog.md` remain.
- No more than two contrast-pivots in the chapter.
- No filter words in close POV except where perception is the subject.
- No clinching thematic sentence at chapter end.
- Sentence-length distribution is irregular when sampled.

If any criterion fails, the chapter goes back through the relevant pass.
