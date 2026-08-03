#!/usr/bin/env python3
"""Position sizing calculator.

Position size is an output, never an input. You choose where the stop goes;
the share count falls out of arithmetic. See 04-risk-management.md.

Usage:
    python3 position_size.py --account 30000 --risk 1 --entry 50.00 --stop 48.50
    python3 position_size.py -a 30000 -r 1 -e 50.00 -s 48.50 -t 53.00
    python3 position_size.py -a 30000 -r 1 -e 50.00 -s 48.50 --contract-size 5

The --contract-size flag handles futures and other instruments where one
unit represents a multiple of the quoted price (e.g. MES = $5 per index point).
"""

import argparse
import sys


def calculate(account, risk_pct, entry, stop, target=None, contract_size=1.0):
    """Return a dict describing the position implied by these parameters."""
    if account <= 0:
        raise ValueError("Account size must be positive.")
    if not 0 < risk_pct <= 100:
        raise ValueError("Risk percent must be between 0 and 100.")
    if entry <= 0 or stop <= 0:
        raise ValueError("Entry and stop prices must be positive.")
    if entry == stop:
        raise ValueError("Entry and stop cannot be equal — risk would be zero.")
    if contract_size <= 0:
        raise ValueError("Contract size must be positive.")

    direction = "LONG" if stop < entry else "SHORT"
    risk_amount = account * (risk_pct / 100.0)
    risk_per_unit = abs(entry - stop) * contract_size
    units = int(risk_amount // risk_per_unit)
    actual_risk = units * risk_per_unit
    notional = units * entry * contract_size

    result = {
        "direction": direction,
        "risk_amount": risk_amount,
        "risk_per_unit": risk_per_unit,
        "units": units,
        "actual_risk": actual_risk,
        "actual_risk_pct": (actual_risk / account) * 100.0,
        "notional": notional,
        "leverage": notional / account,
    }

    if target is not None:
        if target <= 0:
            raise ValueError("Target price must be positive.")
        reward_per_unit = abs(target - entry) * contract_size
        # A target on the wrong side of entry is a common data-entry error and
        # silently produces a meaningless R:R, so flag it rather than report it.
        target_is_profitable = (
            target > entry if direction == "LONG" else target < entry
        )
        result.update(
            {
                "target": target,
                "reward_per_unit": reward_per_unit,
                "total_reward": units * reward_per_unit,
                "rr_ratio": reward_per_unit / risk_per_unit,
                "target_is_profitable": target_is_profitable,
            }
        )

    return result


def format_report(r, account, risk_pct, entry, stop, contract_size):
    unit = "contracts" if contract_size != 1 else "shares"
    lines = [
        "",
        "=" * 52,
        f"  POSITION SIZE — {r['direction']}",
        "=" * 52,
        "",
        f"  Account            ${account:>14,.2f}",
        f"  Risk budget        {risk_pct:>14.2f}%  (${r['risk_amount']:,.2f})",
        "",
        f"  Entry              ${entry:>14,.4f}",
        f"  Stop               ${stop:>14,.4f}",
        f"  Risk per unit      ${r['risk_per_unit']:>14,.4f}",
        "",
        "-" * 52,
        f"  SIZE               {r['units']:>14,d}  {unit}",
        "-" * 52,
        "",
        f"  Actual risk (1R)   ${r['actual_risk']:>14,.2f}"
        f"   ({r['actual_risk_pct']:.2f}%)",
        f"  Notional           ${r['notional']:>14,.2f}",
        f"  Leverage           {r['leverage']:>14.2f}x",
    ]

    if "target" in r:
        lines += [
            "",
            f"  Target             ${r['target']:>14,.4f}",
            f"  Reward             ${r['total_reward']:>14,.2f}",
            f"  Reward:Risk        {r['rr_ratio']:>14.2f} : 1",
        ]

    lines.append("")

    warnings = []
    if r["units"] == 0:
        warnings.append(
            "Size rounds to ZERO — risk budget is smaller than one unit of "
            "risk.\n     Do NOT tighten the stop to fix this. Skip the trade "
            "or trade a\n     smaller-denomination instrument."
        )
    if r["leverage"] > 1.0:
        warnings.append(
            f"Notional exceeds account equity ({r['leverage']:.2f}x). This "
            "requires\n     margin. Risk is still capped at your stop, but a "
            "gap through it\n     can exceed 1R."
        )
    if "target" in r:
        if not r["target_is_profitable"]:
            warnings.append(
                "Target is on the LOSING side of entry — check your inputs."
            )
        elif r["rr_ratio"] < 2.0:
            warnings.append(
                f"Reward:Risk is {r['rr_ratio']:.2f}:1, below the 2:1 minimum "
                "suggested in\n     chapter 04. Requires a high win rate to "
                "stay profitable."
            )

    if warnings:
        lines.append("  WARNINGS")
        for w in warnings:
            lines.append(f"   !!  {w}")
        lines.append("")

    return "\n".join(lines)


def main():
    p = argparse.ArgumentParser(
        description="Calculate position size from account risk and stop distance.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    p.add_argument("-a", "--account", type=float, required=True,
                   help="Account equity in currency units")
    p.add_argument("-r", "--risk", type=float, default=1.0,
                   help="Risk per trade as percent of account (default: 1.0)")
    p.add_argument("-e", "--entry", type=float, required=True,
                   help="Planned entry price")
    p.add_argument("-s", "--stop", type=float, required=True,
                   help="Stop loss price")
    p.add_argument("-t", "--target", type=float, default=None,
                   help="Profit target price (optional)")
    p.add_argument("-c", "--contract-size", type=float, default=1.0,
                   help="Currency value per 1.00 of price movement (default: 1.0)")

    args = p.parse_args()

    try:
        r = calculate(args.account, args.risk, args.entry, args.stop,
                      args.target, args.contract_size)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    print(format_report(r, args.account, args.risk, args.entry, args.stop,
                        args.contract_size))
    return 0


if __name__ == "__main__":
    sys.exit(main())
