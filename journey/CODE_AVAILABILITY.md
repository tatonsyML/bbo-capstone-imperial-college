# Historical Python and notebook availability

[← Project](../README.md) · [Function stories](../functions/README.md) · [Round archive](README.md)

**Observed inputs and outputs are complete; exact historical candidate-generating scripts are not.** All 104 function/round entries have confirmed inputs and returned scores. However, *none of the 104 decisions currently has a separately verified exact original selection script*. A linked analysis or notebook must not be treated as proof that it generated those coordinates.

| Round | Original or related code currently in this repository | Evidence status |
|---:|---|---|
| 1 | [Coursework notebook](round_01/supporting_coursework/Required_assignment_12_1_Tamer_ready.ipynb) | Related coursework; original selector not verified |
| 2 | [UCB Python](round_02/week2_ucb_course_aligned.py), [UCB notebook](round_02/Capstone_BBO_Week2_UCB_only.ipynb) | Related historical code; exact selector not verified |
| 3 | [Queries and outputs](round_03/README.md) only | No original script located in current repository |
| 4 | [Module 15 Python](round_04/capstone_bbo_week4_module15.py), [notebook](round_04/Capstone_BBO_Week4_Module15.ipynb) | Related historical model diagnostics |
| 5 | [Queries and outputs](round_05/README.md) only | No original script located |
| 6 | [Module 17 notebook](round_06/Capstone_BBO_Module17_Week6.ipynb) | Related analysis; complete original fitter not retained |
| 7 | [Queries and outputs](round_07/README.md) only | Round 8 audit code is **not** a Round 7 selector |
| 8 | [Module 19 Python](round_08/capstone_bbo_module19_round8.py) | Related historical analysis |
| 9 | [Controlled-fit Python](round_09/round9_controlled_fits.py) | Related historical analysis |
| 10 | [Exploratory](round_10/early_notebooks/exploratory_analysis.ipynb), [model-comparison](round_10/early_notebooks/model_comparison.ipynb), [optimisation-review](round_10/early_notebooks/optimisation_review.ipynb) notebooks and [shared optimiser](../src/bbo/optimizer.py) | Related or reconstructed implementation; not exact generator proof |
| 11 | [Actual round evidence](round_11/README.md), [verified queries](round_11/queries_verified_from_portal.txt) | Original selector unverified; additional clustering source exists in separately retained working files |
| 12 | [Actual round evidence](round_12/README.md), [verified queries](round_12/queries_verified_from_portal.txt) | Original selector not located in published tree |
| 13 | [Actual round evidence](round_13/README.md) | Original selector not located in published tree |

The saved decision ledgers classify **56 function/round entries with no code link** and **48 linked to related code or notebooks**. None is authenticated as the exact original candidate generator. These counts describe evidence in the current GitHub tree, **not** everything that might exist in separately stored working files.

## Distinguishing historical evidence from new reproductions

The [canonical observations](../data/all_observations.csv) contain 175 starting pairs and 104 real portal evaluations, including repeats. Round 11 and 12 query files were **compiled after the fact from the confirmed portal records**, not recovered as original candidate-selection text. F7 R11 was verified from the official results email, so its input is **not missing**.

The [retrospective GP replay](../scripts/replay_surrogates.py) fits an entirely new model from pre-round data. Its candidates are unscored counterfactuals, not the portal submissions. The shared [Python model modules](../src/bbo/README.md) explain algorithms but do not replace missing original per-week scripts.

## What remains to recover

Additional archived working packages were identified outside GitHub, including an October clustering script, an R7 documentation package, and retrospective Week 12 PCA analyses. The R7 package explicitly says it contains **no original R7 selector**; the Week 12 analyses are retrospective. Source code should only be added once its contents, runnable dependencies, intended round and provenance are confirmed. Do not manufacture scripts to fill an empty week.

[Evidence standards](../docs/EVIDENCE_RULES.md) · [Full chronological journey](README.md)
