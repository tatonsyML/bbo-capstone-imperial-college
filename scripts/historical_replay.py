#!/usr/bin/env python3
"""Prepare, and optionally run, archived round-specific Python analyses.

This is a portable DATA ADAPTER for the unchanged historical scripts.
It rebuilds required data containers from verified published observations,
not from the missing original course ZIP/NumPy files. Source code is copied
unchanged into an isolated workspace. A rerun is a later reproduction and
is not proof that every historical candidate came from an exact script.
"""
from __future__ import annotations

import argparse
import csv
from hashlib import sha256
from io import BytesIO
import json
from pathlib import Path
import shutil
import subprocess
import sys
from zipfile import ZIP_DEFLATED, ZipFile

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
DIMS = (2, 2, 3, 4, 4, 5, 6, 8)
INITIAL_COUNTS = (10, 10, 15, 30, 20, 20, 30, 40)
SOURCES = {
    2: "journey/round_02/week2_ucb_course_aligned.py",
    4: "journey/round_04/capstone_bbo_week4_module15.py",
    8: "journey/round_08/capstone_bbo_module19_round8.py",
    9: "journey/round_09/round9_controlled_fits.py",
}


def observed(root: Path = ROOT) -> list[dict[str, str]]:
    path = root / "data" / "all_observations.csv"
    with path.open(newline="", encoding="utf-8") as stream:
        rows = list(csv.DictReader(stream))
    if len(rows) != 279:
        raise ValueError("Expected exactly 279 verified observations")
    if sum(r["source"] == "course_initial" for r in rows) != 175:
        raise ValueError("Starting data count has changed")
    if sum(r["source"] == "personal_portal" for r in rows) != 104:
        raise ValueError("Returned query count has changed")
    return rows


def by_function(rows: list[dict[str, str]], number: int, round_number: int):
    selected = [r for r in rows if int(r["function"]) == number
                and int(r["round"]) == round_number]
    if len(selected) != (INITIAL_COUNTS[number - 1] if round_number == 0 else 1):
        raise ValueError(f"F{number} round {round_number}: incomplete evidence")
    d = DIMS[number - 1]
    vectors = np.array([[float(r[f"x{j}"]) for j in range(1, d + 1)]
                        for r in selected], dtype=float)
    scores = np.array([float(r["output"]) for r in selected], dtype=float)
    if not np.isfinite(vectors).all() or not np.isfinite(scores).all():
        raise ValueError(f"F{number}: missing or non-finite observation")
    if (vectors < 0).any() or (vectors > 0.999999 + 1e-10).any():
        raise ValueError(f"F{number}: out-of-range input")
    return vectors, scores


def array_bytes(values: np.ndarray) -> bytes:
    output = BytesIO()
    np.save(output, values, allow_pickle=False)
    return output.getvalue()


def make_initial(rows: list[dict[str, str]], root: Path) -> None:
    """Write initial arrays in the format expected by the original R8 code."""
    for number in range(1, 9):
        x, y = by_function(rows, number, 0)
        folder = root / "initial_data" / f"function_{number}"
        folder.mkdir(parents=True, exist_ok=True)
        np.save(folder / "initial_inputs.npy", x, allow_pickle=False)
        np.save(folder / "initial_outputs.npy", y, allow_pickle=False)


def make_initial_zip(rows: list[dict[str, str]], dest: Path) -> None:
    """Make a compatible ZIP containing canonical CSV-derived initial arrays."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(dest, "w", ZIP_DEFLATED) as archive:
        for number in range(1, 9):
            x, y = by_function(rows, number, 0)
            base = f"initial_data/function_{number}/"
            archive.writestr(base + "initial_inputs.npy", array_bytes(x))
            archive.writestr(base + "initial_outputs.npy", array_bytes(y))


def make_early_rounds(rows: list[dict[str, str]], dest: Path) -> None:
    """Prepare R1–R3 files in the syntax expected by the original R4 script."""
    inp, out = [], []
    for round_number in (1, 2, 3):
        points = [by_function(rows, number, round_number)[0][0].tolist()
                  for number in range(1, 9)]
        values = [float(by_function(rows, number, round_number)[1][0])
                  for number in range(1, 9)]
        inp.append(repr(points))
        out.append(repr(values))
    (dest / "inputs_rounds_1_to_3.txt").write_text(
        "\n".join(inp) + "\n", encoding="utf-8")
    (dest / "outputs_rounds_1_to_3.txt").write_text(
        "\n".join(out) + "\n", encoding="utf-8")


def prepare(round_number: int, workspace: Path, root: Path = ROOT) -> dict:
    """Create an isolated workspace, or fail rather than overwrite a prior run."""
    if round_number not in SOURCES:
        raise ValueError("Historical replay is supported for R2, R4, R8 and R9")
    if workspace.exists() and any(workspace.iterdir()):
        raise FileExistsError(f"Refusing to overwrite replay workspace: {workspace}")
    workspace.mkdir(parents=True, exist_ok=True)
    rows = observed(root)
    source = root / SOURCES[round_number]
    if not source.is_file():
        raise FileNotFoundError(source)
    destination = workspace / source.name
    shutil.copyfile(source, destination)
    if destination.read_bytes() != source.read_bytes():
        raise RuntimeError("Historical script copy was not byte-identical")

    if round_number in (2, 4):
        data_dir = workspace / "source_data"
        data_dir.mkdir(exist_ok=True)
        make_initial_zip(rows, data_dir / "Initial_data_points_starter(1).zip")
        if round_number == 2:
            inputs = [by_function(rows, n, 1)[0][0].tolist() for n in range(1, 9)]
            values = [float(by_function(rows, n, 1)[1][0]) for n in range(1, 9)]
            with ZipFile(data_dir / "capstoneprojectweek1submissionprocessed.zip",
                         "w", ZIP_DEFLATED) as archive:
                archive.writestr("inputs.txt", repr(inputs))
                archive.writestr("outputs.txt", repr(values))
        else:
            make_early_rounds(rows, data_dir)
    elif round_number == 8:
        make_initial(rows, workspace)

    original = source.read_bytes()
    query = [by_function(rows, n, round_number)[0][0].tolist()
             for n in range(1, 9)]
    report = {
        "status": "RETROSPECTIVE_CSV_DERIVED_INPUT_REPLAY",
        "round": round_number,
        "historical_source": SOURCES[round_number],
        "source_sha256": sha256(original).hexdigest(),
        "source_byte_identical": True,
        "initial_records": 175,
        "source_record_cutoff": (round_number - 1 if round_number in (2, 4, 8)
                                 else 8),
        "submitted_portal_vectors_for_comparison_only": query,
        "disclaimer": ("Original source script unchanged; compatible inputs rebuilt "
                       "from published observations. This does not verify the "
                       "historical optimiser state or claim identical proposals."),
    }
    (workspace / "replay_manifest.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return report


def main() -> None:
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--round", required=True, type=int, choices=sorted(SOURCES))
    cli.add_argument("--workdir", type=Path,
                     help="Fresh isolated output folder (never overwritten)")
    cli.add_argument("--execute", action="store_true",
                     help="Also execute the byte-identical historical script")
    args = cli.parse_args()
    dest = (args.workdir if args.workdir else
            ROOT / "results" / "historical_replays" / f"round_{args.round:02d}")
    report = prepare(args.round, dest)
    print(f"Prepared R{args.round}: {dest}")
    print("Original script SHA-256:", report["source_sha256"])
    if args.execute:
        script = dest / Path(SOURCES[args.round]).name
        with (dest / "execution_stdout.log").open("w", encoding="utf-8") as stdout, \
             (dest / "execution_stderr.log").open("w", encoding="utf-8") as stderr:
            completed = subprocess.run(
                [sys.executable, str(script)], cwd=dest, check=False,
                stdout=stdout, stderr=stderr, timeout=1800)
        print(f"Script exit code: {completed.returncode}. Logs in {dest}")
        if completed.returncode:
            raise SystemExit(completed.returncode)


if __name__ == "__main__":
    main()
