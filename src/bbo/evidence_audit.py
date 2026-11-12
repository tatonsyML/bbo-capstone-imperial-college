"""Reconcile the master data with all eight historical decision ledgers.

This is an integrity check, NOT an optimisation algorithm. It confirms
that the master dataset contains 175 course-provided observations and
104 personal portal returns (13 for each of eight functions), and that
every returned input/output pair matches its function-specific ledger.

Use Decimal comparisons rather than floating-point conversions: ledger
vectors can have different equivalent numeric formatting, and the
hyphen parser must distinguish coordinate separators from the minus sign
inside exponent notation such as 1e-06.

The independent F7 Round 11 cross-check protects a historically confirmed
record against accidental transcription. Neither that check nor the other
comparisons reproduces the private function or original selector script.
No source observations are changed by this module.
"""
from __future__ import annotations

import csv
import re
from decimal import Decimal
from pathlib import Path

DIMENSIONS = {1: 2, 2: 2, 3: 3, 4: 4, 5: 4, 6: 5, 7: 6, 8: 8}
F7_R11_INPUT = "0.233000-0.128000-0.522000-0.276000-0.310000-0.667000"
F7_R11_SCORE = Decimal("3.278967926227992")


def root_path(root=None):
    """Resolve the repository root or an optional isolated test directory.

    The default path follows the package location, not the caller's
    current working directory. A supplied root supports fixture-based
    integrity tests without writing to the real research files.
    """
    return Path(root) if root is not None else Path(__file__).resolve().parents[2]


def read_csv(path):
    """Read UTF-8 CSV records as strings to retain exact decimal notation.

    Convert numeric text only when comparing values. This avoids losing
    significant decimal digits through premature float conversion.
    """
    with path.open(newline="", encoding="utf-8") as stream:
        return list(csv.DictReader(stream))


def audit_portal_history(root=None):
    """Check all recorded function/round input and output pairs.

    Parameters
    ----------
    root : path-like or None
        Checkout or test fixture root holding data/ and functions/.

    Returns
    -------
    dict
        Counts and the independently confirmed F7 Round 11 result.

    The procedure verifies the 279-row split into 175 starting and
    104 personal observations, confirmed input flags, unique portal
    function/round keys and complete 13-row decision ledgers. Inputs and
    actual scores are compared as exact decimal *values*, not text.

    The final F7 Round 11 check also verifies a separate summary CSV.
    An inconsistency raises AssertionError. These checks establish
    consistency of published data, not accuracy of a model forecast or
    recovery of an original candidate-generation algorithm.
    """
    root = root_path(root)
    # Validate the overall data contract before inspecting individual
    # ledgers; missing initial observations would distort future baselines.
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

    # Dict key cardinality detects duplicate (function, round) records
    # that would otherwise silently overwrite earlier entries.
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
            # Compare 0.700000 and 0.7 as equal numeric values. Do not
            # treat a negative exponent (e-06 or E-06) as a separator.
            observed = [Decimal(record[f"x{i}"]) for i in range(1, dims + 1)]
            recorded = [Decimal(value) for value in re.split(r"(?<![eE])-", item["submitted_input"])]
            if observed != recorded:
                raise AssertionError(f"Submitted coordinates disagree at F{function} R{key[1]}.")
            if Decimal(record["output"]) != Decimal(item["actual_output"]):
                raise AssertionError(f"Actual portal score disagrees at F{function} R{key[1]}.")
            if item["input_status"] != "confirmed":
                raise AssertionError(f"Ledger input not confirmed at F{function} R{key[1]}.")
            verified += 1

    # The original F7 R11 selection code is not required to verify the
    # measured vector and score recorded in the course results.
    f7 = portal[(7, 11)]
    coordinate_text = "-".join(f"{Decimal(f7[f'x{i}']):.6f}" for i in range(1, 7))
    if coordinate_text != F7_R11_INPUT or Decimal(f7["output"]) != F7_R11_SCORE:
        raise AssertionError("CONFIRMED F7 R11 input/output changed: check official email.")

    # Check a second published representation independently to avoid
    # changing the main table while leaving conflicting summary evidence.
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
    # Read-only command-line report: no simulation and no file mutation.
    facts = audit_portal_history()
    for name, value in facts.items():
        print(f"{name}: {value}")
