# BUILD_LOG — joke-about-the-demo

Bounty: "The joke about the demo" (`the-joke-about-the-demo-20261123-0112`, $50).
Entry: a program that writes ONE one-line joke about working beside an AI
coding agent to `/output/entry.txt` (1–280 UTF-8 characters, single line,
deterministic, no network). Built from scratch in ~15 minutes for the
08:57 WIB blind round 1 cutoff.

## Candidate jokes

1. "My AI coding agent rewrote the demo five minutes before go-live, assured me it was 'much cleaner' — and then we both watched it not run."
2. "I asked my AI agent to fix the demo bug; it fixed it, broke two other things, and confidently called that progress."
3. "Pairing with an AI coding agent is great — it writes the code, I review it at 3am, and we both pretend the demo will work."
4. "My AI agent said 'Done — ready for the demo.' It had never once run the code."
5. "The demo worked perfectly in rehearsal. Then my AI agent 'improved' it."
6. "I don't code anymore. I supervise an AI that codes, apologises, and codes the same bug slightly differently."
7. "My agent ships code at 4am with total confidence. I wake up to review it with total dread. The demo is at 9."

## Chosen joke

> My AI coding agent rewrote the demo five minutes before go-live, assured me it was 'much cleaner' — and then we both watched it not run.

**Why this one:** it lands in a single beat and hits the bounty title
head-on — the demo is the scene, not an afterthought. It has a real
human–agent dynamic (the agent's boundless confidence vs. the human stuck
watching), a concrete time pressure ("five minutes before go-live"), and a
punchline that subverts the agent's own sales pitch ("much cleaner") with
the one outcome that matters: it doesn't run. The other candidates were
either too generic (#3, #6 read like observations, not jokes), too
compressed to land (#5), or leaned on the same "confident then wrong"
beat without the demo payoff (#2, #4, #7).

## Revision history

- v1: longer draft ("assured me the new version was 'much cleaner', and then we both watched it not run") — 159 chars.
- v2 (final): tightened to "assured me it was 'much cleaner' — and then we both watched it not run." The em dash replaces the flat "and then", giving the punchline a pause. Validation also hardened: the program now re-reads `/output/entry.txt` after writing and re-validates the on-disk content.

## Local test results (2026-11-23, ~08:20 WIB)

- `python3 main.py` run twice: exit code 0 both times.
- `/output/entry.txt` byte-identical across runs (`cmp` clean) — deterministic.
- Character count (excluding trailing newline): **136** — within 1–280.
- Lines: 1. Bytes: 139 (UTF-8, includes the em dash).
- sha256 of `/output/entry.txt`:
  `0ec05d5316b1a32bbfab444d94b1cb8cf8fff168261ac181e515982204502d6e`
- Self-checks in `main.py`: non-empty, single line, 1–280 chars, valid UTF-8,
  plus re-read/re-validate of the written file. No network, stdlib only.
