# Day Trading: A Beginner's Curriculum

An honest, research-grounded introduction to day trading — what it is, how the
mechanics actually work, what the evidence says about outcomes, and how to
approach it if you decide to proceed.

---

## Read this part first

This curriculum was written by Claude (an AI assistant). It is not written by a
professional trader, and it is not investment advice. That matters, so it is
stated up front rather than buried.

It also means this guide has nothing to sell you. That turns out to be the single
biggest difference between this and most day trading education you will find.

**The evidence on day trading outcomes is unusually clear, and unusually bad.**
Three of the most rigorous studies ever conducted:

| Study | Market & period | Finding |
|---|---|---|
| Chague, De-Losso & Giovannetti (2020) | Brazilian equity futures, 2013–2015 | Of individuals who day traded for **more than 300 days**, **97% lost money**. Only 1.1% earned more than the Brazilian minimum wage. |
| Barber, Lee, Liu & Odean (2014) | All Taiwanese day traders, 1992–2006 | **Less than 1%** of day traders could predictably and reliably earn positive abnormal returns net of fees. |
| Barber, Lee, Liu & Odean (2020) | Taiwan | Day traders lost an average of **23.9 basis points per day** net of fees; aggregate performance was reliably negative in 14 of 15 years. |

The Brazilian study is the one worth sitting with longest. The researchers looked
specifically at people who *persisted* — who did not quit after a bad month, who
put in the screen time that every course tells you is the missing ingredient.
Their regression analysis found **no evidence of learning through experience**.
Persistence, on its own, did not produce improvement.

That is the actual base rate. Any guide that opens with lifestyle imagery instead
of this table is selling something.

### What this does *not* mean

It does not mean day trading is impossible or that everyone who does it is a
fool. The Barber et al. data also shows something more interesting: there is
genuine, persistent skill in the cross-section. Top-ranked day traders in one
year went on to earn **+37.9 bps per day after fees** in the following year,
while bottom-ranked traders earned **−28.9 bps**. That is not noise. Skill is
real and it persists.

It is just extremely rare, and the population that has it is small enough that
your prior should be that you are not in it until your own audited results say
otherwise.

The right frame is not "can this be done?" — it can. The right frame is: *this is
a competitive professional field where you are the newest entrant, competing
against firms with better data, better latency, better capital, and full-time
research staff.* Treat it like applying to a hard profession, not like finding a
hack.

### The correct alternative, stated plainly

For almost everyone whose actual goal is "grow my money," low-cost broad-market
index funds held for decades beat day trading after fees and taxes, with a
fraction of the time cost. If your goal is wealth, that is the answer and you can
stop reading here.

Continue if your goal is to *learn the craft* — with money you can afford to lose
entirely, treating early losses as tuition.

---

## The curriculum

Work through these in order. Do not skip to the setups chapter; it is the least
important one, and it will not help you without the four that precede it.

| # | Chapter | What it covers |
|---|---|---|
| 01 | [The Math of the Game](01-the-math-of-the-game.md) | Expectancy, edge, transaction costs, why most traders lose |
| 02 | [Market Mechanics](02-market-mechanics.md) | Order types, the spread, liquidity, market structure, the trading day |
| 03 | [Getting Started](03-getting-started.md) | Accounts, current regulation, brokers, and a 90-day on-ramp |
| 04 | [Risk Management](04-risk-management.md) | Position sizing, R-multiples, stops, drawdown math |
| 05 | [Setups](05-setups.md) | Concrete beginner strategies with explicit rules |
| 06 | [Psychology & Process](06-psychology-and-process.md) | Tilt, journaling, review discipline |
| 07 | [Taxes & Record-Keeping](07-taxes-and-record-keeping.md) | Wash sales, trader tax status, Section 475(f) |
| 08 | [Red Flags](08-red-flags.md) | How to identify the people trying to profit from you |
| 09 | [What Nobody Tells Beginners](09-what-nobody-tells-beginners.md) | The practical lessons that don't fit a framework |

### Tools

| File | Purpose |
|---|---|
| [`tools/position_size.py`](tools/position_size.py) | Position sizing and R-multiple calculator |
| [`tools/expectancy.py`](tools/expectancy.py) | Expectancy, drawdown, and risk-of-ruin analysis on your own trade log |
| [`tools/trade_journal_template.csv`](tools/trade_journal_template.csv) | Trade journal schema, with a worked example row |

Both scripts are dependency-free Python 3 and run from the command line.

---

## The one-paragraph version

Day trading is a professional skill with a documented ~1% success rate, in which
the primary determinant of survival is not strategy selection but risk control.
Beginners lose because they size positions too large, hold losers too long, cut
winners too early, and trade far more often than their edge justifies — paying
spread and commission on every one of those unnecessary trades. If you proceed:
paper trade first, risk no more than a small fixed fraction of capital per trade,
journal every position, define your exit before you enter, and measure yourself
over hundreds of trades rather than dozens. Expect the first year to cost money.

---

## Sources

- Chague, F., De-Losso, R., & Giovannetti, B. (2020). *Day Trading for a Living?* — [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3423101)
- Barber, B., Lee, Y., Liu, Y., & Odean, T. (2014). *The Cross-Section of Speculator Skill: Evidence from Day Trading.* Journal of Financial Markets — [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=529063) · [full text](https://escholarship.org/uc/item/7k75v0qx)
- Barber, B., Lee, Y., Liu, Y., & Odean, T. *Do Day Traders Rationally Learn About Their Ability?* — [Berkeley](https://faculty.haas.berkeley.edu/odean/papers/Day%20Traders/Day%20Trading%20and%20Learning%20110217.pdf)
