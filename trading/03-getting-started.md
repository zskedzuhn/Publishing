# 03 — Getting Started

Accounts, current regulation, choosing a broker, and a structured 90-day on-ramp
that costs nothing.

---

## 1. Regulation: what changed in 2026

**If you have read older day trading material, this section corrects it.** The
rule most beginners have heard of no longer exists.

### The old regime (2001 – June 2026)

Under FINRA Rule 4210, a customer who executed four or more day trades within
five business days in a margin account (where day trades exceeded 6% of total
trades) was designated a **"pattern day trader"** and was required to maintain
**$25,000 in minimum equity**. Fall below it and day trading was restricted
until the account was funded back up.

This rule shaped retail day trading for a generation. It is why so much
literature is organized around "getting to $25k" and around using cash accounts
to sidestep the threshold.

### The current regime (effective June 4, 2026)

On April 14, 2026, the SEC approved FINRA's amendments to Rule 4210
(File No. SR-FINRA-2025-017). **The amendments eliminate both the "pattern day
trader" designation and the associated $25,000 minimum equity requirement.**
FINRA announced the changes in Regulatory Notice 26-10, effective **June 4,
2026**.

They are replaced by an **intraday margin framework**. Rather than gating access
by a fixed equity threshold and a trade count, firms must monitor a customer's
actual intraday exposure and margin deficiency, and buying power is determined by
real market exposure and maintenance margin requirements throughout the day.

### Four things that follow from this — read carefully

1. **The $2,000 minimum still applies.** FINRA Rule 4210(b)(4) requires $2,000
   minimum equity to trade on margin at all. That is a separate, pre-existing
   rule and it was not repealed.

2. **Your broker may not have implemented it yet.** FINRA granted an 18-month
   phase-in running through **October 20, 2027** for firms needing more time.
   Some brokers are on the new framework; others still enforce the old $25k
   rule. **Check your specific broker's current policy — do not assume.**

3. **Brokers may impose stricter requirements than FINRA does.** They routinely
   do. The regulatory floor is not your broker's floor.

4. **This changes the rules, not the odds.** The $25,000 requirement functioned,
   accidentally, as a barrier that kept some undercapitalized people out of a
   losing activity. Its removal lowers the barrier to entry; it does not improve
   anyone's expectancy. If anything, the correct response to an easier on-ramp
   is *more* self-imposed discipline, not less. The 97% figure from the Brazilian
   study was not caused by a margin rule.

### Cash accounts and settlement

In a cash account you trade only settled funds — no margin, no borrowing. US
equities settle **T+1** (one business day after the trade). So capital used
Monday is available again Tuesday. Cash accounts were historically the main
workaround for the PDT rule; with PDT eliminated they are less necessary, but
they remain a legitimate way to enforce hard discipline on yourself, since
without margin you simply cannot lose more than you deposited.

> **Regulatory note:** the above reflects rules as of mid-2026 and applies to
> US markets. Rules change and vary by jurisdiction. Verify current requirements
> with your broker and, for anything tax-related, a qualified professional.

---

## 2. Capital: how much, honestly

The regulatory minimum is no longer the binding constraint. The math is.

Work it backwards from position sizing. If you risk 1% per trade and your typical
stop distance implies you need, say, $200 of risk to trade a reasonable share
size in a liquid stock, you need a $20,000 account for that to be a 1% risk.

With a small account, you face a hard squeeze:

- Risk a sensible **1%** of a $2,000 account and you are risking $20 per trade.
  After spread and slippage, your edge is swamped by frictional cost.
- Risk a meaningful dollar amount and you are now risking **10–20%** per trade,
  where four ordinary consecutive losses do serious structural damage.

There is no clever way around this. **Undercapitalization is itself a primary
cause of failure**, because it forces oversized risk to generate meaningful
returns.

Realistic guidance:

| Capital | Assessment |
|---|---|
| Under $2,000 | Paper trade. Real trading here is dominated by costs. |
| $2,000 – $10,000 | Viable for learning with strict 1% risk and micro futures or low-priced liquid stocks. Do not expect income. |
| $10,000 – $30,000 | Enough for proper position sizing across most liquid instruments. Still not income. |
| $30,000+ | Sufficient capital for the strategy to be the binding constraint rather than the account size. |

**Non-negotiable:** trade only money whose complete loss would not change your
life. Not rent, not tuition, not borrowed money, not an emergency fund. This is
not a moral point — it is a practical one. Trading with money you need generates
exactly the fear-driven decisions (cutting winners early, holding losers,
oversizing to "make it back") that cause losses.

---

## 3. Choosing a broker

Evaluate on these axes, roughly in order:

1. **Regulatory status.** US: SEC-registered, FINRA member, SIPC insured. Verify
   the firm on [FINRA BrokerCheck](https://brokercheck.finra.org/). Elsewhere:
   confirm the local regulator (FCA, ASIC, etc.). **Never fund a broker you have
   not independently verified is registered.** This single check eliminates most
   outright fraud.
2. **Execution quality.** More important than headline commissions. Ask how
   orders are routed and whether direct market access is available. "Zero
   commission" brokers typically monetize via **payment for order flow** —
   routing your orders to market makers who pay for them. The cost is real, it
   simply appears as slightly worse fills rather than as a line item.
3. **Platform stability.** It will fail on the highest-volume day of the year.
   Have a backup: a second broker, or at minimum the broker's phone trading desk
   number saved in your phone before you need it.
4. **Total cost structure.** Commissions, data fees, platform fees, margin
   interest, inactivity fees.
5. **Current day-trading policy.** Given the phase-in above, ask directly
   whether the firm still enforces the old $25,000 requirement.

Avoid: unregulated offshore brokers, anything advertised via social media DMs,
firms promising guaranteed returns, and any platform where you cannot verify who
holds your money.

### A note on "prop firm" challenges

You will encounter firms offering funded accounts if you pass a paid evaluation.
Some are legitimate. Many are structured so the **evaluation fee is the business
model** — the pass rate is low by design, rules are strict enough that most
participants fail on a technicality, and the firm's revenue comes from repeat
entry fees rather than from trading profits. If you consider one, ask what
percentage of participants pass, whether payouts come from real market
positions, and read the rules on maximum drawdown extremely carefully. Treat any
firm that will not answer the first question as answered.

---

## 4. The 90-day on-ramp

Do not skip this. It costs nothing and it is the highest-value thing in this
curriculum.

### Days 1–30: Study and observe

- Work through this entire curriculum, including the risk chapter twice.
- Open a **paper trading account** (most major brokers provide one free).
- **Watch the open live, every day, without trading.** 9:30 to 11:00 am. Take
  notes on what you see. You are building pattern recognition and, more
  importantly, learning what your own impulses feel like when there is no money
  at stake.
- Pick **one instrument** and one timeframe. One. SPY on the 5-minute chart is a
  perfectly good choice and better than most alternatives.
- Write a first draft of your trading plan (template in chapter 06).

### Days 31–60: Paper trade the plan

- Execute **only** setups your written plan defines. No exceptions, no
  "obvious" trades that fall outside it.
- Journal every trade using `tools/trade_journal_template.csv`.
- Target **at least 50 trades** in this window.
- **Grade each trade A–F on process, independently of outcome.** A losing trade
  that followed your rules is an A. A winning trade that broke them is an F.
- End of period: run `tools/expectancy.py` on your log. Compute expectancy in R,
  win rate, average win/loss, and maximum drawdown.

### Days 61–90: Refine, then go small

- Analyze the data. Which setup has the best expectancy? What time of day are
  you profitable? Which mistakes recur?
- Cut what does not work. Most people find one setup carries their results and
  the rest are noise or negative.
- **If and only if** your paper expectancy is positive over 50+ trades *and*
  your process grades are consistently A/B, begin live trading at the **smallest
  size your broker permits** — one share, one micro contract.
- Expect your results to get worse. This is normal and universal: paper trading
  removes the emotional load, and real money reintroduces it. The gap between
  your paper and live results *is* the measure of your psychological work
  remaining.

### The honest checkpoint

If after 90 days your paper expectancy is negative, the correct conclusion is not
"trade live to make it real." It is either *keep refining on paper* or *stop*.
Both are respectable. Stopping at this stage costs you three months and no money,
which makes it one of the best outcomes available.

---

## 5. Your daily routine

**Pre-market (30 min):**
- Check the economic calendar — FOMC, CPI, NFP, and earnings for anything you
  trade. Know when scheduled volatility is coming.
- Review overnight action and set your watchlist. Keep it to 2–5 names.
- Mark key levels: prior day high/low/close, pre-market high/low.
- Write down your maximum loss for the day and commit to it.

**During the session:**
- Trade only your defined setups.
- Log entries and exits as they happen, not from memory afterward.
- **Hard stop at your daily loss limit.** No exceptions, no recovery attempts.
  Chapter 06 explains why this rule is the one that saves accounts.

**Post-market (20 min):**
- Complete journal entries with screenshots.
- Grade each trade on process.
- Note one specific thing to do differently tomorrow.

**Weekly:**
- Review all trades in aggregate. Update statistics. Adjust the plan
  deliberately — not reactively after a bad day.

---

## What to take from this chapter

1. The $25,000 PDT minimum was eliminated effective June 4, 2026, but the $2,000
   margin minimum remains and your broker may still enforce the old rule during
   the phase-in through October 2027.
2. Easier access does not improve your odds. Impose your own discipline.
3. Undercapitalization causes failure by forcing oversized risk.
4. Verify any broker on BrokerCheck before funding it.
5. Do the full 90-day on-ramp. It is free and it is the best filter you have.

Next: [04 — Risk Management](04-risk-management.md)
