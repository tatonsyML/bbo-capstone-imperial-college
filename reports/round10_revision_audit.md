# Round 10 revision audit | Superseded models and selected portal inputs

**Prepared:** 18 October 2026  
**Evidence status:** Measured inputs/outputs through Week 9 only. Round 10 queries have been submitted and user-confirmed, but **scores remain pending**.  
**Purpose:** Explain what changed after additional experiments without rewriting the Week 1–9 history or turning forecasts into observations.

## 1. What changed?

| Function | Previous provisional candidate | Actual Round 10 submitted candidate | Why |
|---|---|---|---|
| F1 | 0.472784-0.455748 | **0.582552-0.558941** | Explore a positive-response neighbourhood suggested by external evidence |
| F3 | 0.325355-0.003391-0.538367 | **0.469634-0.620072-0.416672** | Test a different region suggested by Rishin's measured results; interpolation uncertain |
| F6 | 0.437642-0.275181-0.565494-0.833184-0.042658 | **0.379322-0.338275-0.586412-0.727790-0.036539** | Test a regional candidate with better peer-informed GP predictions |
| F7 | 0.223588-0.369270-0.256273-0.262985-0.391467-0.834089 | **0.190478-0.171014-0.347582-0.283057-0.283946-0.639922** | Test an alternative region rather than continue a nearly flat local refinement |

F2, F4, F5 and F8 retain the original working proposals. The complete submitted set is in [Round 10 queries](../experiments/round_10/queries.txt).

## 2. Evidence comparison, without treating predictions as portal scores

| Function | Comparison | Interpretation |
|---|---|---|
| F2 | Own Week 9 forecast **0.730502** versus returned **0.505526** | The earlier local GP overstated its accuracy |
| F4 | Own Week 9 forecast **0.658932869** versus returned **0.658932867** | The controlled local fit was exceptionally accurate |
| F5 | Tested additive cubic **RMSE 61.80** versus quadratic **1,033.44** on four later peer points | Polynomial degree matters; still a small, model-selected external test |
| F6 | Earlier proposal GP ensemble **−0.262**, revised proposal **−0.192** | Better **predicted** mean; model range approximately −0.249 to −0.151 |
| F7 | Earlier proposal GP ensemble **1.73**, revised proposal **2.79** | Better **predicted** mean; model range approximately 2.246 to 3.115 |
| F8 | Own-data additive quadratic predicts five later external observations at about **1.35e−10 RMSE** | Strong external corroboration of the fitted structure, not a portal-confirmed Round 10 result |

**F8 vertex:** 0.100000-0.150000-0.130000-0.150000-0.800000-0.500000-0.200000-0.600000, fitted score **10**.

The F5 all-upper-bound choice remains 0.999999 in each coordinate; its cubic model predicts approximately **8,489** there, but the real output has not been returned.

## 3. External evidence and provenance

Classmates' publicly shared records informed supplementary **experimental models** and helped reveal underexplored areas; they have **not** been counted as this participant's own portal observations.

- [Rishin Mitra, cumulative Week 10 records](https://github.com/mitrarishinoracleace/AIML/tree/main/data/accumulated/week10)
- [Andreia Bilé-Silva, input/output records](https://github.com/andreia-bs/Capstone-project)
- [Ugo Isiocha, F7 benchmark reported in model card](https://github.com/u-isiocha/Capstone/blob/main/docs/model-card.md)
- [Hilton Patel, F1 positive-response result in code](https://github.com/HP014/Machine-Learning-Capstone-Project)

**Data handling:** Only peer coordinates inside the legal 0.000000–0.999999 range entered the legal-input polynomial and GP comparisons. In particular, Andreia's F5 report at (1, 1, 1, 1) was excluded from those fits as **outside the course portal bounds**. The original reported value is evidence of a boundary trend, not a legal candidate.

**Validation design:** The experimental polynomial models included linear, additive quadratic, additive cubic and full quadratic feature sets with different regularisation values. GP comparisons varied RBF/Matérn kernels, length scales, fixed noise terms and target transformations. Retrospective tests held out the author's Weeks 6–9 or later peer observations, as applicable.

**Crucial limitation:** Hyperparameters were compared and selected using small holdouts, and the external query histories are themselves adaptively generated. Those best-in-grid RMSE figures are **exploratory selection statistics**, not independently estimated deployment error. Peer improvements on different runs need not be directly comparable to this participant's scores without confirming identical evaluation conditions.

**Academic-use note:** Public accessibility is not consent for unrestricted assessed use. The participant must comply with programme collaboration and attribution rules when applying peer-observed outputs to assessed query design.

## 4. Reproducibility status

The authoritative personal observation CSV files, main GP/acquisition code and Round 10 submitted inputs are in this repository. This audit captures the supplementary parameter families, source records, predictions and chosen coordinates. The detailed ad-hoc external test scripts were developed separately from the versioned project pipeline; the **exact supplementary analysis is not yet fully reproducible from this repository alone**. Any future publication should add the tested script revisions, dependencies, seeds and peer data download instructions under permitted terms.

This document makes no claim that F3, F6, F7 or F8 achieved the forecast scores; only new portal outputs can establish that.
