# Black-Box Optimisation Capstone

**Status:** observed data through Week 9; Round 10 candidates are prospective and are not included in observed performance.

This repository preserves the original capstone architecture while reflecting how the project evolved. It separates reusable optimisation code, historical evidence, accumulated data, exploratory notebooks, reports and transparency documentation.

## Core workflow

`observations → surrogate/challengers → acquisition/diagnostics → candidate decision → portal query → update`

The current framework is **evidence-gated**. HEBO-inspired, TuRBO-style, GP committee, local-fit and structural candidates are challengers. A more sophisticated model does not automatically outrank stronger direct evidence.

## Repository structure

```text
bbo-capstone-imperial-college/
├── README.md
├── requirements.txt
├── requirements-advanced.txt
├── configs/
├── data/
│   ├── initial/
│   └── accumulated/
├── src/bbo/
├── experiments/
├── notebooks/
├── reports/
├── docs/
└── tests/
```

## Evidence discipline

The project distinguishes four evidence classes:

1. **Observed** — portal inputs and returned outputs.
2. **Prospective** — forecasts and rationale recorded before a result.
3. **Retrospective** — challenger analyses performed later.
4. **Interpretive** — conclusions made after comparing forecasts with observations.

Retrospective HEBO/TuRBO recommendations never receive invented portal scores.

## Module 21 transparency documents

- [Datasheet](docs/datasheet.md)
- [Model card](docs/model_card.md)
- [Decision log](docs/decision_log.md)

## Assessment submission archive

Historical/final assessment-facing versions are kept separately from the living project under [submissions/](submissions/README.md). Exact historical text is archived only when it can be recovered; missing older submissions are explicitly marked rather than reconstructed.

## Current observed dataset

The current cut contains **247 observed evaluations**:

- 175 programme-supplied initial observations
- 72 submitted Week 1–9 observations

Per function the totals are 19, 19, 24, 39, 29, 29, 39 and 49.

Round 10 is kept separately as prospective evidence until the portal returns results.

## Reproduce

```bash
python -m pip install -r requirements.txt
PYTHONPATH=src python -m bbo.pipeline
python -m pytest -q
```

Optional advanced challenger packages are listed in `requirements-advanced.txt`.

## Transparency note

A rerunnable model is not the same as a reproducible decision. The repository therefore preserves not only code and data, but also the evidence class and rationale behind important query decisions.
