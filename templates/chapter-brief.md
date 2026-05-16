# Chapter Brief — chapter <NN>

This document is produced by the orchestrator from the plotter's outputs + current continuity state. It is the drafter's working document. Drafter does not invent anything outside this brief without flagging.

## Identity

- chapter: <NN>
- pov: <character name>
- target words: <e.g. 4000 — loose>
- in-world time: <date, time of day, season>  ← flows into the chapter footer's `in-world-time:` key verbatim
- location(s): <primary, then any change locations>  ← primary flows into the footer's `location:` key
- voice-profile-active: <library/voice/<author>.md | genre-default>

> The drafter writes a chapter footer (HTML comment) using the exact key names defined in `subagents/drafter.md`. Two of those keys — `in-world-time:` and `location:` — come straight from this brief. A third — `characters-present:` — comes from the "Other characters present" table below plus the POV character. Use canonical character names from `series-bible/characters/cast-index.md` so the continuity index can match them.

## Beat(s) this chapter advances

From `plot/beat-sheet.md`:

- <beat name, position> — <what changes by end of chapter>

## Setups to plant

From `plot/setup-payoff.md`:

| id | description | how to plant (suggested) |
|----|-------------|--------------------------|
| S-NNN | <e.g. Mira's locket contains a map fragment> | <e.g. she touches it when frightened, no commentary> |

## Payoffs to fire

| id | setup origin (ch, what) | what fires here |
|----|--------------------------|------------------|
| S-NNN | ch X, <description> | <how it resolves now> |

## Knowledge state

### Start of chapter

POV character knows:
- <fact 1>
- <fact 2>
...

POV character believes (wrongly):
- <belief 1>
...

POV character does NOT know:
- <load-bearing fact 1>
...

### What POV learns this chapter

- <learning 1>
- <learning 2>

### What POV still doesn't know at end

- <ongoing gap 1>

## Other characters present

| Character | Knowledge entering scene | What they're hiding | What they will reveal |
|-----------|--------------------------|----------------------|------------------------|
| ... | ... | ... | ... |

## Continuity touchpoints

- Carry from previous chapter: <last image, tonal note, unresolved beat>
- Open setups warmed this chapter: <S-NNN, light reminder>
- Avoid: <known continuity hazards — e.g. don't reveal X yet, don't let Y be in this scene>

## Scene plan (loose)

The drafter may restructure scenes, but should cover:

1. <Scene 1 — goal, conflict, disaster>
2. <Scene 2 — reaction, dilemma, decision>
3. <Scene 3 — next goal>

## Chapter exit

- End on: <image | action | line of dialogue>
- Hook tension: <what question is the reader left holding>
- Hand-off to next chapter: <POV change? Time jump? Location change?>
