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
| Full historical query evidence audit | [evidence_audit.py](../src/bbo/evidence_audit.py) |
| F1 coefficient fit and validation | [f1_reconstruction.py](../src/bbo/f1_reconstruction.py) |
| F7 positive Hartmann-6 check | [f7_reconstruction.py](../src/bbo/f7_reconstruction.py) |

## Recovered historical Round 12 source

The [four original 2 November analysis scripts](../journey/round_12/README.md#recovered-original-week-12-python-analysis) are now preserved verbatim, alongside portable working-directory copies and a checksum-verified archive of the original numerical transcripts and saved JSON results. They implement the actual Week 12 modelling study (GPs, PCA/kernel PCA, model ranking, Optuna TPE, input/output warping and trust-region Thompson sampling). The earlier notebook's later demonstration code is **not** a replacement for these historical scripts. See [the original round archive](../journey/round_12/README.md) for authentic evidence and execution limits.

## What the final notebook actually reproduces

The final walkthrough has three distinct evidence routes:

- **Historical decision audit:** verify each of the **104 personal portal inputs/outputs** against the eight function-specific decision ledgers. Follow links to surviving course-time scripts (for example, Round 2 UCB and Round 9 local fits). Some originals require course seed files not redistributed here; the notebook does **not** claim to regenerate all 104 choices.
- **Working optimisation examples:** run GP/EI, HEBO-inspired committee and a TuRBO-style candidate search using a historical data cutoff. These are **retrospective demonstrations of method mechanics**, not proven reproductions of the specific historical inputs submitted.
- **Mathematical investigations:** fit F1 from 10 initial observations and check 13 later returns; evaluate the positive Hartmann-6 F7 reconstruction against 43 recorded points; fit F8 from 40 initial observations and validate 13 later returns; evaluate F5 at the recorded boundary. Label prospective and retrospective evidence separately.

**Confirmed F7 R11 input:** `0.233000-0.128000-0.522000-0.276000-0.310000-0.667000`, score `3.278967926227992`. The original **selection script** is missing, **not the input**. [Authoritative verified facts](../docs/VERIFIED_FACTS.md).

## Separate post-capstone comparison

[Full HEBO and TuRBO-1 benchmark](../research/full_optimisers/README.md) uses a fitted F8 **simulator**, not new portal evaluations. It has different dependencies and instructions from the core notebook. Results should not be presented as historical capstone submissions.

## Finding original code

Each [round](../journey/README.md) links to surviving scripts, notes, inputs and outputs. Each [function story](../functions/README.md) points to the same evidence. No second set of historical code is maintained here.

[Model card](../MODEL_CARD.md) · [Dataset datasheet](../DATASHEET.md) · [Evidence rules](../docs/EVIDENCE_RULES.md)
