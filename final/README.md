# Final implementations and reproduction

[← Project overview](../README.md) · [Historical rounds](../journey/README.md) · [Methods](../methods/README.md)

This is the short route to running the **final documented analyses**. It does not replace the [original round-by-round record](../journey/README.md); some historical candidate-selection scripts are missing, and later code should not be attributed to earlier portal submissions.

## Start with the executable notebook

[**Capstone Final Walkthrough.ipynb**](../notebooks/Capstone_Final_Walkthrough.ipynb)

With Python 3.11 recommended, run from the repository root:

```bash
python -m pip install -r requirements-notebook.txt
python -m pytest -q
jupyter notebook notebooks/Capstone_Final_Walkthrough.ipynb
```

[Dependencies](../requirements-notebook.txt) · [Source-code guide](../src/bbo/README.md)

## Main source modules

| Component | File |
|---|---|
| GP surrogate modelling | [surrogates.py](../src/bbo/surrogates.py) |
| Acquisition functions | [acquisition.py](../src/bbo/acquisition.py) |
| Candidate search | [search.py](../src/bbo/search.py) |
| Historical HEBO-inspired and TuRBO-style adaptations | [optimizer.py](../src/bbo/optimizer.py) |
| F8 model reconstruction and F5 numerical validation | [structural_validation.py](../src/bbo/structural_validation.py) |

## Separate post-capstone comparison

[Full HEBO and TuRBO-1 benchmark](../research/full_optimisers/README.md) uses a fitted F8 **simulator**, not new portal evaluations. It has different dependencies and instructions from the core notebook. Results should not be presented as historical capstone submissions.

## Finding original code

Each [round](../journey/README.md) links to surviving scripts, notes, inputs and outputs. Each [function story](../functions/README.md) points to the same evidence. No second set of historical code is maintained here.

[Model card](../MODEL_CARD.md) · [Dataset datasheet](../DATASHEET.md) · [Evidence rules](../docs/EVIDENCE_RULES.md)
