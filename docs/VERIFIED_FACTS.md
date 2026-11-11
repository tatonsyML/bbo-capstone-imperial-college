# Verified capstone facts and consistency rules

[← Project home](../README.md) · [Final notebook](../notebooks/Capstone_Final_Walkthrough.ipynb) · [F7 evidence](../journey/round_11/README.md)

This is the **current canonical register** for numerical facts in the public repository. Historical submissions and dated snapshots are retained as evidence, but an older statement of missing information must **not override later source recovery**.

## Confirmed F7 Round 11 input (DO NOT REOPEN AS MISSING)

| Field | Authoritative value |
|---|---|
| Function | **F7**, six input dimensions |
| Round | **11** |
| Input | **`0.233000-0.128000-0.522000-0.276000-0.310000-0.667000`** |
| Returned score | **`3.278967926227992`** |
| Source | Official Round 11 programme results email, recovered after earlier incomplete local snapshots |
| Verification | [R11–12 portal CSV](../data/portal_rounds_11_12.csv), [canonical observations](../data/all_observations.csv), [F7 decision ledger](../functions/F7/selection_history.csv), [Round 11 page](../journey/round_11/README.md) |

**Only the exact original Round 11 candidate-selection script is unavailable. The submitted F7 input and returned score are fully known.** Do not conflate those facts.

The [automated evidence audit](../src/bbo/evidence_audit.py) checks this exact input and score in multiple files on every test run, alongside all 104 personal submissions. The [regression tests](../tests/test_verified_history.py) also scan active documentation and the final notebook for contradictory claims. Older working snapshots under `archive/` remain dated evidence rather than the current state.

## Other verified points

- Eight functions with input dimensions **2, 2, 3, 4, 4, 5, 6 and 8**.
- **279** recorded observations: **175** course-supplied initial records plus **104** personal portal evaluations (13 rounds × eight functions). Repeated queries remain counted.
- All 104 personal submissions have confirmed input vectors and actual portal returns. Every one matches the published per-function selection ledger.
- F1 best **1.9999999996761817**, first reached Round 11 at `0.628540-0.628540`.
- F5 best **8662.405001248297**, first reached Round 10 at four inputs of `0.999999`.
- F7 best **3.3223680113931557**, first reached Round 12. The positive Hartmann-6 hypothesis has a documented **pre-result** Round 12 prediction; evaluating it on all 43 known F7 rows is a subsequent retrospective consistency check, not proof that all coefficients were originally known.
- F8 best **10**, first reached Round 10 at `[0.10, 0.15, 0.13, 0.15, 0.80, 0.50, 0.20, 0.60]`.
- Some historic candidate-generating scripts are unavailable. Where a script survives but its exact relationship to one particular query is unverified, label it as **related historical code**, not the proven generator.
- The F1 two-component reconstruction is a later **own-data-only parameter fit** within a supplied model family; the family was recovered from separate working code, not independently discovered from ten observations.
- The F8 40-initial/13-later test is **retrospective**. Full official HEBO and BoTorch TuRBO-1 comparisons are **post-capstone** and use a fitted simulator, not portal outcomes.

## Publication consistency checklist

1. Use [the canonical observed CSV](../data/all_observations.csv) for numerical scores and inputs, never retype unknown values from memory.
2. Use the [eight function ledgers](../functions/README.md) and [round journey](../journey/README.md) to distinguish **what was known**, **what was submitted**, **what returned**, and **what was learnt later**.
3. Separate actual paid portal evaluations, hypothetical algorithmic suggestions, and reconstructed mathematical surface scores.
4. Keep historical source and later reproductions distinct. An accurate later model fit does not demonstrate which algorithm chose the original query.
5. Run `python -m pytest -q`, `python tests/check_internal_links.py` and the final notebook GitHub Actions workflow before merging changes to `main`.
