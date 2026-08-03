# 02 — Market Mechanics

You cannot manage risk on an instrument whose plumbing you do not understand.
This chapter covers the machinery: how orders work, what the spread really is,
why liquidity determines your risk, and what actually happens during a trading
day.

---

## 1. The order book

At any moment, a stock has two prices, not one:

- **Bid** — the highest price a buyer is currently willing to pay.
- **Ask** (or offer) — the lowest price a seller is currently willing to accept.

```
        ASK (sellers)                 BID (buyers)
    $50.04   1,200 shares         $50.02   800 shares
    $50.03     500 shares         $50.01 2,400 shares
 →  $50.02     900 shares    →    $50.00 1,100 shares
```

The gap between the best bid and best ask is the **spread**. Here it is $0.01.

When you "buy at market," you are buying from the lowest asks, working upward
through the book until your order is filled. **If your order is larger than the
size available at the best ask, you consume that level and fill the remainder at
worse prices.** That is slippage, and it is a direct function of how much size
sits in the book relative to your order.

This is the mechanism behind a rule you will see repeated throughout this
curriculum: *liquidity is a risk parameter, not a convenience.* In a thin stock,
your stop loss does not protect you the way you think it does, because there may
be no one there to fill it near your price.

---

## 2. Order types

Getting these wrong is one of the most expensive beginner mistakes. Learn them
properly.

### Market order
Executes immediately at the best available price.

- **Guarantees**: execution.
- **Does not guarantee**: price.
- **Use when**: you must be out *now* — the position is going against you and
  exit certainty matters more than a few cents.
- **Danger**: in fast or thin markets, fills can be dramatically worse than the
  displayed quote. Never place a market order into a halted stock resuming
  trading, or in the seconds around a scheduled news release.

### Limit order
Executes only at your specified price or better.

- **Guarantees**: price.
- **Does not guarantee**: execution.
- **Use when**: entering a position. You are not obligated to trade; being picky
  about entry costs you nothing but a missed trade.
- **Danger**: you can be left unfilled while the move happens without you, or —
  worse — get filled only on the trades that go against you. (If price runs
  away from your buy limit, you miss the winner; if price collapses through it,
  you are filled. This adverse selection is real and is one reason limit entries
  are not free.)

### Stop order (stop-market)
Dormant until price touches your **stop price**, then becomes a market order.

- **Use when**: defining your maximum loss on a position.
- **Danger**: it becomes a *market* order. In a gap or a fast drop, you can fill
  far below your stop price. A stop is a trigger, not a guarantee of price.

### Stop-limit order
Triggers at the stop price, then places a *limit* order rather than a market
order.

- **Advantage**: no catastrophic slippage.
- **Critical danger**: **it may never fill.** If price gaps straight through your
  limit, you are still holding a position that is now much worse. Traders have
  turned a −1R into a −8R this way. For a protective stop on a directional day
  trade, a plain stop-market is usually the more honest instrument — you are
  choosing certain exit over uncertain price, which is the correct trade-off
  when the purpose of the order is survival.

### Bracket / OCO (one-cancels-other)
Attaches both a profit target and a stop loss to a position; filling one cancels
the other.

**Use these.** Placing your stop and target at the same moment you enter is the
single most effective mechanical defense against your own in-trade judgment.
Chapter 06 explains why your in-trade judgment is the thing you most need
defending from.

---

## 3. Liquidity and why it defines your universe

**Liquidity** is the ability to get in and out at a predictable price. It is
approximated by:

- **Average daily volume (ADV)** — shares traded per day.
- **Spread as a percentage of price** — a $0.01 spread on a $200 stock (0.005%)
  is trivial; a $0.05 spread on a $2 stock (2.5%) is punitive.
- **Depth** — size resting at each price level, not just the top of book.

### The beginner's liquidity filter

Trade only instruments with:

- Average daily volume **above ~1 million shares** (ideally well above),
- A spread of **one or two cents** on a stock priced above $20,
- No pending halt, and not a recent IPO with unstable behavior.

This rules out most of what gets promoted in trading chatrooms — sub-$5
small-caps, low-float runners, and thinly traded names. That is the point.
Those instruments are where beginners are systematically harvested, precisely
because wide spreads and thin depth make the cost of every mistake much larger.

---

## 4. The trading day (US equities)

Times are US Eastern.

| Session | Hours | Character |
|---|---|---|
| Pre-market | 4:00 – 9:30 am | Thin, wide spreads. News reprices here. Hazardous for beginners. |
| **The open** | 9:30 – 10:30 am | Highest volume and volatility of the day. Most day trading opportunity — and most day trading damage — occurs here. |
| Mid-morning | 10:30 – 11:30 am | Trends established at the open often continue or fail decisively. |
| **Lunch** | 11:30 am – 1:30 pm | Volume drains. Ranges tighten, false breakouts proliferate. Widely regarded as the worst period to trade. |
| Afternoon | 1:30 – 3:00 pm | Volume returns gradually. |
| **The close** | 3:00 – 4:00 pm | Volume spikes. Institutional rebalancing, MOC orders. Sharp, fast moves. |
| After-hours | 4:00 – 8:00 pm | Thin. Earnings released here. Wide spreads. |

Two practical implications:

1. **Most beginners should trade a narrow window** — roughly 9:45 to 11:00 am.
   The first fifteen minutes are the most violent and least forgiving; letting
   them pass costs you little and protects you from a lot. Trading all day is
   how you convert a small edge into a large commission bill.
2. **The lunch lull is where discipline dies.** Nothing is happening, you are
   bored, and boredom generates trades that your rules do not support. Close the
   platform.

---

## 5. Volatility, and sizing to it

Two stocks at $100 are not equally risky. One may move $0.50 on a typical day;
the other $5.00. Placing an identical stop distance on both is a category error.

**Average True Range (ATR)** measures typical movement over a period, capturing
gaps as well as intraday range. It is the standard tool for this.

The rule: **stop distance should be a function of the instrument's volatility,
not a fixed dollar or percentage figure you find comfortable.** A stop placed
inside the instrument's normal noise band will be hit by random fluctuation
regardless of whether your directional thesis was correct. You will then observe
the price move in your intended direction without you, conclude the market is
rigged, and widen your stops emotionally on the next trade. That sequence is
extremely common and entirely avoidable.

Practical starting point: place the stop beyond a structural level (below the
swing low for a long), and sanity-check that the distance is at least ~1× the
5-minute ATR. Then let position size adjust — which is exactly what chapter 04
covers.

---

## 6. Instruments: a brief comparison

| Instrument | Leverage | Notes for beginners |
|---|---|---|
| **Stocks** | Up to ~4:1 intraday on margin | Most intuitive. Best starting point. Wide instrument selection, transparent mechanics. |
| **ETFs** (SPY, QQQ) | Same as stocks | Extremely liquid, penny spreads, no single-company blowup risk. Excellent for learning. |
| **Futures** (ES, MES, NQ) | Very high (notional/margin often 20:1+) | 23-hour sessions, deep liquidity, favorable tax treatment (§1256). **Leverage is the danger** — micro contracts (MES, MNQ) exist specifically to make position sizing feasible for small accounts. |
| **Options** | High, non-linear | Adds time decay and volatility as independent variables. **Not a beginner instrument**, despite being marketed as one. You can be right on direction and still lose everything. |
| **Forex** | Very high (up to 50:1 US retail) | 24-hour, decentralized, quality of execution varies enormously by broker. Heavily targeted by scams. |
| **Crypto** | Varies; often extreme offshore | 24/7, no circuit breakers, uneven regulation and custody risk. |

**Recommendation for a beginner: liquid large-cap stocks or a major index ETF.**
Learn the craft where the mechanics are simplest and leverage cannot destroy you
faster than you can learn. Add complexity only after you have documented,
consistent results — and most people never need to.

---

## What to take from this chapter

1. Every trade crosses a spread; that cost is real and immediate.
2. Use limit orders to enter, stop-market orders to protect, and brackets to
   remove in-trade discretion.
3. Liquidity is a risk parameter. Restrict yourself to liquid instruments.
4. Trade a narrow window, and avoid the lunch lull.
5. Size stops to volatility (ATR), not to your comfort level.
6. Start with large-cap stocks or index ETFs.

Next: [03 — Getting Started](03-getting-started.md)
