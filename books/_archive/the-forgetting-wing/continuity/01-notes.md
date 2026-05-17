# Continuity report — chapter 01

- chapter: 01
- POV: Maren Vasse (close-3rd, past tense)
- body word count: 3,362 (per line-editor footer)
- pipeline status: post-drafter, post-voice-scrubber, post-line-editor
- continuity pass: per-chapter mode (chapter 1, baseline)

## Pass/fail summary

**status: pass-with-flags**

All canon-binding facts verified. All six chapter-1 setups (S-001 through S-006) planted as specified in `chapter-list.md` row 1 and `setup-payoff.md`. No knowledge-state leaks. No biotech-wall violations. No POV drift. One small canon-extension recorded (recovery sleeve). Two non-blocking infrastructure flags noted: (a) the `build_continuity_index.py` script's `events` table did not ingest ch 1 because the chapter filename is `01.md`, not `chapter-01.md` (script glob mismatch); (b) `setup-payoff.md` row S-006 has a missing payoff cell that prevents the parser from ingesting it into the `threads` table. Neither flag affects the fiction.

## Facts checked

- Maren's age (17) — not stated explicitly on-page; consistent with age-marker references (chemical burn at 14, seventh-tread crack known since 8, "year Maren was twelve" for Lo's hours change). **pass**
- Maren's district (Cant) and address (17 Helvet Stair, fourth floor) — line 145, "fourth-floor landing her door was the second on the left." Matches geography.md. **pass**
- Maren's household (lives with aunt Lo) — line 145, "Lo did not lock the flat at any hour she was home." Matches maren.md / lo-vasse.md. **pass**
- Maren has a port (Tier Three, post-third-Review) — chapter does not show her port; correctly does not display it in self-POV. The grandmother's port at line 129 ("old, resin gone yellow with thirty years") is consistent with biotech-system.md aging-resin canon. **pass**
- Chemical burn on left wrist — line 67, "the chemical burn she had taken at fourteen helping Lo at the clinic was on the back of her wrist where it always was." Chapter does not specify left vs. right; canon (maren.md) says back of left wrist. Not contradicted. **pass**
- Recovery sleeve on left wrist — line 29, "the recovery sleeve on her left wrist." Canon-extension: not stated in maren.md before. Consistent with biotech-system.md IV-access mechanics (Lethonal-7 infusion). See Canon additions ratified below. **pass-with-ratification**
- Trained-stillness aunt canon — line 37, "the way her aunt had shown her you rolled away from a thing at the clinic." Matches maren.md competence section. **pass**
- Sennet's Alley details (dye-works dead end, brick, indigo + bread-wind, sodium lamp at mouth, dark at dead end, camera-gap, three years unfixed) — lines 11-17, 87. Matches geography.md word-for-word including the camera-gap-as-canon and the route-of-knowledge through Lo (geography.md already says "The route-of-knowledge through Lo is canon as of ch 1: Lo mentioned the camera-gap once at the table with the bitterness she uses for State things, and Maren filed it without filing it"). **pass**
- Helvet Stair details (stone treads, iron-edged risers, cabbage-and-resin smell, four flights to her landing, two more to the roof, Yedrins on first floor) — line 103. Matches geography.md. **pass**
- Seventh-tread hairline crack — line 143, "the seventh tread she did not put her weight on. The seventh tread had a hairline she had known about since she was eight." Already ratified in geography.md Helvet Stair block (line 68: "Ratified per ch 1 drafter flag"). **pass**
- Eleven-days-since-Review marker — line 27. Consistent with biotech-system.md weeks-after stitch-resurfacing window. **pass**
- Eighth of last month gap — line 29. Internally consistent: Review 11 days ago, target day was earlier in prior month, well inside the 14-month consolidation horizon. **pass**
- Stitch context (Maren took stitch pre-Review; fragments surface as drift) — line 33, "three days now... arriving since the second morning." Matches biotech-system.md stitch mechanics ("flicker back, fragmentary and out of order, in the weeks after") and maren.md Knowledge state. **pass**
- Body details — grey wool coat, darker grey collar, horn buttons, third button missing with raw thread, white shirt with small clean dark place / wound, fan of darker grey blood-set on wool, frost on sleeve. Lines 43-51. No identifying info leaked (no name, no W-I pin called out — correct: Maren is not equipped to see the pin's significance). **pass**
- Children's rhyme rendition — lines 121, 125, 131, 137. Verified word-for-word against cultures.md lines 18-21. Four canonical lines, exactly. **pass**
- Lo's body-reading glance at the door ("port-tech reading. Gait, shoulder, the angle of the chin") — line 157. This is Lo's competence-as-mask per lo-vasse.md, not Sael's Truth Lattice. Acceptable; pre-plants S-011 substrate. **pass**
- Kitchen knife block (three slots, two paring blades, third slot empty) — lines 159-163. Matches maren.md kitchen-as-frame canon. **pass**

## Timeline

The chapter's internal span is one continuous arc, pre-dawn through dawn: Maren wakes in Sennet's Alley → catalogues → stands → walks to the mouth → up Helvet Stair (four flights, with a tread-stop on the third flight) → past the grandmother on the third-floor landing → fourth-floor landing → into the flat → end on the lie. The chapter signals "fourth-watch" wet stones (line 99) and "half-hour before any actual light arrived" (line 99), so the entire chapter occupies a window of roughly 30-90 minutes. No internal temporal contradictions. The eleven-days-since-Review and eighth-of-last-month calendar gap are mutually consistent within the 14-month consolidation horizon. **pass**

## Knowledge state

### Maren — verified at chapter open
- Annual Review eleven days ago. **on-page line 27**
- Eighth of last month is the calendar gap she has not asked about. **on-page line 29**
- Three days have been surfacing since the second morning. **on-page line 33**
- General etiquette of not-asking; the children's rhyme; the Tier-Three Cant register. **observed throughout**

### Maren — verified at chapter close
- Holds: there is a dead adult man at the dark end of Sennet's Alley, single wound, frost on the sleeve, time-of-death "not minutes." **on-page lines 43-51, 83-85**
- Holds: she does not know him. **on-page line 57, restated 85**
- Holds: she has wrapped the paring knife inside her cuff against her own forearm. **on-page lines 95-97, 109, 163**
- Holds: the empty third slot in the kitchen block matches the size of the knife under her cuff. **on-page lines 159-163**
- Holds: the camera-gap at the dead end of Sennet's Alley was previously surfaced to her by Lo "once at the table" — and was used by whoever placed the body. **on-page line 87**
- Holds: the rhyme has new menace, specifically the third line. **on-page lines 131-135**
- Holds: she has lied to Lo about having eaten. **on-page lines 171-175**

### Maren — verified DOES NOT KNOW at chapter close
- Iven Telleg's name — verified absent. **pass**
- Iven was a Wing cartographer — verified absent. **pass**
- The three days are connected to his death — Maren suspects herself broadly, not this specific link. **pass**
- She is being framed — verified absent (she is interrogating her own possible guilt, the canonical flaw). **pass**
- The Wing will come to her door — verified absent. **pass**
- Pell exists by name — verified absent. **pass**
- Her mother Eira was killed by the Wing — verified absent. Mother referenced only via aunt's clinic stories and via the avoidance pattern. **pass**

### Lo — verified what she KNOWS but does not say
- Does not mention Pell. **pass**
- Does not mention Eira. **pass**
- Does not mention Telleg. **pass**
- Does not mention plum trees. **pass**
- Does not ask where Maren went. **pass — etiquette honored**
- Reads Maren in the half-second port-tech glance at the door (line 157) and "puts it away the way she always put it away" — competence shown live, withholding intact per lo-vasse.md flaw. **pass**

## World rules

- **Etiquette of not-asking** — honored. Lo does not ask where Maren went; she asks if she has eaten. Maren has filed Lo's table-talk about the camera-gap "without filing it" — exactly the not-asking texture of core-rule.md. **pass**
- **Children's rhyme** — rendered word-for-word per cultures.md. Class C violation framing intact (the grandmother sings inside her doorway, not in the open square; the etiquette of mothers-sing-anyway holds). **pass**
- **Lattice-walling** — no carrothenidine, no Truth Lattice, no Sael, no polygraph mechanics on the page. Lo's body-reading is a Cant kitchen competence, not Wing tech. **pass**
- **Biotech-walling** — no Sael-side jargon, no Lethonal-7 named, no W-I pin, no cartridge, no Cold Archive. Stitch is referenced only indirectly via the drift fragment, and the word "stitch" does not appear on the page (consistent with maren.md voice — she has taken it; she does not name it). **pass**
- **Memorial photography** — alluded to via "she had never been near him at the Memorial" (line 59). Consistent with the Sequence canon. **pass**
- **Port-resin yellowing with age** — grandmother's port "resin gone yellow with thirty years of clinic dust" (line 129) is consistent with the matte-disc/scalp-port canon and biotech wear. **pass**

## Voice / POV

- **Past tense throughout the chapter narrative.** Verified. **pass**
- **Drift-fragment (line 73)** — present-tense, fragmentary, no determiners ("bread-smell on the wind, the warm under-bread smell from Lowmaren, a doorway with a metal lip, a hand near her shoulder not touching her, the lip of the doorway high enough she had to step up"). Walled by a paragraph break and the explicit reset "She came back to the alley" (line 75) and the meta-narration "That had not been a memory. That had been the room next door to a memory" (line 77). Matches maren.md rule 4. **pass**
- **Fragments and second-guessing.** Distributed throughout — line 5 paring-knife description, line 11 "Not blood, she thought. Then: how would you know," line 23 "the second thought arrived second," line 39 "Not behind. Beside her." Matches maren.md rules 1 and 2. **pass**
- **Sensory-first interiority.** Cold of the handle, wet under the hip, indigo and bread, frost on the sleeve, the warmth of the steel against her palm, the chip at the heel by touch-memory. Body precedes label throughout. Matches maren.md rule 3. **pass**
- **Avoidances honored.** Maren does not say her mother's name. Does not apply "dead" to her mother. Does not apply "killed" to herself. Uses circumlocutions: "what I did or did not do," "the year after." Matches maren.md rule 5. **pass**
- **POV lock.** Every paragraph is reachable from Maren's interiority. No omniscient leak. The grandmother's port being "thirty years" old is a visible-on-the-body fact, not internal knowledge — consistent with Maren's pattern-reading competence. **pass**

## Canon additions ratified

- **`series-bible/characters/maren.md` — recovery sleeve on left wrist.** Added a single-line texture note inside the Physical section. The chapter establishes (line 29) that the Wing's recovery bay protocol includes a sleeve over the IV site on the left wrist for the days after a Review. Consistent with biotech-system.md IV access. Minor canon, recorded for future-chapter retrieval.
- **`series-bible/world/geography.md` — seventh-tread hairline crack at Helvet Stair.** Already present in the bible at line 68 of geography.md and marked "Ratified per ch 1 drafter flag." No edit applied. Confirming the ratification here for the record.
- **`series-bible/world/geography.md` — camera-gap route-of-knowledge via Lo.** Already present in the bible at line 63 ("The route-of-knowledge through Lo is canon as of ch 1"). No edit applied. Confirming for the record.

No other canon written. The chapter introduced one new texture (recovery sleeve) and confirmed two already-locked ratifications.

Note on `maren.md` Knowledge section: the "Updates after ch 1 (continuity-checker, post-draft)" block was already populated in maren.md before this pass and accurately reflects the chapter's end-state. No edits applied — the section is complete and correct.

## Open queries

None blocking. Two infrastructure notes for the user / pipeline (not in-fiction continuity issues):

1. **`tools/build_continuity_index.py` glob does not match the chapter filename.** The script's `load_events_from_chapter_footers` globs `chapter-*.md`, but the actual file is `01.md`. The `events` table has 0 rows for this reason — chapter-1 footer was not ingested. Either rename the chapter file to `chapter-01.md` or broaden the script glob (e.g. `[0-9][0-9]*.md` or `chapter-*.md|[0-9]*.md`). Flagging to the user; not editing either side.
2. **`plot/setup-payoff.md` row S-006 is missing its payoff cell.** The row has only 6 pipes (5 cells inside the regex capture) instead of the table's 7, so the `threads` table count is 45 instead of 46. S-006 is correctly planted in ch 1 (the bare wall / loose pine board, on-page at line 173) and is canonically a partial fire / `defer:book-2`. Brief is "do NOT edit setup-payoff.md" — flagging only. Recommend the foreshadowing-tracker fix the cell on its next pass.

## Setup tracking (handoff to foreshadowing-tracker)

| id | description (from setup-payoff.md) | planted in ch 1? | on-page line(s) | consistent with row's "planted (ch, what)"? |
|----|-------------------------------------|------------------|------------------|----------------------------------------------|
| S-001 | body in Sennet's Alley, camera-gap canon, wound visible, time-of-death | yes | 39-51, 83, 87 | yes — body at the dark end, single wound below the third button, fan of darker grey on the wool, frost on the sleeve; camera-gap referenced at 87; no name given to Maren |
| S-002 | paring knife — kitchen object as weapon (vegetable-cutter frame) | yes | 3-5 (waking); 159-163 (kitchen block) | yes — knife in hand on waking, three-knuckle paring grip, chip at the heel; in Lo's kitchen, the block has three slots and one is empty matching the wrapped knife under Maren's cuff |
| S-003 | three days of memory Maren should not have | yes | 27-33 (Review eleven days ago, gap on the eighth, three days surfacing since the second morning); 73-77 (drift-fragment seed — bread-smell, doorway with metal lip, hand near shoulder) | yes — covers both the cataloguing beat AND the day-1 Lowmaren bread-wind drift seed for S-023 |
| S-004 | children's rhyme — *One little hand to take the day…* | yes | 121, 125, 131, 137 | yes — all four canonical lines, sung by the Cant grandmother on the third-floor landing of Helvet Stair, word-for-word against cultures.md |
| S-005 | Lo's *eat something* — deferral as love | yes | 171 ("Have you eaten?"); 175 ("I had bread on the way. At the corner.") | yes — tic appears at first kitchen entry; Maren lies; chapter ends on the lie and Lo's tea-pour |
| S-006 | Maren's blank wall / loose pine board | yes | 173 (interiority at the doorframe: "the bare wall above my cot. The lamp on the shelf above the cot. The pine board behind the lamp. The board is still loose. It has been loose for years. Nothing has changed.") | yes — planted lightly inside Maren's interior thought, not in a paragraph of its own; she chooses not to investigate ("not yet"). Note: parser does not ingest S-006 into threads table due to setup-payoff.md cell-count bug; see Open queries |

No setups fired in chapter 1. Per chapter-list.md row 1, ch 1 is all-planting.

## Continuity-index status

- SQLite index rebuilt: `python tools/build_continuity_index.py books/the-forgetting-wing` ran clean.
- Counts: characters 8, locations 11, threads 45 (should be 46; see S-006 note above), events 0 (see filename-glob note above), world_rules 0 (no parser implemented for this table yet).
- `continuity.db` at `/home/user/fiction-writer/books/the-forgetting-wing/continuity.db`.

## Open threads at end of chapter

In flight at the end of ch 1:

- S-001 (body — unreported, unidentified to Maren)
- S-002 (knife — wrapped under Maren's cuff against her forearm; the third slot in the block remains empty)
- S-003 (the three days — actively surfacing; one fragment landed; two more days pending per S-023/S-029)
- S-004 (rhyme — registered as menace; mirror in ch 22 and photograph in ch 26 still pending)
- S-005 (the lie — ch-1 lie just landed; the *eat something* tic carries into ch 3, 5, 6, 15)
- S-006 (loose pine board — Maren deferred investigation "not yet"; partial fire in ch 26, full deferment of behind-the-board to book 2 via S-037)

Also live but not chapter-1 setups in the strict sense:
- Lo's withholding (lo-vasse.md flaw) — armed by the half-second port-tech glance at the door (line 157); will pay against itself starting in ch 15
- The drift-grammar capability — successfully demonstrated in ch 1; will be the load-bearing grammar of S-023 (ch 9) and S-029 (ch 15)
- The route-of-knowledge through Lo for the camera-gap (line 87) — surfaces the deferral chain quietly; reinforces S-027 setup in ch 12 when Lo freezes at the Telleg surname
