# Data guide

## What is actually recorded?

| Source | Count | Use |
|---|---:|---|
| Course-provided initial observations | **175** | Starting evidence across eight functions |
| Personal portal returns, R1–R10 | **80** | [Recorded round history](accumulated/history_through_week10.csv) |
| Personal portal returns, R11–R12 | **16** | [Round 11/12 portal log](portal_rounds_11_12.csv) |
| Personal portal returns, R13 | **8** | [Final portal log](portal_rounds_13.csv) |
| **Total verified** | **279** | Includes repeated input locations |

All 13 rounds have returned: 104 personal portal evaluations (13 × 8), plus 175 initial supplied observations.

## Find the right data file

- **Best inputs and results:** [reports/current_best_after_week13.csv](../reports/current_best_after_week13.csv)
- **Full cumulative history through R13:** [data/accumulated/history_through_week13.csv](accumulated/history_through_week13.csv)
- **Historical portal scores through R10:** [data/accumulated/history_through_week10.csv](accumulated/history_through_week10.csv)
- **Exact later portal returns and known missing coordinate:** [data/portal_rounds_11_12.csv](portal_rounds_11_12.csv)
- **Exact Round 13 portal returns:** [data/portal_rounds_13.csv](portal_rounds_13.csv)
- **F8 initial versus later validation observations:** [data/accumulated/function_8/observations_through_week13.csv](accumulated/function_8/observations_through_week12.csv)
- **Initial-data source and redistribution caveat:** [data/initial/README.md](initial/README.md)
- **Full dataset description:** [docs/datasheet.md](../docs/datasheet.md)

## Interpretation rules

1. A *round's output* is not necessarily the highest score seen **so far**. Recompute cumulative best from observed outputs when plotting.
2. Inputs lie in the legal six-decimal portal range. The effective upper coordinate is `0.999999`, not `1.000000`.
3. The eight response scales differ, so their raw scores must not be combined.
4. External published observations can inform model comparisons but must remain separately attributed and **must not be counted as personal returns**.
5. Historical CSVs and models were created at different dates. Prefer the **through-R13** results for current reporting; retain earlier snapshots to document the sequence of decisions.

**Known gap:** R11's F7 output is known, but the exact submitted coordinate is not preserved in the available source. It remains missing rather than being imputed.

[Provenance](../docs/evidence_provenance.md) · [Evidence and limitations](../docs/round12_evidence.md) · [Main README](../README.md)
