# Development journey | 13 returned rounds

[← Project homepage](../README.md) · [Eight function stories](../functions/README.md) · [Research decisions by round](../docs/WEEKLY_SUBMISSION_EVIDENCE.md) · [Methods and experiments](../docs/methods.md) · [Final code](../notebooks/README.md)

This is the chronological record of my thirteen-round optimisation project. Each round draws on my research notes and links the submitted inputs, observed results and surviving code. The [week-by-week research summary](../docs/WEEKLY_SUBMISSION_EVIDENCE.md) traces changes in strategy. Later mathematical reconstructions are identified separately from forecasts recorded before portal returns.

**Numbering:** *Week* and *Round* refer to the same evaluation cycle (Week 1 = Round 1). *Module* refers to the course module covering that round. For example, Round 1 belongs to Module 12, and Round 13 belongs to Module 24. Labels such as **Module 21.2** identify an assessment component within a course module, not a separate optimisation round.

| Round | Module | Main method or question | Evidence and lesson | Source folder |
|---|---:|---|---|---|
| **1** | 12 | Initial GP/acquisition baseline | Model strength differed sharply by function | [Open R1](round_01/README.md) |
| **2** | 13 | UCB experiments and uncertainty checks | F4/F5 improved; GP proposals still needed portal checks | [Open R2](round_02/README.md) |
| **3** | 14 | Function-specific acquisition and search | Five new personal bests; tune policy by function | [Open R3](round_03/README.md) |
| **4** | 15 | GP, classification and small NN challengers | F5/F6/F8 records improved; hybrids remained diagnostics | [Open R4](round_04/README.md) |
| **5** | 16 | Controlled coordinate probes | Controlled moves helped but did not prove a maximum | [Open R5](round_05/README.md) |
| **6** | 17 | Ridge/MLP/GP comparisons | F2/F3 improved; model complexity needed validation | [Open R6](round_06/README.md) |
| **7** | 18 | ARD kernel and forecast checks | F5/F7 improved; F1 signal remained negligible | [Open R7](round_07/README.md) |
| **8** | 19 | Prospective forecasts and adaptive experiments | Forecast hypotheses prepared before results | [Open R8](round_08/README.md) |
| **9** | 20 | Forecast error versus search region | F2 forecast failed; F4 forecast was locally precise | [Open R9](round_09/README.md) |
| **10** | 21 | Boundary and quadratic structural tests | F5 legal boundary and F8 fitted vertex verified | [Open R10](round_10/README.md) |
| **11** | 22 | **Contemporary DBSCAN analysis**, F1 and F2–F4 gains | Five-point F1 cluster did not contain best observed score; F1 breakthrough and F2–F4 new bests | [Open R11](round_11/README.md) |
| **12** | 23 | **GP ensembles, PCA/kernel PCA, Optuna TPE, warping and trust-region Thompson sampling** | Four Python implementations, candidate comparisons and new F6/F7 bests | [Open R12](round_12/README.md) |
| **13** | 24 | Final F2/F3/F4 gains | F2/F3/F4 improved again in final round | [Open R13](round_13/README.md) |

## Final reflection

[**When the Prediction Was Right but the Decision Was Wrong: Thirteen Rounds of Black-Box Optimisation**](final_reflection/README.md) draws together the strategy changes, final results, mathematical reconstructions and main lessons from all thirteen rounds.

For reproducible runs of the original weekly source using compatible published-data inputs, see the [historical script replay guide](../docs/historical_replay.md). This is separate from the original portal decisions.

## Original work and historical snapshots

- [Week 1–13 observed inputs and outputs](../data/all_observations.csv), including the confirmed F7 Round 11 coordinates.
- [Module 21.2 original assessed datasheet/model card/decision log](round_10/archive/component_21_2/), preserved as historical evidence.
- [Module 21.1 original reflection](round_10/archive/component_21_1/submission.md).
- [Stage 1 and missing component index](stage_1/README.md).

**Research evidence:** The portal history records actual evaluations. Later model reconstructions are distinguished from predictions made before the corresponding results.

[Main project](../README.md) · [Final reproducible notebook](../notebooks/Capstone_Final_Walkthrough.ipynb).
