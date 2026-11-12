# Development journey | 13 returned rounds

[← Project homepage](../README.md) · [Eight function stories](../functions/README.md) · [Methods and experiments](../docs/methods.md) · [Final code](../notebooks/README.md)

This is my chronological account of thirteen rounds of experiments. Each round links the selected inputs, measured results, reasoning and relevant Python code. The function pages explain how the results changed the next decision.

**Numbering:** *Week* and *Round* refer to the same evaluation cycle (Week 1 = Round 1). *Module* refers to the course module covering that round. For example, Round 1 belongs to Module 12, and Round 13 belongs to Module 24. Labels such as **Module 21.2** identify an assessment component within a course module, not a separate optimisation round.

| Round | Module | Main method or question | Evidence and lesson | Source folder |
|---|---:|---|---|---|
| **1** | 12 | Initial exploration across 175 observations; GP/EI ideas | Model strength differed sharply by function | [Open R1](round_01/README.md) |
| **2** | 13 | GP/UCB with function-specific κ from 1.0 to 3.0 | F4/F5 improved; [original Python](round_02/week2_ucb_course_aligned.py) and [candidate records](round_02/week2_ucb_results.csv) | [Open R2](round_02/README.md) |
| **3** | 14 | F1 maximin, F2 global EI, F3 local GP mean, F4–F8 local EI; 501×501 2D grids and larger candidate pools | Five new personal bests; tune policy by function | [Open R3](round_03/README.md) |
| **4** | 15 | GP, logistic regression, SVM and small NN challengers | F5/F6/F8 improved; [historical Python](round_04/capstone_bbo_week4_module15.py) explores the diagnostics | [Open R4](round_04/README.md) |
| **5** | 16 | Controlled coordinate probes | Controlled moves helped but did not prove a maximum | [Open R5](round_05/README.md) |
| **6** | 17 | GP/MLP comparison with five-fold validation (F7 NRMSE 0.112 vs 0.314; F8 0.051 vs 0.157) | F2/F3 improved; [Module 17 notebook](round_06/Capstone_BBO_Module17_Week6.ipynb) | [Open R6](round_06/README.md) |
| **7** | 18 | ARD kernels, noise, restarts and rolling-origin forecast checks | F5/F7 improved; F1 remained negligible | [Open R7](round_07/README.md) |
| **8** | 19 | Prospective forecasts, LLM-assisted hypotheses and programmatic candidate checks | [Original Python](round_08/capstone_bbo_module19_round8.py) and [saved candidates](round_08/results/round8_queries.csv) | [Open R8](round_08/README.md) |
| **9** | 20 | Local polynomial fits and forecast errors | F2 forecast failed; F4 forecast was precise; [Python](round_09/round9_controlled_fits.py) and [forecast ledger](round_09/results/round9_queries.csv) | [Open R9](round_09/README.md) |
| **10** | 21 | F5 boundary, F8 quadratic, HEBO-inspired and TuRBO-style alternatives | F5 legal boundary and F8 fitted vertex returned the predicted regions; [saved candidates](round_10/round10_candidates.csv) | [Open R10](round_10/README.md) |
| **11** | 22 | DBSCAN (`min_samples=3`, radius sensitivity) alongside structural investigations | F1's five-point cluster missed its best score; F1 breakthrough and F2–F4 gains | [Open R11](round_11/README.md) |
| **12** | 23 | **GP ensembles, PCA/kernel PCA, Optuna TPE, warping and trust-region Thompson sampling** | Four Python implementations, candidate comparisons and new F6/F7 bests | [Open R12](round_12/README.md) |
| **13** | 24 | Final F2/F3/F4 gains | F2/F3/F4 improved again in final round | [Open R13](round_13/README.md) |

## How to read the results

The [master dataset](../data/all_observations.csv) contains **175 course-provided starting observations and 104 personally submitted portal returns**. A submitted point and its returned score are measured results; a proposed candidate or a GP forecast is not. The [function decision ledgers](../functions/README.md) distinguish inputs, actual outcomes and forecasts recorded before the corresponding results.

Later mathematical reconstructions and [post-capstone optimiser comparisons](../research/full_optimisers/README.md) are separate investigations. The F5 equation was developed after its Round 10 boundary decision; the F7 Hartmann-6 prediction preceded Round 12; the F8 quadratic predicted the Round 10 vertex, while its 40-initial/13-later holdout analysis was retrospective. Historical code is linked where preserved, without assuming every surviving script generated the precise submitted vector.

**A useful distinction:** A good model fit, a good forecast and a valuable next experiment are three different achievements.

## Code and experiment trail

The round pages contain the full learning narrative. For direct access to surviving implementations and their relevant outputs, use this shorter index.

| Rounds | Implementation or record | What it contributes |
|---|---|---|
| **1–3** | [Week 1 notebook](round_01/supporting_coursework/Required_assignment_12_1_Tamer_ready.ipynb) · [Round 2 GP/UCB](round_02/week2_ucb_course_aligned.py) | Initial exploration and original function-specific GP/UCB work |
| **4–6** | [Round 4 GP/SVM/NN Python](round_04/capstone_bbo_week4_module15.py) · [Round 6 comparison notebook](round_06/Capstone_BBO_Module17_Week6.ipynb) | Model challengers, controlled probes and cross-validation |
| **7–9** | [Round 8 Python](round_08/capstone_bbo_module19_round8.py) · [Round 8 forecasts](round_08/results/round8_queries.csv) · [Round 9 local fits](round_09/round9_controlled_fits.py) | Prospective forecasts, selected candidates and local sensitivity |
| **10–11** | [Round 10 candidate list](round_10/round10_candidates.csv) · [Week 11 clustering analysis](../research/diagnostics/clustering/README.md) | Alternative regions and structural hypotheses |
| **12–13** | [Round 12 original code](round_12/README.md#week-12-modelling-and-optimisation-code) · [Final inputs](round_13/queries.txt) · [Final returns](round_13/outputs.txt) | Robust model comparisons and final measured decisions |

Round 13's F8 reflection considered a distinct neighbouring point, but the final portal record shows an exact repeat of the Round 10 vertex. The measured record takes precedence over the intended experiment.

## Final reflection

[**When the Prediction Was Right but the Decision Was Wrong: Thirteen Rounds of Black-Box Optimisation**](final_reflection/README.md) draws together the strategy changes, final results, mathematical reconstructions and main lessons from all thirteen rounds.

For reproducible runs of the original weekly source using compatible published-data inputs, see the [historical script replay guide](../docs/historical_replay.md). This is separate from the original portal decisions.

## Original work and historical snapshots

- [Week 1–13 observed inputs and outputs](../data/all_observations.csv), including the confirmed F7 Round 11 coordinates.
- [Module 21.2 original assessed datasheet/model card/decision log](../archive/round_10/component_21_2/), preserved as historical evidence.
- [Module 21.1 original reflection](../archive/round_10/component_21_1/submission.md).
- [Stage 1 and missing component index](stage_1/README.md).

**Research evidence:** The portal history records actual evaluations. Later model reconstructions are distinguished from predictions made before the corresponding results.

[Main project](../README.md) · [Final reproducible notebook](../notebooks/Capstone_Final_Walkthrough.ipynb).
