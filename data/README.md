# Data guide

## What is actually recorded?

The complete dataset contains **279 rows (approximately 40 KB)** and is stored in this repository. No large datasets are hosted here. External datasets, if needed for further research, should be linked rather than committed.

| Source | Count | Use |
|---|---:|---|
| Course-provided initial observations | **175** | Starting evidence across eight functions |
| Personal portal returns, R1–R10 | **80** | [Recorded round history](accumulated/history_through_week10.csv) |
| Personal portal returns, R11–R12 | **16** | [Round 11/12 portal log](portal_rounds_11_12.csv) |
| Personal portal returns, R13 | **8** | [Final portal log](portal_rounds_13.csv) |
| **Total verified** | **279** | Includes repeated input locations |

All 13 rounds have returned: 104 personal portal evaluations (13 × 8), plus 175 initial supplied observations.

**Complete observational record:** [279 rows in one tidy CSV](all_observations.csv), comprising 175 course-provided and 104 personal portal outcomes. All 104 personal portal returns have confirmed input coordinates.

**Source of truth:** `data/all_observations.csv` is the authoritative complete dataset. Each `functions/F1/observations.csv` through `functions/F8/observations.csv` is an exact function-specific partition for convenient reading. [Automated ledger tests](../tests/test_function_ledgers.py) check that these copies match the master record row for row. Earlier `data/accumulated/` cut-offs remain available for reproducing the evidence available at different rounds; they are not interchangeable with the completed dataset.

## CSV column conventions

The files use different, intentional header conventions because they serve different roles. **Column names are case-sensitive** in pandas and other analysis tools. For new analysis, start with the [complete observational record](all_observations.csv); do not rename preserved historical files merely to make their headers look alike.

| File family | Example columns | Meaning |
|---|---|---|
| [Complete observations](all_observations.csv) and each function's `observations.csv` | `function`, `round`, `x1`–`x8`, `output` | Canonical measured inputs and scores, including initial observations |
| `functions/F1`–`F8/selection_history.csv` | `round`, `submitted_input`, `actual_output` | One portal submission and return per function per round, plus decision evidence |
| [R11–R12](portal_rounds_11_12.csv) and [R13](portal_rounds_13.csv) portal logs | `Function`, `Round`, `Input`, `Output`, `Input_Status` | Preserved compact round logs |
| [Accumulated function snapshots](accumulated/function_8/observations_through_week9.csv) | `function`, `stage`, `x1`–`x8`, `output` | Earlier observation cut-offs with only that function's input dimensions |
| [Cumulative history](accumulated/history_through_week13.csv) | `Function`, `Stage`, `Input`, `Output`, `Best_so_far` | Chronological scores and running best |
| [Final best-score summary](../results/current_best_after_week13.csv) | `Function`, `Final_Best`, `Best_Input` | Derived best result per function, not an individual portal return |

For a matching function and round, `actual_output` in its selection ledger and `Output` in a portal log refer to the corresponding `output` in the master record. Likewise, `submitted_input` and `Input` are hyphen-separated views of the master `x1`–`x8` coordinates. By contrast, `Best_so_far` and `Final_Best` are *aggregates*, not interchangeable with an individual `output`. Check both the file's role and the recorded function/round when joining tables.

## Find the right data file

- **Best inputs and results:** [results/current_best_after_week13.csv](../results/current_best_after_week13.csv)
- **Full cumulative history through R13:** [data/accumulated/history_through_week13.csv](accumulated/history_through_week13.csv)
- **Historical portal scores through R10:** [data/accumulated/history_through_week10.csv](accumulated/history_through_week10.csv)
- **Exact later portal returns, including confirmed F7 R11 coordinates:** [data/portal_rounds_11_12.csv](portal_rounds_11_12.csv)
- **Exact Round 13 portal returns:** [data/portal_rounds_13.csv](portal_rounds_13.csv)
- **F8 initial versus later validation observations:** [data/accumulated/function_8/observations_through_week13.csv](accumulated/function_8/observations_through_week13.csv)
- **Original-data provenance and redistribution caveat:** [usage and permissions](../USAGE_AND_PERMISSIONS.md)
- **Full dataset description:** [DATASHEET.md](../DATASHEET.md)

## Interpretation rules

1. A *round's output* is not necessarily the highest score seen **so far**. Recompute cumulative best from observed outputs when plotting.
2. Inputs lie in the legal six-decimal portal range. The effective upper coordinate is `0.999999`, not `1.000000`.
3. The eight response scales differ, so their raw scores must not be combined.
4. External published observations can inform model comparisons but must remain separately attributed and **must not be counted as personal returns**.
5. Historical CSVs and models were created at different dates. Prefer the **through-R13** results for current reporting; retain earlier snapshots to document the sequence of decisions.

**Function 7, Round 11:** The confirmed portal input was `0.233000-0.128000-0.522000-0.276000-0.310000-0.667000`, returning `3.278967926227992`. All 104 submitted vectors are present in the complete dataset.

[Provenance](../DATASHEET.md) · [Evidence and limitations](../journey/round_12/README.md) · [Main README](../README.md)
