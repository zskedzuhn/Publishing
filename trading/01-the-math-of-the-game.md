# 01 — The Math of the Game

Most trading education starts with chart patterns. That is backwards. Chart
patterns are the least durable part of trading. The math below is the part that
does not change, and it is the part that determines whether you survive.

---

## 1. Expectancy is the only number that matters

A strategy's **expectancy** is the average amount you expect to win or lose per
trade, over many trades:

```
Expectancy = (Win rate × Average win) − (Loss rate × Average loss)
```

Work an example. You win 40% of trades. Winners average $300, losers average
$150.

```
Expectancy = (0.40 × $300) − (0.60 × $150)
           = $120 − $90
           = +$30 per trade
```

Positive. This strategy makes money over time despite **losing 60% of its
trades.**

Now the mirror image. You win 70% of trades — a win rate that feels great and
that most beginners chase — but winners average $100 and losers average $300:

```
Expectancy = (0.70 × $100) − (0.30 × $300)
           = $70 − $90
           = −$20 per trade
```

Negative. You are right most of the time and you go broke anyway.

**This is the single most important idea in this document.** Win rate, by itself,
carries almost no information. The ratio between your average win and your
average loss carries most of it. A beginner who understands this will
outperform one who has memorized forty chart patterns but chases a high hit rate.

The reason this matters practically: nearly every destructive beginner habit is
an attempt to raise win rate at the expense of expectancy. Moving a stop loss
"just a little" so the trade can recover, taking profit early because green feels
good, averaging down into a loser — every one of these raises your win rate and
lowers your expectancy. They feel like discipline. They are the opposite.

---

## 2. R-multiples: the unit that makes trades comparable

Stop thinking in dollars. Think in **R**, where 1R is the amount you risk on a
trade.

If you buy at $50.00 with a stop at $49.50, your risk per share is $0.50. That is
1R. Every outcome is then expressed as a multiple of it:

| Exit price | P&L per share | R-multiple |
|---|---|---|
| $49.50 (stopped out) | −$0.50 | −1.0R |
| $50.75 | +$0.75 | +1.5R |
| $51.50 | +$1.50 | +3.0R |
| $49.75 (manual cut) | −$0.25 | −0.5R |

This is not notation for its own sake. It does three things:

1. **It makes trades comparable across position sizes and instruments.** A +2R on
   a 100-share trade and a +2R on a 1,000-share trade are the same quality
   decision, judged correctly.
2. **It removes dollar emotion from review.** "I lost $840" triggers something
   different than "I took a −1R." The second is what you should be recording.
3. **It converts expectancy into something portable.** Expressed in R, the first
   example above is +0.20R per trade. That figure tells you what your system is
   worth regardless of account size.

Adopt this vocabulary now. Every chapter after this uses it.

---

## 3. Transaction costs: the tax you pay on activity

Every trade costs you money before the market moves at all. Three components:

**The spread.** The gap between the bid (what buyers offer) and the ask (what
sellers demand). Buy at the ask, sell at the bid, and you have paid the spread.
On a liquid large-cap stock this might be $0.01. On a thin small-cap it can be
$0.10 or worse — and on that thin stock, a $0.10 spread against a $0.50 risk
is **20% of your risk budget gone at the moment of entry.**

**Commissions.** Many US brokers advertise $0 stock commissions. Futures,
options, and most non-US markets still charge per contract. "Zero commission"
does not mean zero cost — see payment for order flow below.

**Slippage.** The difference between the price you expected and the price you
got. Market orders in fast-moving conditions routinely fill worse than the quote
you saw. This is the cost beginners consistently forget to model, and it is
largest precisely when you most want to trade: news events, opening minutes,
breakouts.

### Why this compounds into ruin

Suppose your round-trip cost is $0.02 per share and your average winning trade
captures $0.30 per share.

- Trade 100 times: costs are $2.00 per share of cumulative drag.
- Trade 1,000 times: costs are $20.00 per share.

Against a strategy with a genuine but small edge, **overtrading alone converts a
winning system into a losing one.** This is a large part of why the Taiwan study
found day traders losing 23.9 bps per day *net of fees* — the gross performance
was far less catastrophic than the net.

The practical rule that follows: **the frequency of your trading must be
justified by the size of your edge.** More trades is not more opportunity. More
trades is more cost, and cost is certain while edge is probabilistic.

---

## 4. The asymmetry of losses

Losses hurt more than equivalent-percentage gains help. This is arithmetic, not
psychology:

| Drawdown | Gain required to recover |
|---|---|
| −10% | +11.1% |
| −20% | +25% |
| −33.3% | +50% |
| −50% | +100% |
| −75% | +300% |
| −90% | +900% |

A 50% loss requires a 100% gain to get back to even. This is why capital
preservation dominates return-seeking for a beginner, and why the risk chapter
is the most important one in this curriculum.

The corollary is uncomfortable but worth internalizing: **your first job is not
to make money. It is to still be in the game in twelve months.** Traders who
survive long enough to find an edge can compound it. Traders who blow up in month
three never get to find out whether they had one.

---

## 5. Variance, and why 30 trades tell you nothing

Consider a genuinely profitable strategy: 45% win rate, winners average 2R,
losers average 1R. Expectancy is `(0.45 × 2) − (0.55 × 1) = +0.35R` per trade.
A good system.

Now ask what a 20-trade sample looks like. With a 55% chance of losing on any
given trade, strings of consecutive losses are ordinary:

- Six losses in a row: roughly 2.8% likely on any given sequence of six — which
  means over a few hundred trades, near-certain to happen repeatedly.
- Ten losses in a row: rare per-sequence, but not remotely impossible over a
  career.

**A profitable system will regularly produce losing weeks and losing months.**
This creates the central epistemological problem of trading: you cannot tell a
bad system from a good system in a drawdown by looking at the P&L. Both look
identical over short horizons.

Two consequences:

1. **Do not judge a strategy on fewer than ~100 trades**, and prefer several
   hundred. Below that, you are reading noise.
2. **Judge process, not outcome, in the short run.** A trade that followed your
   rules and lost is a *good trade*. A trade that broke your rules and won is a
   *bad trade* — it was rewarded by chance, and the reward will teach you a habit
   that costs you later. This distinction is genuinely hard to hold onto, and it
   is what the journal in chapter 06 exists to enforce.

---

## 6. Risk of ruin

Even a positive-expectancy system can bankrupt you if you bet too large. This is
the "gambler's ruin" problem, and it is why position sizing is not a detail.

The intuition: if you risk 25% of your account per trade, four consecutive
losses — an entirely ordinary event, as shown above — takes you to roughly 32% of
starting capital, requiring a 216% gain to recover. At 2% risk per trade, those
same four losses cost you about 8%, and you continue trading normally.

**The same strategy, at different position sizes, is either a business or a
lottery ticket.** Nothing about the edge changed. Only the sizing did.

`tools/expectancy.py` in this repo will compute expectancy, maximum drawdown,
and a Monte Carlo risk-of-ruin estimate from your own trade log. Run it against
your paper trading results before you risk real money.

---

## What to take from this chapter

1. Expectancy, not win rate, determines profitability.
2. Measure everything in R, not dollars.
3. Costs are certain and scale with activity; edge is probabilistic. Trade less
   than you want to.
4. Drawdowns are mathematically asymmetric — protect capital first.
5. Short-run results are noise. Judge process over outcome, and demand a large
   sample before concluding anything.
6. Position sizing converts a good strategy into a surviving one.

Next: [02 — Market Mechanics](02-market-mechanics.md)
