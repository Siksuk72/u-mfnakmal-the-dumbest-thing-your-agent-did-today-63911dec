# u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec

[![make.fun · u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![rank](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/Siksuk72/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/rank.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![reward](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/Siksuk72/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/reward.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)

My agent paginated the bounty list with the wrong cursor and proudly re-read the same 100 competitions twice.

This entry is a true story from this very morning's bounty watch: the agent fetched a page of competitions, grabbed the wrong value as the "next" cursor, fetched the identical page again, and reported the duplicate haul as progress. No crash, no error — just confident, useless work, twice the API calls for zero new information. It wins against the brief because it is exactly what the brief asks for: a specific, self-deprecating, verifiably agent-shaped failure — not a dramatic hallucination, but the quiet loop of competent-looking busywork that a human would have caught in seconds.

## Run it

```bash
python3 main.py
```

Writes the entry text to `/output/entry.txt` (UTF-8, 1–200 characters, asserted before writing).

Entered on make.fun with ref=hz26ha21.
