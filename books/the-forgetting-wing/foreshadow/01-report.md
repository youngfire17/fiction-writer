# Foreshadow report — chapter 01

- chapter: 01
- POV: Maren Vasse
- body word count (per line-edit footer): 3,362
- pipeline status: post-drafter, post-voice-scrubber, post-line-editor, post-continuity-checker, post-foreshadowing-tracker
- pass verdict: **pass**
- total setup-payoff rows in graph: **46** (after rebuild; was already 46 at pass open — see S-006 note below)

## S-006 row repair

The continuity-checker handed off with a flag that `setup-payoff.md` row S-006 had only 6 pipes (5 cells) instead of 7, causing the parser to skip it and report `threads=45`. On opening the file I found the row already in canonical 7-cell form: `| id | description | type | planted | payoff | status | notes |`. Splitting line 16 on `|` yields 9 segments (leading empty, 7 content cells, trailing newline) — the same shape as S-001 and every other row. The pre-handoff repair was already in place. I ran `python tools/build_continuity_index.py books/the-forgetting-wing/` and confirmed:

- threads: **46** (was 45 in continuity-checker's pre-handoff state; now correct)
- events: **1** (chapter-1 footer ingested — the script glob did pick up `01.md` after all; continuity-checker's filename-glob flag is also resolved)

S-006's payoff cell currently reads: `ch 19: Pell shows Maren a photograph of Eira-at-six that Pell took and signed with her stitched cross-thread; ch 26: in memory, the apartment wall with one photograph propped on the rail`. Status: `partial fire`. The behind-the-board residue is correctly held in S-037 as `defer:book-2`. No further edit applied.

No other rows required structural repair.

## Ch 1 plant audit (S-001 through S-006)

All six chapter-1 setups required by `chapter-list.md` row 1 are physically on the page in the chapter as written and match each row's `planted (ch, what)` description. The `notes` cell of each row already carries a `ch1-plant-confirmed: line N` annotation from the continuity-checker / pre-handoff pass. I re-validated each against the prose:

- **S-001 — body in Sennet's Alley.** Planted on the page. Lines 39-51 (body, single wound below the third button, fan of darker grey on the wool, frost on the sleeve as time-of-death proxy), line 83 (he had been someone), line 87 (camera-gap routed via Lo — *Lo had said so once at the table…Someone had filed it and used it*). No name leaked. Satisfies row description.
- **S-002 — paring knife as kitchen weapon / frame.** Planted on the page. Line 3 (opening line — knife in her hand on waking), line 5 (three-knuckle paring grip, chip at the heel, Cant-issue with worn wooden scale), lines 95-97 (wrapped inside the cuff against forearm, blade pointed back at her own wrist), lines 159-163 (Lo's wooden block, three slots, two paring blades, empty third slot matching the wrapped knife). Frame-implication landed without exposition. Satisfies row description.
- **S-003 — three days of memory Maren should not have.** Planted on the page. Lines 27-33 (Review eleven days ago, eighth of last month as the official gap, three days arriving "at angles" since the second morning). Drift-seed lines 73-77 (bread-smell on the wind from Lowmaren, doorway with a metal lip, hand near her shoulder not touching her — walled by *That had not been a memory. That had been the room next door to a memory*). This is the row's planted-component AND the day-1 seed for the ch-9 surfacing (S-023). Satisfies row description.
- **S-004 — children's rhyme.** Planted on the page. All four canonical lines from cultures.md sung by the third-floor Cant grandmother on Helvet Stair (lines 121, 125, 131, 137 — *One little hand to take the day / One little hand to pass it on / One little day for the city's sake / Wake up clean, wake up gone*). Maren registers the third line as new menace (lines 133-135). Satisfies row description.
- **S-005 — Lo's *eat something* tic.** Planted on the page. Line 171 ("Have you eaten?") asked after the half-second port-tech glance at the door (line 157). Maren lies in line 175 ("I had bread on the way. At the corner."). Chapter closes on the lie and Lo's tea-pour (line 177). The deferral-as-love mechanism is baseline-established. Satisfies row description.
- **S-006 — Maren's blank wall / loose pine board.** Planted on the page, lightly, inside Maren's interiority at the doorframe (line 173 — *the bare wall above my cot. The lamp on the shelf above the cot. The pine board behind the lamp. The board is still loose. It has been loose for years. Nothing has changed. … I will not touch the board. … not yet.*). Maren actively chooses not to investigate — the deferral is the seed of S-037's `defer:book-2` resolution. Satisfies row description.

Verdict per row: **pass / pass / pass / pass / pass / pass.** No status field changed for S-001 through S-006 — per project policy, status columns describe target end-of-book status, not draft state. Notes-column `ch1-plant-confirmed:` annotations are present.

## New canon, unrowed candidates (the drafter's free additions)

- **Recovery sleeve on Maren's left wrist (line 29).** Ratified as canon in `maren.md` by the continuity-checker. Biotech texture / Wing-procedure marker. No setup-payoff implication: the sleeve is a one-time presence-marker, never tracked elsewhere in the chapter list. **Verdict: texture, no row needed.**
- **Chemical-burn left-wrist detail (line 67).** Already-canon character marker (maren.md). Surfaced on-page now. Not a chekhov — it is identity/age texture. **Verdict: texture, no row needed.**
- **Helvet Stair seventh-tread hairline crack (line 143).** Ratified in `geography.md` per drafter flag. Used here as a Cant-child competence beat ("known about since she was eight") and as a small evasion-of-noise demonstration. Not flagged in `chapter-list.md` for a future payoff. Could plausibly resurface in ch 12 (Cant stairwell scene with Sael) or ch 22 (Maren passes the stairwell again), but the chapter list does not reserve it as a setup. **Verdict: texture / competence demonstration, no row needed.** If the drafter wants to weaponize the tread (e.g. as an evasion beat in ch 12), flag back to the plotter and I will add a row.
- **Empty third slot in Lo's wooden knife block (lines 159-163).** Already captured inside S-002 notes ("three slots, two paring blades, empty third slot matches the wrapped knife exactly"). Confirmed live. **Verdict: already tracked.**
- **Lo's "did not pour yet" / resin-on-hands smell (lines 103, 171).** Pacing-and-texture detail; the not-pouring resolves within the scene (line 177 — Lo pours the tea). Resin-on-hands is Lo's competence-as-mask texture per lo-vasse.md. **Verdict: texture, no row needed.**
- **The folded paper bird Maren took from the recovery nurse (line 29).** *Borderline.* The pamphlet-as-folded-object is canonical Cant culture (core-rule.md: "Every household has a stack of them. Children fold them into boats"). The recovery-bay nurse folding them into *birds* and Maren *taking one without asking* is on-page texture not anticipated in `chapter-list.md`. The detail is doing characterization work (Maren claims a small comfort from a stranger; the recovery bay is humanized for an instant). There is no scheduled payoff. **Verdict: AMBIGUOUS — flagged to user (see Flags below).** I am not adding a row per the spec rule against inventing setups.

## Graph health

After rebuild:

- **Total threads in graph:** 46 (canon).
- **Plant-side status reflected for ch-1 plants:** S-001 through S-006 carry `ch1-plant-confirmed: line N` in notes; status columns unchanged (they describe end-of-book status per project convention).
- **`fired` count in status column:** 38 (per plotter's summary; status field describes intended end-of-book state, not drafted state).
- **`defer:book-2` count (rows with `defer:book-2` somewhere in status field):** 5 rows have it as their primary status (S-033, S-035, S-037, S-038, S-041); a further 10 rows are `partial fire` or `fired in book 1` with a `defer:book-2` sub-component documented in notes. Total touch count: **15** rows touch book 2, matching plotter's summary.
- **`planted` count, raw status field:** 0 rows currently sit at literal `planted` status — every row already projects forward to its end-of-book state. This is correct for the project's status-as-target-state convention.
- **`armed` count, raw status field:** 0 (same reason).
- **`abandoned-with-justification`:** 0.

**Mismatch-with-plotter check:** The plotter's summary says 46 / 38 fired / 15 touching book 2. After rebuild and the S-006 row check, graph confirms 46 / 38 fired / 15 touching book 2. **No mismatch.** Important: only ch 1 is drafted; most "fired" entries are still future-tense in prose. Status columns describe target, not draft state. This is by design.

## Unfired risk list

After scanning every row for `planted (ch, what)` chapter ≤ 1 vs. on-page confirmation:

- Rows with planted-chapter = 1: S-001, S-002, S-003, S-004, S-005, S-006. All six confirmed on-page (above). **Zero unfired risk for ch 1.**
- Rows with planted-chapter in early single digits but drawing on canon ratified through ch 1 (the camera-gap-via-Lo route-of-knowledge for S-001, the bread-smell drift-seed for S-023, the rhyme for S-031 / Charter-author setups): all canon dependencies are in place. No row depends on canon that has shifted.
- One Maren-ghost row (S-046, plum trees in Lowmaren — Eira's kitchen instruction at twelve) lists its plant as "referenced by Maren's interiority in ch 1, ch 15, ch 19, ch 22." Ch 1 does not reference the plum trees by name on the page; Maren's mother is referenced only obliquely ("the aunt's clinic stories"). This is consistent with the row's framing — the plum trees are Maren's prior canon, not a new chapter-1 plant; the ch-1 reference is in the *background of Maren's interiority*, not on the page as text. **Not a risk** — the row is honest about being canon-prior. Flagging only so the user knows the row's "ch 1 reference" is implicit and the explicit on-page mention will land in ch 15 / 19 / 22.

## Recommendations for ch 2 (Sael POV)

Setups the next chapter must carry forward, per `chapter-list.md` row 2 and `beat-sheet.md` B-03:

- **Plant S-007** (W-I clearance brass pin behind Iven's left ear in the alley-file photograph). Sael sees the pin in the file before he reaches the alley. Reader is told the pin is wrong; Sael lists it as one of three things wrong with the file.
- **Plant S-008** (case routed to Iren without an Audit stamp). Anomaly 1 of three on Sael's list.
- **Plant S-009** (Iren recommended Sael for the case). Anomaly 3 of three on Sael's list. Sael accepts the recommendation as flattering.
- **Plant S-010** (Sael's carrothenidine dose schedule on his desk, the count habit). Capability AND threat; the first time count-grammar appears on the page.

Carry-forward from ch 1 that ch 2 must honor (mostly negative-space — Sael does not yet know any of this; the reader holds it):

- The body in the alley is the same body Sael will see in the file. Sael does NOT know Maren is connected. Maren's name does not appear in ch 2 — the W-I pin and the no-Audit-stamp are the engine of Sael's chapter, not Maren.
- The reader has the camera-gap (S-001 notes). Sael in ch 2 has the routing slip but does not have the camera-gap insight (Maren did, via Lo). The reader holds the asymmetry.
- The drift-seed (S-003 / S-023 day-1 fragment) is in the reader's head. Sael does not have it. No carry needed; the asymmetry is the engine.
- No callbacks from ch 1 to plant in ch 2. Ch 2 is pure Sael-side setup. The first cross-POV touch is ch 3 (Field Recovery at the door of 17 Helvet Stair).

No ch-1 setup needs a re-touch in ch 2. S-001 (the body) is the natural overlap — Sael sees the same body in photo, but seeing it through his eyes is the chapter's job, not a re-touch.

## Flags for the user

1. **Paper bird (line 29) — texture or chekhov?** Maren takes a folded-paper bird from the recovery bay nurse "without asking." The detail is on-page, doing characterization work, and is not anticipated in `chapter-list.md`. I have not added a row. If the plotter wants this as a future chekhov (e.g., something Maren puts on the rail in ch 26's resolution mirror, or something Lo finds in Maren's coat pocket in ch 3, or a memento that surfaces near the climax), say so and I will add an S-NNN row with a planned payoff. If it is pure texture, no action needed — but documenting the flag so we don't accidentally pay it off later without having tracked it.

2. **Seventh-tread hairline crack (line 143) — competence beat or future-evasion chekhov?** Currently treated as texture / age-marker. If the drafter wants to use it in ch 12 (Cant-stairwell scene) as a small evasion beat against Sael — Maren steps over the tread, Sael does not — the setup would benefit from a tracked row. Flagging for plotter decision.

3. **S-006 row reported as malformed in the continuity-checker handoff is not malformed at the time of this pass.** Either the continuity-checker repaired it silently during its own pass, or a prior repair landed between handoffs. Threads count is 46. Events count is 1 (the continuity-checker's filename-glob flag also no longer applies — the rebuilt index ingests `01.md` cleanly). Documenting for the record.

4. **No paranormal drift detected.** All ch-1 plants remain inside biotech / training / psychological / institutional space. Drift-grammar fragment in line 73 is mechanically grounded in stitch-resurfacing (per biotech-system.md), not spirit-memory.

## Tracker notes

- No edits applied to `setup-payoff.md` this pass. The file was already in canonical 7-cell shape for all 46 rows; the `ch1-plant-confirmed: line N` annotations for S-001 through S-006 were already present in the notes column from the pre-handoff state; no status column required changing per the project's status-as-target-state convention.
- Index rebuilt clean: `python tools/build_continuity_index.py books/the-forgetting-wing/` → `{'characters': 8, 'locations': 11, 'events': 1, 'threads': 46, 'world_rules': 0}`.
- Per-spec: I do not write prose. I do not invent setups. Paper-bird and seventh-tread are flagged to the user, not added.
- Drafter's footer claim ("planted: S-001…S-006; fired: none") matches what is on the page. Footer ratified.
