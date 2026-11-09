# Reproduce the evidence

This guide distinguishes **tests that are executable from this repository** from **historical experiments whose exact environment or scripts are not fully retained**.

## Quick start

Requirements: Python, pip, a shell and access to the repository root. The package dependencies are pinned in [requirements.txt](../requirements.txt), except for the minimum pytest version.

```bash
python -m pip install -r requirements.txt
PYTHONPATH=src python -m bbo.structural_validation
PYTHONPATH=src python -m pytest -q
```

On Windows PowerShell, replace `PYTHONPATH=src <command>` with `$env:PYTHONPATH = 'src'` followed by the command.

## What the structural validation checks

| Check | Input | Expected conclusion |
|---|---|---|
| F8 full-rank fit | 40 initial course observations | 17 identifiable coefficients |
| F8 post-fit validation | 13 later personal portal returns, excluded from fit | Maximum absolute error under `2e-14` (test threshold) |
| F8 predicted vertex | Recovered quadratic | Centre approximately `(0.10,0.15,0.13,0.15,0.80,0.50,0.20,0.60)`, maximum approximately 10 |
| F5 permitted corner | Four inputs of `0.999999` | Approximately `8662.405001248297` |

The code is in [src/bbo/structural_validation.py](../src/bbo/structural_validation.py) and tests in [tests/test_structural_validation.py](../tests/test_structural_validation.py). The [F8 CSV](../data/accumulated/function_8/observations_through_week13.csv) labels initial versus later points. The model fits **only the initial 40**.

The test demonstrates a strong retrospective fit and held-out prediction for that equation family. It is not evidence that this model was used in Round 1.

## Other source material

The historical GP and acquisition pipeline is available in [src/bbo](../src/bbo/) with [run_pipeline.py](../run_pipeline.py), [notebooks](../notebooks/) and [configs](../configs/optimisation.yaml).

```bash
PYTHONPATH=src python -m bbo.pipeline
```

**Scope:** the pipeline is a preserved older demonstration with a data cut through Week 10. It **does not** reproduce every Round 11–13 candidate-selection experiment and must not be presented as such. Some notebooks are short exploratory snapshots rather than polished end-to-end applications.

## Evidence and limitations

- Latest verified status: **all 13 rounds**, or 104 personal portal evaluations.
- The [Round 13 input/output log](../data/portal_rounds_13.csv) and [final audit](round13_evidence.md) are verified.
- The exact R11 input on F7 is missing from the available retained sources; its returned score was recorded.
- Published external examples informed later investigations but must not be mixed into the personal returns dataset without source labelling and any required academic attribution.
- Complete official HEBO and TuRBO frameworks are **not** claimed to have been benchmarked.
- Starting observations and past bests are distinct from an individual round's returned outcome.

For a short explanation start with [the README](../README.md), then consult [methods](strategy_and_validation.md), [mathematical reconstruction](structural_reconstruction.md) and [data provenance](evidence_provenance.md).
