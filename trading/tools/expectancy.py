#!/usr/bin/env python3
"""Trade log analyzer: expectancy, drawdown, and risk of ruin.

Reads a CSV trade journal (see trade_journal_template.csv) and reports the
statistics that actually determine whether a system is viable. Run this on
your paper trading results BEFORE risking real money.

Usage:
    python3 expectancy.py trade_journal_template.csv
    python3 expectancy.py my_trades.csv --risk 1.0 --simulations 20000

Required column:
    r_multiple    outcome of each trade in R (e.g. 2.0, -1.0, -0.44)

Optional columns, used if present:
    setup           per-setup breakdown
    followed_plan   yes/no — splits results by rule adherence
    process_grade   A-F  — process grade distribution
    mistake         recurring mistake tally
    pnl             currency P&L totals

Dependency-free: standard library only.
"""

import argparse
import csv
import random
import sys
from collections import Counter, defaultdict


# ---------------------------------------------------------------- loading

def load_trades(path):
    """Read the CSV and return (trades, skipped_row_count)."""
    try:
        with open(path, newline="", encoding="utf-8-sig") as f:
            rows = list(csv.DictReader(f))
    except FileNotFoundError:
        raise SystemExit(f"Error: file not found: {path}")

    if not rows:
        raise SystemExit("Error: file contains no data rows.")
    if "r_multiple" not in rows[0]:
        raise SystemExit(
            "Error: CSV must contain an 'r_multiple' column.\n"
            "See trade_journal_template.csv for the expected schema."
        )

    trades, skipped = [], 0
    for row in rows:
        raw = (row.get("r_multiple") or "").strip()
        if not raw:
            skipped += 1
            continue
        try:
            r = float(raw)
        except ValueError:
            skipped += 1
            continue

        pnl = None
        raw_pnl = (row.get("pnl") or "").strip()
        if raw_pnl:
            try:
                pnl = float(raw_pnl.replace("$", "").replace(",", ""))
            except ValueError:
                pnl = None

        trades.append({
            "r": r,
            "pnl": pnl,
            "setup": (row.get("setup") or "").strip() or "(unlabeled)",
            "followed": (row.get("followed_plan") or "").strip().lower(),
            "grade": (row.get("process_grade") or "").strip().upper(),
            "mistake": (row.get("mistake") or "").strip().lower(),
        })

    if not trades:
        raise SystemExit("Error: no rows contained a usable r_multiple value.")
    return trades, skipped


# ---------------------------------------------------------------- stats

def basic_stats(rs):
    wins = [r for r in rs if r > 0]
    losses = [r for r in rs if r < 0]
    scratches = [r for r in rs if r == 0]
    n = len(rs)

    avg_win = sum(wins) / len(wins) if wins else 0.0
    avg_loss = sum(losses) / len(losses) if losses else 0.0
    gross_win = sum(wins)
    gross_loss = abs(sum(losses))

    return {
        "n": n,
        "wins": len(wins),
        "losses": len(losses),
        "scratches": len(scratches),
        "win_rate": len(wins) / n * 100.0,
        "expectancy": sum(rs) / n,
        "total_r": sum(rs),
        "avg_win": avg_win,
        "avg_loss": avg_loss,
        "largest_win": max(rs),
        "largest_loss": min(rs),
        "payoff": (avg_win / abs(avg_loss)) if avg_loss else float("inf"),
        "profit_factor": (gross_win / gross_loss) if gross_loss else float("inf"),
    }


def drawdown_and_streaks(rs):
    """Max peak-to-trough drawdown in R, plus longest win/loss streaks."""
    equity = peak = 0.0
    max_dd = 0.0
    win_streak = loss_streak = cur_w = cur_l = 0

    for r in rs:
        equity += r
        peak = max(peak, equity)
        max_dd = max(max_dd, peak - equity)

        if r > 0:
            cur_w += 1
            cur_l = 0
        elif r < 0:
            cur_l += 1
            cur_w = 0
        else:
            cur_w = cur_l = 0
        win_streak = max(win_streak, cur_w)
        loss_streak = max(loss_streak, cur_l)

    return {
        "max_drawdown_r": max_dd,
        "longest_win_streak": win_streak,
        "longest_loss_streak": loss_streak,
        "final_equity_r": equity,
    }


def monte_carlo_ruin(rs, risk_pct, n_trades, sims, ruin_threshold=0.5, seed=42):
    """Bootstrap-resample the trade distribution to estimate ruin probability.

    Each trade compounds against current equity, so a losing streak shrinks
    subsequent bet sizes the way real fractional-risk sizing does. 'Ruin' is
    a drawdown past ruin_threshold of starting equity.
    """
    rng = random.Random(seed)
    risk = risk_pct / 100.0
    ruined = 0
    finals, drawdowns = [], []

    for _ in range(sims):
        equity = 1.0
        peak = 1.0
        hit_ruin = False
        for _ in range(n_trades):
            equity *= (1.0 + rng.choice(rs) * risk)
            if equity <= 0:
                equity = 0.0
                hit_ruin = True
                break
            peak = max(peak, equity)
            if equity <= ruin_threshold:
                hit_ruin = True
                break
        if hit_ruin:
            ruined += 1
        finals.append(equity)
        drawdowns.append((peak - equity) / peak if peak > 0 else 1.0)

    finals.sort()

    def pct(p):
        idx = min(int(p * len(finals)), len(finals) - 1)
        return finals[idx]

    return {
        "ruin_pct": ruined / sims * 100.0,
        "median_final": pct(0.50),
        "p05_final": pct(0.05),
        "p95_final": pct(0.95),
        "mean_max_dd": sum(drawdowns) / len(drawdowns) * 100.0,
    }


# ---------------------------------------------------------------- output

def bar(value, width=28, scale=1.0):
    filled = max(0, min(width, int(abs(value) / scale * width)))
    return "#" * filled


def report(trades, args):
    rs = [t["r"] for t in trades]
    s = basic_stats(rs)
    d = drawdown_and_streaks(rs)

    out = []
    w = 60
    out.append("\n" + "=" * w)
    out.append("  TRADE LOG ANALYSIS")
    out.append("=" * w)

    # --- sample adequacy, stated first because it gates everything else
    n = s["n"]
    if n < 30:
        verdict = "NOT INTERPRETABLE — this is noise, not a result."
    elif n < 100:
        verdict = "PRELIMINARY — treat as directional only."
    elif n < 300:
        verdict = "REASONABLE — conclusions are becoming meaningful."
    else:
        verdict = "GOOD sample size."
    out.append(f"\n  Sample: {n} trades — {verdict}")
    if n < 100:
        out.append("  Chapter 01: do not judge a strategy on fewer than ~100 trades.")

    # --- core
    out.append("\n" + "-" * w)
    out.append("  CORE STATISTICS")
    out.append("-" * w)
    out.append(f"  Expectancy         {s['expectancy']:>10.3f} R per trade")
    out.append(f"  Total              {s['total_r']:>10.2f} R")
    out.append(f"  Win rate           {s['win_rate']:>10.1f} %   "
               f"({s['wins']}W / {s['losses']}L / {s['scratches']}S)")
    out.append(f"  Average win        {s['avg_win']:>10.2f} R")
    out.append(f"  Average loss       {s['avg_loss']:>10.2f} R")
    pf = s["profit_factor"]
    po = s["payoff"]
    out.append(f"  Payoff ratio       {po:>10.2f}"
               if po != float("inf") else "  Payoff ratio          no losses")
    out.append(f"  Profit factor      {pf:>10.2f}"
               if pf != float("inf") else "  Profit factor         no losses")
    out.append(f"  Largest win        {s['largest_win']:>10.2f} R")
    out.append(f"  Largest loss       {s['largest_loss']:>10.2f} R")

    pnls = [t["pnl"] for t in trades if t["pnl"] is not None]
    if pnls:
        out.append(f"  Net P&L            {sum(pnls):>10,.2f}  "
                   f"({len(pnls)} of {n} trades priced)")

    # --- risk
    out.append("\n" + "-" * w)
    out.append("  RISK")
    out.append("-" * w)
    out.append(f"  Max drawdown       {d['max_drawdown_r']:>10.2f} R")
    out.append(f"  Longest loss run   {d['longest_loss_streak']:>10d} trades")
    out.append(f"  Longest win run    {d['longest_win_streak']:>10d} trades")

    # --- verdict on expectancy
    e = s["expectancy"]
    out.append("\n" + "-" * w)
    if e > 0:
        out.append(f"  POSITIVE EXPECTANCY: +{e:.3f}R per trade.")
        out.append(f"  Over 100 trades this system returns about {e * 100:.1f}R.")
        if n < 100:
            out.append("  BUT the sample is too small to trust. Keep going.")
    else:
        out.append(f"  NEGATIVE EXPECTANCY: {e:.3f}R per trade.")
        out.append("  This system loses money at any position size.")
        out.append("  Sizing up will not fix it. Revise or discard the strategy.")
    out.append("-" * w)

    # --- per setup
    by_setup = defaultdict(list)
    for t in trades:
        by_setup[t["setup"]].append(t["r"])
    if len(by_setup) > 1:
        out.append("\n" + "-" * w)
        out.append("  BY SETUP")
        out.append("-" * w)
        out.append(f"  {'Setup':<18}{'N':>5}{'Win%':>8}{'Exp(R)':>10}{'Total':>10}")
        for name, vals in sorted(by_setup.items(),
                                 key=lambda kv: -sum(kv[1]) / len(kv[1])):
            ss = basic_stats(vals)
            out.append(f"  {name[:17]:<18}{ss['n']:>5}{ss['win_rate']:>8.1f}"
                       f"{ss['expectancy']:>10.3f}{ss['total_r']:>10.2f}")
        out.append("\n  Cut the negative-expectancy setups. Most traders find one")
        out.append("  setup carries their results and the rest are noise.")

    # --- discipline
    followed = [t["r"] for t in trades if t["followed"] in ("yes", "y", "true", "1")]
    broke = [t["r"] for t in trades if t["followed"] in ("no", "n", "false", "0")]
    if followed and broke:
        fs, bs = basic_stats(followed), basic_stats(broke)
        out.append("\n" + "-" * w)
        out.append("  DISCIPLINE")
        out.append("-" * w)
        out.append(f"  Followed plan   {fs['n']:>4} trades   "
                   f"exp {fs['expectancy']:>7.3f}R   total {fs['total_r']:>8.2f}R")
        out.append(f"  Broke plan      {bs['n']:>4} trades   "
                   f"exp {bs['expectancy']:>7.3f}R   total {bs['total_r']:>8.2f}R")
        adherence = len(followed) / (len(followed) + len(broke)) * 100.0
        out.append(f"  Adherence rate  {adherence:.1f}%")
        cost = fs["expectancy"] - bs["expectancy"]
        if cost > 0:
            out.append(f"\n  Breaking your plan costs {cost:.3f}R per trade.")
            out.append(f"  Across {bs['n']} such trades: {cost * bs['n']:.2f}R left on the table.")
        else:
            out.append("\n  Rule-breaking has outperformed here. Two possibilities:")
            out.append("  the sample is too small (most likely), or your written")
            out.append("  rules genuinely need revision. Do not conclude the")
            out.append("  latter without a large sample — see chapter 06 on why")
            out.append("  'broke plan + won' is the most dangerous outcome.")

    grades = Counter(t["grade"] for t in trades if t["grade"])
    if grades:
        out.append("\n  Process grades: " + "  ".join(
            f"{g}:{grades[g]}" for g in sorted(grades)))

    mistakes = Counter(t["mistake"] for t in trades if t["mistake"])
    if mistakes:
        out.append("\n" + "-" * w)
        out.append("  RECURRING MISTAKES")
        out.append("-" * w)
        worst = defaultdict(float)
        for t in trades:
            if t["mistake"]:
                worst[t["mistake"]] += t["r"]
        for m, c in mistakes.most_common(10):
            out.append(f"  {m[:34]:<36}{c:>3}x  {worst[m]:>8.2f}R")
        out.append("\n  Fix the most frequent one first. One specific behavioral")
        out.append("  fix per week beats a resolution to 'be more disciplined'.")

    # --- monte carlo
    if n >= 20:
        mc = monte_carlo_ruin(rs, args.risk, args.horizon, args.simulations)
        out.append("\n" + "-" * w)
        out.append(f"  MONTE CARLO — {args.simulations:,} runs of "
                   f"{args.horizon} trades at {args.risk}% risk")
        out.append("-" * w)
        out.append("  Resampled from your own trade distribution.")
        out.append("")
        out.append(f"  Risk of ruin (-50%)     {mc['ruin_pct']:>8.2f} %")
        out.append(f"  Median final equity     {mc['median_final']:>8.2f} x")
        out.append(f"  5th percentile          {mc['p05_final']:>8.2f} x")
        out.append(f"  95th percentile         {mc['p95_final']:>8.2f} x")
        out.append(f"  Mean max drawdown       {mc['mean_max_dd']:>8.1f} %")
        out.append("")
        if mc["ruin_pct"] > 5:
            out.append(f"  !! {mc['ruin_pct']:.1f}% ruin risk is unacceptably high.")
            out.append("     Halving risk per trade cuts this immediately and with")
            out.append("     certainty — no strategy improvement required.")
        elif mc["ruin_pct"] > 1:
            out.append("  Ruin risk is meaningful. Consider reducing size.")
        else:
            out.append("  Ruin risk is acceptable at this position size.")
        out.append("\n  Caveat: assumes future trades resemble past ones and that")
        out.append("  outcomes are independent. Neither is strictly true.")

    out.append("\n" + "=" * w + "\n")
    return "\n".join(out)


def main():
    p = argparse.ArgumentParser(
        description="Analyze a CSV trade journal: expectancy, drawdown, risk of ruin.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    p.add_argument("csvfile", help="Path to trade journal CSV")
    p.add_argument("-r", "--risk", type=float, default=1.0,
                   help="Risk per trade as %% of equity for simulation (default: 1.0)")
    p.add_argument("-n", "--horizon", type=int, default=250,
                   help="Trades per simulated run (default: 250)")
    p.add_argument("-s", "--simulations", type=int, default=10000,
                   help="Number of simulation runs (default: 10000)")
    args = p.parse_args()

    trades, skipped = load_trades(args.csvfile)
    if skipped:
        print(f"Note: skipped {skipped} row(s) with missing or invalid r_multiple.",
              file=sys.stderr)
    print(report(trades, args))
    return 0


if __name__ == "__main__":
    sys.exit(main())
