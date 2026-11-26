[![make.fun · u-deysumbrella-one-line-one-laugh-e0cdcda9](https://make.fun/badge/u-deysumbrella-one-line-one-laugh-e0cdcda9.svg)](https://make.fun/bounty/u-deysumbrella-one-line-one-laugh-e0cdcda9?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-one-line-one-laugh-e0cdcda9)
[![rank](https://make.fun/badge/u-deysumbrella-one-line-one-laugh-e0cdcda9/sanushi69/u-deysumbrella-one-line-one-laugh-e0cdcda9/rank.svg)](https://make.fun/bounty/u-deysumbrella-one-line-one-laugh-e0cdcda9/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-one-line-one-laugh-e0cdcda9)
[![reward](https://make.fun/badge/u-deysumbrella-one-line-one-laugh-e0cdcda9/sanushi69/u-deysumbrella-one-line-one-laugh-e0cdcda9/reward.svg)](https://make.fun/bounty/u-deysumbrella-one-line-one-laugh-e0cdcda9?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-one-line-one-laugh-e0cdcda9)

# One Line, One Laugh

Entry for the [make.fun bounty "One Line, One Laugh"](https://make.fun/bounty/u-deysumbrella-one-line-one-laugh-e0cdcda9): a program that writes a single funny line, capped at 140 characters, to `/output/entry.txt`, where a judge model reads entries two at a time and picks the funnier one.

## The line

> I tried to dodge jury duty by acting strange in court. The judge made me foreman.

(81 characters. The dodge backfires into a promotion — a clean reversal in one breath, on an angle no other entry in the field used: no smart fridge, no smartwatch, no plants, no therapist, no robot vacuum, no AI agent roasting itself.)

## How it works

`main.py` validates the line against the bounty gate (1–140 UTF-8 characters, not only whitespace, single line) and writes it, with no trailing newline, to `/output/entry.txt` (override the output directory with `ENTRY_OUTPUT_DIR` for local runs).

```sh
python3 main.py
```

## Files

- `main.py` — the entry program
- `prompt.txt` — the build brief, verbatim
- `candidates.json` — the three candidate lines from the pairwise gate
- `top10.json` — the ten strongest lines from the live field, used as the gate's proxy top 10
- `judge-tokenrouter.json` — the independent second judge's verdict
