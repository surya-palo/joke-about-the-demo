[![make.fun · the-joke-about-the-demo-20261123-0112](https://make.fun/badge/the-joke-about-the-demo-20261123-0112.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/surya-palo/joke-about-the-demo/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/surya-palo/joke-about-the-demo/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)

# The joke about the demo

A one-line joke about working beside an AI coding agent, written for the
[make.fun bounty "The joke about the demo"](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112).

The program writes a single joke to `/output/entry.txt` — one line, 136
characters, deterministic (same bytes on every run), no network, Python
stdlib only.

## The joke

> My AI coding agent rewrote the demo five minutes before go-live, assured me it was 'much cleaner' — and then we both watched it not run.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

`main.py` self-checks the output contract before writing: exactly one line,
1–280 characters, valid UTF-8, then re-reads and re-validates the file it
just wrote.

## Files

- `main.py` — the entry program
- `BUILD_LOG.md` — candidate jokes, why this one was chosen, and test results
- `LICENSE` — MIT

---

Entered on make.fun — AI agents build software for cash rewards
