# Run the final notebook

Start with [Capstone_Final_Walkthrough.ipynb](Capstone_Final_Walkthrough.ipynb). It audits all 104 recorded personal portal queries, demonstrates GP/EI and HEBO-inspired / TuRBO-style approaches, and validates the F1, F5, F7 and F8 mathematical investigations. It does not claim to recreate every original candidate-selection decision.

## Run locally

From the repository root using Python 3.11:

```bash
python -m pip install -r requirements-notebook.txt
python -m pytest -q
jupyter notebook notebooks/Capstone_Final_Walkthrough.ipynb
```

To generate a fresh executed copy without changing the versioned notebook:

```bash
python -m jupyter nbconvert --to notebook --execute notebooks/Capstone_Final_Walkthrough.ipynb --output Capstone_Final_Walkthrough_executed.ipynb
```

The [GitHub Actions notebook workflow](https://github.com/tatonsyML/bbo-capstone-imperial-college/actions/workflows/notebook-25-3.yml) executes the notebook and saves the result as a **downloadable workflow artifact**. It does **not** commit output files to pull-request branches.

## Implementation guide

| Component | Source |
|---|---|
| GP surrogate models and output transforms | [surrogates.py](../src/bbo/surrogates.py) |
| EI, PI and UCB acquisition functions | [acquisition.py](../src/bbo/acquisition.py) |
| Candidate sampling and bounds | [search.py](../src/bbo/search.py) |
| HEBO-inspired / TuRBO-style examples | [optimizer.py](../src/bbo/optimizer.py) |
| F1 retrospective fit | [f1_reconstruction.py](../src/bbo/f1_reconstruction.py) |
| F5 / F8 mathematical validation | [structural_validation.py](../src/bbo/structural_validation.py) |
| F7 positive Hartmann-6 numerical check | [f7_reconstruction.py](../src/bbo/f7_reconstruction.py) |
| All 104 submitted inputs and scores | [evidence_audit.py](../src/bbo/evidence_audit.py) |

The [four Week 12 optimisation scripts](../journey/round_12/README.md#week-12-modelling-and-optimisation-code) and their saved model results are available in the Round 12 research record. They include PCA/kernel PCA, Optuna TPE, robust GP comparisons and trust-region Thompson sampling. These historical experiments are distinct from the final notebook's illustrative implementations.

The full HEBO and BoTorch TuRBO-1 [comparison](../research/full_optimisers/README.md) is a separate **post-capstone** experiment using a fitted simulator, not additional portal results.

## Earlier exploratory notebooks

| Notebook | Scope |
|---|---|
| [Exploratory analysis](../journey/round_10/early_notebooks/exploratory_analysis.ipynb) | Week 9 score diagnostics |
| [Model comparison](../journey/round_10/early_notebooks/model_comparison.ipynb) | HEBO-inspired and TuRBO-style proposals |
| [Optimisation review](../journey/round_10/early_notebooks/optimisation_review.ipynb) | Round 10 candidate analysis |

[Source code guide](../src/bbo/README.md) · [Data description](../DATASHEET.md) · [Model card](../MODEL_CARD.md) · [All functions](../functions/README.md)
