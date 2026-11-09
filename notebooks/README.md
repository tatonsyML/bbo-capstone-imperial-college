# Final reproducible notebook

**Start here for Component 25.3:** [Capstone_Final_Walkthrough.ipynb](Capstone_Final_Walkthrough.ipynb). It describes and executes the core data audit, verified results, Gaussian Process decision demonstration and independently testable F5/F8 evidence.

Run it from the repository root or the `notebooks/` folder:

```bash
python -m pip install -r requirements-notebook.txt
python -m jupyter nbconvert --to notebook --execute notebooks/Capstone_Final_Walkthrough.ipynb --output Capstone_Final_Walkthrough_executed.ipynb
```

The output notebook is generated locally or by GitHub Actions. On the review branch, the workflow also commits a verified executed copy, so tables and figures remain visible when opening the source notebook on GitHub. The [automated notebook job](https://github.com/tatonsyML/bbo-capstone-imperial-college/actions/workflows/notebook-25-3.yml) executes the same cells and saves a downloadable notebook artifact. The published notebook includes executed outputs after the dedicated notebook verification workflow completes.

The three earlier small notebooks are dated explorations that were not saved with output cells. They are not the assessed 25.3 reproduction path.

| Earlier notebook | Purpose | Status |
|---|---|---|
| [Exploratory analysis](exploratory_analysis.ipynb) | Week 9 best-so-far diagnostic | Historical helper |
| [Model comparison](model_comparison.ipynb) | HEBO-inspired and TuRBO-style proposals | Historical helper |
| [Optimisation review](optimisation_review.ipynb) | Round 10 candidate archive | Historical helper |

[Assessment map](../docs/assessment_25_3.md) · [Datasheet](../DATASHEET.md) · [Model card](../MODEL_CARD.md)
