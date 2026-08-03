# 05 — Setups

The least important chapter, placed fifth deliberately.

Setups are the part beginners want first and the part that matters least. A
mediocre setup with excellent risk management survives. An excellent setup with
poor risk management does not. If you arrived here by skipping chapters 01 and
04, go back.

**These are teaching examples, not recommendations.** They are widely published,
which means any edge in them is thin and contested. Their purpose is to give you
something concrete and rule-based to practice on paper — the structure of a
tradeable rule set matters more here than the specific rules.

---

## What makes a setup tradeable

Before any specific pattern, understand the requirements. A tradeable setup must
specify, in writing, *before* you enter:

1. **Context** — what market conditions must hold for this to apply.
2. **Trigger** — the precise, objective event that puts you in.
3. **Stop** — where the idea is proven wrong.
4. **Target** — where you take profit, and why there.
5. **Invalidation** — conditions under which you skip the trade entirely.

If you cannot write all five in a sentence each, you do not have a setup. You
have a feeling with a chart attached.

A useful test: could a stranger read your rules and take the same trade you
would? If not, the rules are underspecified, and the gaps will be filled by your
mood.

---

## Setup 1: Opening Range Breakout (ORB)

The most common beginner setup. Straightforward to define, which is its main
virtue.

**Concept.** The first 15–30 minutes of trading establish a range. A decisive
break of that range with volume sometimes signals the direction for the next
period.

**Rules:**

| Element | Definition |
|---|---|
| Context | Liquid large-cap or index ETF. Ideally a catalyst (earnings, news, gap). |
| Setup | Mark the high and low of the first 15 minutes (9:30–9:45). |
| Trigger | Price closes above the 15-min high (long) on a 5-min bar, with volume above the session average. |
| Stop | Below the midpoint of the opening range, or below the breakout bar's low. |
| Target | 2R minimum. Consider scaling: half at 2R, trail the remainder. |
| Invalidation | No volume expansion; range is unusually wide; the day is a scheduled news day and the release has not yet occurred. |

**Why it fails.** False breakouts are extremely common — price pokes above the
range, triggers everyone's buy stops, and reverses immediately. That is not bad
luck; it is a known behavior, since resting stop orders above an obvious level
are exactly the liquidity a larger seller wants to trade against. Requiring a
*close* beyond the level rather than a touch filters some of this, at the cost of
worse entry prices. There is no version of this that removes the trade-off.

---

## Setup 2: VWAP Reversion

**VWAP** (Volume-Weighted Average Price) is the average price weighted by volume
since the open. It is genuinely important because many institutions benchmark
execution against it, which gives it real behavioral significance rather than
merely charted significance.

**Concept.** In a range-bound market, price extended far from VWAP tends to
revert toward it.

**Rules:**

| Element | Definition |
|---|---|
| Context | Range-bound day — no strong trend, price oscillating around VWAP. |
| Setup | Price extends ≥2× ATR from VWAP. |
| Trigger | A reversal candle (rejection wick, engulfing bar) at the extension. |
| Stop | Beyond the extreme of the extension. |
| Target | VWAP itself. |
| Invalidation | **Any strongly trending day.** |

**Why it fails.** This setup fights the trend by construction. On a strong trend
day it produces a sequence of losses as price extends further and further from
VWAP without reverting. The invalidation rule is doing nearly all the work here,
and it is also the hardest rule to apply honestly, because "is this a trending
day?" is a judgment call you will make while already wanting to take the trade.

---

## Setup 3: Pullback in Trend

Generally the most robust of the three, because it aligns with rather than
against the dominant force.

**Concept.** In an established trend, enter on a retracement rather than chasing
extension.

**Rules:**

| Element | Definition |
|---|---|
| Context | Clear trend — higher highs and higher lows; price above a rising moving average (9 or 20 EMA). |
| Setup | Price pulls back to the moving average or a prior support level on declining volume. |
| Trigger | A reversal bar in the direction of the trend at that level. |
| Stop | Below the pullback low. |
| Target | Prior swing high, then trail. |
| Invalidation | Pullback exceeds 50% of the prior leg; volume expands on the pullback (suggesting real selling rather than a pause). |

**Why it fails.** Trends end, and the final pullback in a trend looks exactly
like every profitable pullback that preceded it. There is no way to distinguish
them in advance — which is precisely why the stop and the position size matter
more than the pattern recognition.

---

## The uncomfortable truth about setups

Notice that every setup above has a "why it fails" section, and that in each case
the failure mode is structural rather than fixable. That is not pessimism; it is
the actual nature of the thing.

**No setup works most of the time.** A 40–50% win rate is normal and can be very
profitable (see chapter 01). Your edge does not come from being right often. It
comes from:

- **Selectivity** — taking only high-quality instances rather than every
  instance that roughly resembles the pattern.
- **Execution** — entering and exiting at planned prices rather than emotional
  ones.
- **Risk management** — losers cost 1R, winners run past 2R.
- **Consistency** — trading the same way across hundreds of repetitions so that
  expectancy has room to express itself.

This is why chapter 04 outranks this one. Given a positive-expectancy setup, risk
management determines your outcome. Given negative expectancy, no amount of
pattern study saves you.

---

## Indicators: a warning

You will be shown hundreds. RSI, MACD, Bollinger Bands, stochastics, Ichimoku,
and every proprietary variant someone is selling.

Three points worth holding onto:

1. **All indicators are derived from price and volume.** They are transformations
   of data you already have. None contains hidden information.
2. **All are lagging** — computed from past bars, by construction.
3. **More indicators produce worse decisions**, not better ones. A chart with
   eight indicators will always show something suggesting a trade in either
   direction, which means it provides no filtering at all — you will simply see
   whichever signal matches what you already wanted to do.

Start with bare price, volume, VWAP, and one moving average. Add an indicator
only when you can articulate the specific decision it improves and can show that
improvement in your journal data. Most traders end up with fewer indicators over
time, not more.

---

## Building your own

The strongest approach is not adopting someone else's setup but developing one
from observation:

1. **Observe** — watch one instrument daily for weeks. Note recurring behavior.
2. **Hypothesize** — form a specific, falsifiable claim. "When X occurs, price
   tends to do Y within Z bars."
3. **Define** — write the five elements above, precisely enough for a stranger.
4. **Test** — paper trade at least 50 instances. Log every one.
5. **Measure** — compute expectancy with `tools/expectancy.py`.
6. **Refine or discard** — most hypotheses fail. That is the process working.
   Discarding a hypothesis on 50 paper trades is a success, not a wasted month.

A setup you developed and tested yourself, and whose failure modes you have
personally observed, will be traded with a conviction that no purchased setup can
give you — which matters enormously at the moment a position goes against you.

---

## What to take from this chapter

1. A setup is not tradeable until context, trigger, stop, target, and
   invalidation are written down.
2. All three examples fail in structural ways. That is normal.
3. Edge comes from selectivity, execution, and risk control — not from the
   pattern.
4. Indicators are derived, lagging, and subject to diminishing returns.
5. Setups you build and test yourself beat setups you adopt.

Next: [06 — Psychology & Process](06-psychology-and-process.md)
