# Final reproducible notebook

**Start with the executable notebook:** [Capstone_Final_Walkthrough.ipynb](Capstone_Final_Walkthrough.ipynb). It describes and executes the core data audit, verified results, Gaussian Process decision demonstration and independently testable F5/F8 evidence.

Run this command from the **repository root** (the paths below assume that location):

```bash
python -m pip install -r requirements-notebook.txt
python -m jupyter nbconvert --to notebook --execute notebooks/Capstone_Final_Walkthrough.ipynb --output Capstone_Final_Walkthrough_executed.ipynb
```

The output notebook is generated locally or by GitHub Actions. The notebook workflow executes the current walkthrough and publishes an executed copy as a workflow artefact. This is not the original weekly query-selection code. The [automated notebook job](https://github.com/tatonsyML/bbo-capstone-imperial-college/actions/workflows/notebook-25-3.yml) executes the same cells and saves a downloadable notebook artifact. The published notebook includes executed outputs after the dedicated notebook verification workflow completes.

The three earlier small notebooks are dated explorations that were not saved with output cells. The final walkthrough is the current reproduction route.

| Earlier notebook | Purpose | Status |
|---|---|---|
| [Exploratory analysis](../journey/round_10/early_notebooks/exploratory_analysis.ipynb) | Week 9 best-so-far diagnostic | Historical helper |
| [Model comparison](../journey/round_10/early_notebooks/model_comparison.ipynb) | HEBO-inspired and TuRBO-style proposals | Historical helper |
| [Optimisation review](../journey/round_10/early_notebooks/optimisation_review.ipynb) | Round 10 candidate archive | Historical helper |

[Datasheet](../DATASHEET.md) · [Model card](../MODEL_CARD.md)
