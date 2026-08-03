# 04 — Risk Management

This is the most important chapter in this curriculum.

Strategies are commodities — thousands are published free, and many of them
work. Risk management is what separates the people using them profitably from
the people who used the same strategy and blew up. If you internalize only one
chapter, make it this one.

---

## 1. The 1% rule

**Risk no more than 1% of account equity on any single trade.**

For a $25,000 account, that is $250 of risk per trade — not a $250 position, but
a position whose loss *if your stop is hit* is $250.

Why 1%? Run the survival math on a 10-loss streak, which any trader will
experience:

| Risk per trade | After 10 consecutive losses | Gain needed to recover |
|---|---|---|
| 1% | −9.6% | +10.6% |
| 2% | −18.3% | +22.4% |
| 5% | −40.1% | +67.0% |
| 10% | −65.1% | +186.8% |
| 20% | −89.3% | +831.3% |

At 1% you have an ordinary bad stretch and continue trading. At 10% you are
functionally finished — a 186% recovery is not happening, and the psychological
state that produces is not one in which anybody trades well.

Beginners should risk **0.5%** while learning. You are paying for education; keep
tuition low. Nobody has ever regretted sizing too small during their first
hundred trades.

---

## 2. Position sizing: the formula

Position size is an *output*, never an input. You do not decide how many shares
to buy. You decide where your stop goes, and the size falls out of arithmetic.

```
Position size = (Account × Risk %) ÷ (Entry price − Stop price)
```

**Worked example.**

- Account: $30,000
- Risk per trade: 1% → $300
- Entry: $50.00
- Stop: $48.50 → risk per share $1.50

```
Position size = $300 ÷ $1.50 = 200 shares
```

You buy 200 shares ($10,000 notional). If stopped out, you lose $300 — exactly
1R.

Now the crucial part. Same account, tighter stop at $49.50 (risk $0.50/share):

```
Position size = $300 ÷ $0.50 = 600 shares
```

600 shares, $30,000 notional — your entire account, and more if using margin.
**Yet the risk is identical: $300.**

This is the insight most beginners miss. A tighter stop does not mean less risk;
it means *more shares at the same risk.* Risk is governed by the distance to your
stop multiplied by size, never by size alone. Two traders holding wildly
different share counts can be running identical risk, and a trader who "only
bought 100 shares" can be risking far more than one who bought 1,000.

Use `tools/position_size.py` in this repo to compute this. Do it before every
trade until it is automatic.

---

## 3. Where the stop actually goes

The order of operations matters, and beginners routinely reverse it:

> **Wrong:** decide size → place stop wherever keeps the dollar loss comfortable.
>
> **Right:** find where the thesis is invalidated → place stop there → derive
> size.

Your stop belongs at **the price that proves you were wrong**, not at the price
where the loss starts to hurt. Those are unrelated quantities, and conflating
them is why so many stops sit just inside the noise band, guaranteeing they get
hit by random fluctuation.

Practical placement:

- **Structure-based** — below the swing low (long) or above the swing high
  (short), plus a small buffer to avoid the obvious cluster where everyone else's
  stops sit.
- **Volatility-based** — a multiple of ATR, typically 1× to 2×, which scales
  automatically with conditions.
- **Time-based** — exit if the trade has not worked within N bars. Underused and
  genuinely valuable: a thesis that has not played out is a thesis that is
  failing, even if it has not hit your price stop.

If the correct structural stop implies a position size too small to be worth
trading, **that is information: skip the trade.** It is not an invitation to
tighten the stop.

### The rule that matters more than its placement

**Never move a stop away from your entry.** Not once, not "just this time," not
because you are confident. Moving a stop wider converts a defined −1R into an
undefined loss, and it is the proximate cause of a large share of blown accounts.

Moving a stop *toward* your entry — to lock in profit as a trade works — is
fine and often correct. The asymmetry is the entire point.

---

## 4. Daily and weekly limits

Position-level risk is not enough. You also need circuit breakers, because the
worst damage comes from sequences, not single trades.

| Limit | Suggested level | Action on breach |
|---|---|---|
| Daily loss limit | 3R (or 2–3% of account) | Stop trading. Close the platform for the day. |
| Daily trade limit | 3–5 trades | Stop. Prevents overtrading and revenge cycles. |
| Weekly loss limit | 6R (or 5–6%) | Stop for the week. Review before resuming. |
| Monthly loss limit | 10% | Stop. Full strategy review before returning. |

**The daily loss limit is the single most valuable rule you will adopt.**

The mechanism it defends against is specific and predictable. You take two
losses. You feel the urge to make it back *today*. You take a larger position
than your rules allow, on a setup that is not quite your setup, because you need
this one to work. That trade loses too. Now you are down five times your normal
daily loss, and you are making decisions in a state that has nothing to do with
market analysis.

This sequence is called **revenge trading**, it is close to universal, and it
destroys more accounts than any strategy flaw. The daily loss limit is a
mechanical brake that works precisely because it does not require you to be
rational at the moment it triggers — the decision was already made when you were
calm.

Set it in advance. Write it down. Treat breaching it as a serious rule violation
regardless of what happens afterward.

---

## 5. Correlation: the hidden concentration

You hold three positions, each risked at 1%. You believe you are risking 3%.

If those positions are AAPL, MSFT, and NVDA, you are not. Large-cap tech names
move together, especially on macro news. A rate surprise takes all three down
simultaneously. Your effective risk is much closer to a single 3% position — and
the diversification you thought you had was an illusion.

Rules:

- Treat highly correlated positions as **one position** for sizing purposes.
- Cap total open risk at **2–3%** across all positions.
- Be aware that in genuine market stress, correlations across nearly everything
  converge toward 1. The diversification you have is weakest exactly when you
  need it most.

---

## 6. Leverage

Margin lets you control more than you have. Under the intraday margin framework
that replaced the PDT rule (chapter 03), available buying power is determined by
your actual exposure and maintenance requirements rather than a fixed threshold —
but the underlying arithmetic is unchanged.

**Leverage multiplies outcomes; it does not create edge.** A negative-expectancy
strategy with leverage loses money faster. That is the whole effect.

Beginners should use **no leverage at all.** Once your position sizing is
correct, leverage becomes largely irrelevant anyway — because your risk is capped
by your stop distance and 1% rule, not by your buying power. If you find yourself
*needing* leverage to make trades meaningful, the real problem is
undercapitalization, and leverage is the worst available solution to it.

A margin call, for the record, means your broker liquidates your positions at
their discretion, at whatever prices are available, usually at the worst possible
moment. You do not choose what gets sold.

---

## 7. Risk of ruin

Even a positive-expectancy system will bankrupt you if sized wrong. Risk of ruin
depends on three inputs: win rate, payoff ratio, and **risk per trade** — and the
third is the only one you control directly and immediately.

Illustrative figures for a system with a 50% win rate and 1:1 payoff (roughly
break-even before costs):

| Risk per trade | Approximate risk of ruin |
|---|---|
| 1% | Very low |
| 2% | Low |
| 5% | Substantial |
| 10% | Near certain over enough trades |

The pattern generalizes: **risk per trade is the dominant term.** You can improve
your strategy for years; halving your position size improves survival odds
immediately and with certainty.

`tools/expectancy.py` runs a Monte Carlo simulation of this against your own
trade log. Run it on your paper results before going live.

---

## 8. The risk checklist

Before every single trade:

- [ ] Is this one of my defined setups? (If no — no trade.)
- [ ] Where is my stop, and what invalidates the thesis?
- [ ] What is my position size from the formula?
- [ ] Is my risk ≤ 1% of account?
- [ ] Where is my profit target? Is the reward at least 2× the risk?
- [ ] Am I under my daily loss limit and daily trade limit?
- [ ] Does this correlate with positions I already hold?
- [ ] Am I calm? (If no — no trade.)

Eight questions, under a minute. Print it. Keep it visible. The trades you skip
because of this list will, over a career, be worth more than the trades you take.

---

## What to take from this chapter

1. Risk ≤1% per trade (0.5% while learning). Survival is the first objective.
2. Position size is derived from stop distance — it is never chosen directly.
3. Stops go where the thesis breaks, never where the pain starts. Never widen one.
4. A daily loss limit is your primary defense against revenge trading.
5. Correlated positions are one position.
6. Leverage multiplies results without creating edge. Avoid it.
7. Risk per trade dominates risk of ruin — and it is entirely under your control.

Next: [05 — Setups](05-setups.md)
