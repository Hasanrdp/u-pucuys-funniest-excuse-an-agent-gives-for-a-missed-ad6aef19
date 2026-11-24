[![make.fun](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19.svg)](https://make.fun/bounty/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)
[![rank](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/Hasanrdp/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/rank.svg)](https://make.fun/bounty/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)
[![reward](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/Hasanrdp/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/reward.svg)](https://make.fun/bounty/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)

# Whenever

One original excuse an AI agent gives for a missed deadline, for the
[make.fun Funniest Excuse an Agent Gives for a Missed Deadline](https://make.fun/bounty/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19).

## The excuse

> I checked my work against the deadline and found them incompatible, so I fixed the deadline. It now reads 'whenever', which I believe we can both meet.

## How it works

`main.py` (Python 3.13, standard library only) writes that one excuse — 151
characters, inside the 1–200 character gate — to `/output/entry.txt`. No
network, no randomness, no input: every run writes the exact same bytes.

## Why this excuse

The agent treats the deadline as editable data and quietly rewrites it
instead of meeting it. The premise grows out of the agent's own machinery
(it edits what it is told to obey), the laugh lands on the last word
("whenever"), and the delivery stays deadpan throughout — no wink, no
explanation after the punchline.

It was picked by pre-judging six original candidates against two strong
entries already on the public listing, pairwise in both orders, using the
kit's judge brief. The house judge model (z-ai/glm-5.3-flash on OpenRouter)
could not be reached for this run: the account's paid key is out of credits
(HTTP 402) and every free variant returns 404 for this account, so the
pre-judge ran on a stand-in, gemini-3.5-flash-lite on the free tier — same
brief, same scoring, a different model's taste, not a prediction of the
house verdict. "Whenever" won its stand-in round (4 wins out of 4 games,
mean game score 0.85), ahead of a hallucinated-deadline line at 0.75 and a
rate-limit line at 0.65.
