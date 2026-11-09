# Component 25.3 | Instructor assessment guide

**One place to verify the full capstone:** project purpose, data, models, observed outcomes, limitations and executable evidence.

[← Project homepage](../README.md) · [Final notebook](../notebooks/Capstone_Final_Walkthrough.ipynb)

## Rubric map (five criteria, five points each)

| Requirement | File to assess | Verification |
|---|---|---|
| **Commented code, easy to run, results reproducible** | **[Final Jupyter notebook](../notebooks/Capstone_Final_Walkthrough.ipynb)**; [source code](../src/bbo/README.md); [tests](../tests/) | Run All and confirm 279 observations, eight bests, F8's 40/13 holdout, F5 boundary |
| **Complete datasheet** | **[Final datasheet](../DATASHEET.md)** | Origin, composition, collection, preparation, missing inputs, bias, permitted use and distribution |
| **Complete model card** | **[Final model card](../MODEL_CARD.md)** | GP assumptions, strategy evolution, results, quantitative validation, failure modes and maintenance |
| **Approximately 100-word explanation** | [README introduction](../README.md#the-project-in-about-100-words) | 105 words in clear general-audience English |
| **Well-organised repository and linked data** | [README](../README.md) · [279-row CSV](../data/all_observations.csv) · [visualisations](functions.md) · [assessment archive](../journey/README.md) | All current deliverables linked directly; historical documents separately indexed |

## How to reproduce

Clone the public repository, open a terminal in its root, and use a compatible Python environment (Python 3.11 recommended):

```bash
python -m pip install -r requirements-notebook.txt
python -m jupyter nbconvert --to notebook --execute notebooks/Capstone_Final_Walkthrough.ipynb --output Capstone_Final_Walkthrough_executed.ipynb
python -m pytest -q
python src/bbo/structural_validation.py
```

The source notebook finds the repository root from its working directory. The executed notebook contains the generated tables, plots and numerical checks. A [notebook execution workflow](https://github.com/tatonsyML/bbo-capstone-imperial-college/actions/workflows/notebook-25-3.yml) runs it on a clean GitHub runner and uploads an executed notebook artifact. The existing [core tests](https://github.com/tatonsyML/bbo-capstone-imperial-college/actions/workflows/core-tests.yml) independently verify code and structural results.

## What the assessor should know

- **279 observed outputs:** 175 supplied starting observations and 104 personally returned queries. [Data provenance](../DATASHEET.md).
- **One missing F7 input:** the Round 11 score is known; its input coordinates are unavailable and have not been guessed.
- **F8 validation:** 17-coefficient additive quadratic fitted to 40 initial observations; 13 later returns excluded from fitting. This experiment is retrospective.
- **F5 validation:** permitted boundary 0.999999 in each coordinate, rather than the mathematical 1.0 corner.
- **Not full hidden-source recovery:** F2/F3/F4/F6 have no confirmed closed-form reconstruction. F1 has incomplete historical reconstruction parameters.
- **HEBO/TuRBO:** adaptations were used during the capstone; the full reference-algorithm experiment was added afterwards and does not represent actual portal scores.
- **Course data rights:** initial binary files are not published, but numerical values are present in the CSV; permission should be checked.
- **Historical work:** early submission copies and notebooks remain in the archive but are not the entry point for Component 25.3.

**Review route:** 105-word explanation → final Jupyter notebook → final datasheet and model card → supporting code and experiment history.

[← Return to README](../README.md)
