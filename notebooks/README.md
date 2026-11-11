# Final reproducible notebook

**Start with the executable notebook:** [Capstone_Final_Walkthrough.ipynb](Capstone_Final_Walkthrough.ipynb). It audits all 104 historical submitted queries against their decision ledgers, links surviving code, demonstrates working GP/EI and simplified HEBO/TuRBO-style suggestions, verifies results, and reproduces retrospective F1/F5/F7/F8 mathematical investigations. It does not claim to regenerate all historical candidate choices.

Run it from the repository root or the `notebooks/` folder:

```bash
python -m pip install -r requirements-notebook.txt
python -m jupyter nbconvert --to notebook --execute notebooks/Capstone_Final_Walkthrough.ipynb --output Capstone_Final_Walkthrough_executed.ipynb
```

The output notebook is generated locally or by GitHub Actions. On the review branch, the workflow also commits a verified executed copy, so tables and figures remain visible when opening the source notebook on GitHub. The [automated notebook job](https://github.com/tatonsyML/bbo-capstone-imperial-college/actions/workflows/notebook-25-3.yml) executes the same cells and saves a downloadable notebook artifact. The published notebook includes executed outputs after the dedicated notebook verification workflow completes.

The three earlier small notebooks are dated explorations that were not saved with output cells. They are not the assessed 25.3 reproduction path.

| Earlier notebook | Purpose | Status |
|---|---|---|
| [Exploratory analysis](../journey/round_10/early_notebooks/exploratory_analysis.ipynb) | Week 9 best-so-far diagnostic | Historical helper |
| [Model comparison](../journey/round_10/early_notebooks/model_comparison.ipynb) | HEBO-inspired and TuRBO-style proposals | Historical helper |
| [Optimisation review](../journey/round_10/early_notebooks/optimisation_review.ipynb) | Round 10 candidate archive | Historical helper |

[Verified F7 R11 and all 104 portal records](../docs/VERIFIED_FACTS.md) · [Datasheet](../DATASHEET.md) · [Model card](../MODEL_CARD.md)
