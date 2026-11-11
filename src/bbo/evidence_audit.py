"""Reconcile canonical portal observations with the eight published decision ledgers.

This is a *data provenance audit*, not an optimiser or a recreation of the
historic candidate-generating code. It validates every one of 104 submitted
input/output pairs, without assuming that reproducing a score reproduces
the decision that led to it.
"""
from __future__ import annotations

import csv
from decimal import Decimal
from pathlib import Path

DIMENSIONS = {1: 2, 2: 2, 3: 3, 4: 4, 5: 4, 6: 5, 7: 6, 8: 8}
F7_R11_INPUT = "0.233000-0.128000-0.522000-0.276000-0.310000-0.667000"
F7_R11_SCORE = Decimal("3.278967926227992")


def root_path(root=None):
    return Path(root) if root is not None else Path(__file__).resolve().parents[2]


def read_csv(path):
    with path.open(newline="", encoding="utf-8") as stream:
        return list(csv.DictReader(stream))


def audit_portal_history(root=None):
    """Require exact numerical agreement for all eight functions and all 13 rounds.

    Input formatting varies between six-place strings and shorter numeric
    representations in the ledgers, so compare Decimal *values*, not strings.
    The confirmed F7 R11 source email is a fixed, explicit regression guard.
    """
    root = root_path(root)
    rows = read_csv(root / "data" / "all_observations.csv")
    if len(rows) != 279:
        raise AssertionError(f"Expected 279 total records; found {len(rows)}.")
    if sum(r["source"] == "course_initial" for r in rows) != 175:
        raise AssertionError("Course initial record count changed.")
    own = [r for r in rows if r["source"] == "personal_portal"]
    if len(own) != 104:
        raise AssertionError("Personal portal record count changed.")
    if any(r["input_status"] != "confirmed" for r in rows):
        raise AssertionError("An observation has an unconfirmed input.")

    portal = {(int(r["function"]), int(r["round"])): r for r in own}
    if len(portal) != 104:
        raise AssertionError("Duplicate function/round keys in personal results.")

    verified = 0
    for function, dims in DIMENSIONS.items():
        ledger = read_csv(root / f"functions/F{function}/selection_history.csv")
        if len(ledger) != 13 or {int(r["round"]) for r in ledger} != set(range(1, 14)):
            raise AssertionError(f"F{function} ledger is not complete for 13 rounds.")

        for item in ledger:
            key = (function, int(item["round"]))
            record = portal[key]
            observed = [Decimal(record[f"x{i}"]) for i in range(1, dims + 1)]
            recorded = [Decimal(value) for value in item["submitted_input"].split("-")]
            if observed != recorded:
                raise AssertionError(f"Submitted coordinates disagree at F{function} R{key[1]}.")
            if Decimal(record["output"]) != Decimal(item["actual_output"]):
                raise AssertionError(f"Actual portal score disagrees at F{function} R{key[1]}.")
            if item["input_status"] != "confirmed":
                raise AssertionError(f"Ledger input not confirmed at F{function} R{key[1]}.")
            verified += 1

    f7 = portal[(7, 11)]
    coordinate_text = "-".join(f"{Decimal(f7[f'x{i}']):.6f}" for i in range(1, 7))
    if coordinate_text != F7_R11_INPUT or Decimal(f7["output"]) != F7_R11_SCORE:
        raise AssertionError("CONFIRMED F7 R11 input/output changed: check official email.")

    short_log = next(
        r for r in read_csv(root / "data" / "portal_rounds_11_12.csv")
        if int(r["Function"]) == 7 and int(r["Round"]) == 11
    )
    if (short_log["Input"] != F7_R11_INPUT or
            Decimal(short_log["Output"]) != F7_R11_SCORE or
            short_log["Input_Status"] != "confirmed"):
        raise AssertionError("R11–12 CSV contradicts the confirmed F7 R11 source.")

    return {
        "total_observations": len(rows),
        "initial_observations": 175,
        "portal_returns": verified,
        "confirmed_f7_r11": coordinate_text,
        "f7_r11_score": str(F7_R11_SCORE),
    }


if __name__ == "__main__":
    facts = audit_portal_history()
    for name, value in facts.items():
        print(f"{name}: {value}")
