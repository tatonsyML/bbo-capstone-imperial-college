# Complete function-by-function experiment ledgers

These pages present the **same experimental history** as the [13-round journey](../journey/README.md), reorganised by function without replacing the original documents. The single source of truth remains [all_observations.csv](../data/all_observations.csv): **175 course-provided starting observations plus 104 personal portal returns, 279 total.**

| Function | Dimensions | Initial observations | Real portal rounds | Best measured result | Decision ledger |
|---|---:|---:|---:|---:|---|
| [F1](F1/README.md) | 2 | 10 | 13 | `1.999999999676` | [CSV](F1/selection_history.csv) |
| [F2](F2/README.md) | 2 | 10 | 13 | `0.7442504263021` | [CSV](F2/selection_history.csv) |
| [F3](F3/README.md) | 3 | 15 | 13 | `-0.003753096918719` | [CSV](F3/selection_history.csv) |
| [F4](F4/README.md) | 4 | 30 | 13 | `0.7468979113807` | [CSV](F4/selection_history.csv) |
| [F5](F5/README.md) | 4 | 20 | 13 | `8662.405001248` | [CSV](F5/selection_history.csv) |
| [F6](F6/README.md) | 5 | 20 | 13 | `-0.03751864724437` | [CSV](F6/selection_history.csv) |
| [F7](F7/README.md) | 6 | 30 | 13 | `3.322368011393` | [CSV](F7/selection_history.csv) |
| [F8](F8/README.md) | 8 | 40 | 13 | `10.00000000000` | [CSV](F8/selection_history.csv) |

## How to use the function pages

Open F1–F8 for all 13 submitted coordinate vectors, actual returned scores and links to the underlying Round evidence. Each directory has a full-precision `observations.csv`, a 13-row `selection_history.csv` with decision and code provenance, and a `model_runs/README.md` explaining how to refit a surrogate without future information.

**What is missing:** The exact submitted input for F7 Round 11, although its output is known. Several original optimisation scripts and fitted kernel objects were never retained. No invented coordinates, fitted parameters or unobserved function scores are added.

## One codebase, separately fitted models

The [shared GP](../src/bbo/surrogates.py), [acquisition functions](../src/bbo/acquisition.py), and [candidate search](../src/bbo/search.py) are common to F1–F8. Each function has its own dimension, training observations, fitted hyperparameters and acquisition scores. A single new [GP replay script](../scripts/replay_surrogates.py) handles `--function 1` through `--function 8` and `--round 1` through `--round 13`.

```bash
python -m pip install -r requirements.txt
python scripts/replay_surrogates.py --function 2 --round 9 --kernel Matern25 --acquisition EI --restarts 0
```

The replay uses **only the original observations available before the target Round** and labels its trained kernel parameters and suggested candidate `retrospective_counterfactual`. It does **not** claim to reproduce the original portal-selection process.

The [historical lightweight HEBO-inspired / TuRBO-style code](../src/bbo/optimizer.py) is not full HEBO or TuRBO. The [later reference benchmark](../research/full_optimisers/README.md) includes official HEBO and BoTorch-based TuRBO-1 implementations, but was **not used to generate the historic 104 submissions** and has no published full-engine comparison results.

[Main README](../README.md) · [Round-first journey](../journey/README.md) · [Methodology](../docs/methods.md).
