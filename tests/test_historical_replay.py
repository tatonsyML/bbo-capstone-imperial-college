"""Check chronological provenance and safe preparation of original weekly scripts."""
from __future__ import annotations

import ast
import csv
from io import BytesIO
import json
from pathlib import Path
from zipfile import ZipFile

import numpy as np
import pytest

from scripts.historical_replay import INITIAL_COUNTS, ROOT, SOURCES, prepare


def _ledger(function: int):
    path = ROOT / "functions" / f"F{function}" / "selection_history.csv"
    with path.open(newline="", encoding="utf-8") as source:
        rows = list(csv.DictReader(source))
    assert len(rows) == 13
    return {int(r["round"]): r for r in rows}


def test_round8_prospective_forecasts_cross_referenced():
    expected = {2: 0.695189, 3: -0.019675, 5: 5654.123, 7: 1.791396}
    for function in range(1, 9):
        row = _ledger(function)[8]
        if function in expected:
            assert float(row["pre_result_forecast"]) == pytest.approx(expected[function])
            assert row["forecast_provenance"] == "recorded_before_return_approximate"
            assert row["forecast_source_path"] == "journey/round_08/README.md"
        elif function == 8:
            assert not row["pre_result_forecast"], "Multiple kernel forecasts are not a single mean"
            assert row["forecast_provenance"] == "recorded_before_return_three_gp_kernels"
            for prediction in ("9.902821", "9.906066", "9.907368"):
                assert prediction in row["forecast_details"]
            assert row["forecast_source_path"] == "journey/round_08/README.md"
        else:
            assert not row["pre_result_forecast"]
            assert row["forecast_provenance"] == "not_retained"


def test_round12_records_original_analysis_without_claiming_exact_selector():
    dated = "journey/round_12/original/week12_full_review_2026-11-02.md"
    code = "journey/round_12/original/review_round12.py"
    for f in range(1, 9):
        row = _ledger(f)[12]
        assert row["selection_record_path"] == dated
        assert (ROOT / dated).is_file()
        if f in (2, 3, 4, 6):
            assert row["related_code_path"] == code
            assert (ROOT / code).is_file()
            assert row["code_evidence_status"] == "related_historical_analysis_not_verified_exact"
        else:
            assert not row["related_code_path"]
            assert row["code_evidence_status"] == "original_selection_script_not_retained"


def test_archive_replay_prepares_canonical_initial_arrays(tmp_path):
    work = tmp_path / "round8"
    report = prepare(8, work)
    assert report["source_byte_identical"] is True
    assert report["source_record_cutoff"] == 7
    assert report["status"] == "RETROSPECTIVE_CSV_DERIVED_INPUT_REPLAY"
    assert (work / Path(SOURCES[8]).name).read_bytes() == (ROOT / SOURCES[8]).read_bytes()
    assert len(report["submitted_portal_vectors_for_comparison_only"]) == 8
    for f, count in enumerate(INITIAL_COUNTS, 1):
        x = np.load(work / "initial_data" / f"function_{f}" / "initial_inputs.npy")
        y = np.load(work / "initial_data" / f"function_{f}" / "initial_outputs.npy")
        assert x.shape[0] == y.shape[0] == count
    with pytest.raises(FileExistsError):
        prepare(8, work)


def test_round2_source_zip_and_first_round_have_no_future_portal_results(tmp_path):
    work = tmp_path / "round2"
    report = prepare(2, work)
    assert report["source_record_cutoff"] == 1
    with ZipFile(work / "source_data" / "Initial_data_points_starter(1).zip") as archive:
        expected = "initial_data/function_8/initial_inputs.npy"
        assert expected in archive.namelist()
        x = np.load(BytesIO(archive.read(expected)))
        assert x.shape == (40, 8)
    with ZipFile(work / "source_data" / "capstoneprojectweek1submissionprocessed.zip") as archive:
        points = ast.literal_eval(archive.read("inputs.txt").decode())
        scores = ast.literal_eval(archive.read("outputs.txt").decode())
    assert len(points) == len(scores) == 8
    assert scores[7] == pytest.approx(9.8321123600691)


def test_round4_three_earlier_rounds_are_separate(tmp_path):
    work = tmp_path / "round4"
    report = prepare(4, work)
    assert report["source_record_cutoff"] == 3
    src = work / "source_data"
    inputs = [ast.literal_eval(s) for s in (src / "inputs_rounds_1_to_3.txt").read_text().splitlines()]
    outputs = [ast.literal_eval(s) for s in (src / "outputs_rounds_1_to_3.txt").read_text().splitlines()]
    assert len(inputs) == len(outputs) == 3
    assert all(len(r) == 8 for r in inputs + outputs)
    assert outputs[2][7] == pytest.approx(9.8634785625365)


def test_round9_source_unchanged_and_no_generated_inputs(tmp_path):
    work = tmp_path / "round9"
    report = prepare(9, work)
    assert report["source_record_cutoff"] == 8
    assert (work / Path(SOURCES[9]).name).read_bytes() == (ROOT / SOURCES[9]).read_bytes()
    assert not (work / "source_data").exists()
    assert json.loads((work / "replay_manifest.json").read_text())["round"] == 9
