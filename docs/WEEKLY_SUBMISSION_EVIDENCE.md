# Research decisions across thirteen rounds

[← Development journey](../journey/README.md) · [Eight functions](../functions/README.md) · [Evidence rules](EVIDENCE_RULES.md) · [Verified portal facts](VERIFIED_FACTS.md)

This overview traces how I approached eight unknown functions across thirteen rounds, linking my [experimental journey](../journey/README.md), [eight function investigations](../functions/README.md) and the original code and results that survive.

My recorded decisions, predictions, submitted inputs and results are distinguished throughout. A proposed experiment is not a measured result; the [portal record](../data/all_observations.csv) establishes the submitted inputs and returned scores. Later reconstructions are labelled separately.

## How the strategy evolved

| Round | What I investigated | What the evidence means |
|---:|---|---|
| [1](../journey/round_01/README.md) | Inspected the 175 supplied observations, chose eight function-specific queries using exploratory judgement and GP/EI **ideas**; no full Week 1 candidate-generator survives | The complete original candidate-generating script was not retained |
| [2](../journey/round_02/README.md) | Moved to a more consistent **GP/UCB** workflow. Documented \(\kappa\) settings: F1 **3.0**, F2 **2.5**, F3/F7 **2.0**, F4/F5/F6 **1.0**, F8 **1.5** | Link the surviving [Week 2 original code](../journey/round_02/week2_ucb_course_aligned.py); The UCB settings reflect the recorded approach, distinct from later model comparisons |
| [3](../journey/round_03/README.md) | Differentiated the search: F1 maximin, F2 global EI, F3 local GP predicted mean, F4–F8 local EI; described **501×501** grids in 2D, **300,000** random candidates at higher dimensions, 8 optimiser restarts, and EI margin = 1% observed-score SD | The original R3 candidate-generating script is not retained; SVM was considered as a supplementary filter rather than the main optimiser |
| [4](../journey/round_04/README.md) | Compared GP with logistic regression, linear/RBF SVM and a small NN as **classifiers/diagnostics**; examined surrogate gradients, including F7 x1/x6 | The [Module 15 code](../journey/round_04/capstone_bbo_week4_module15.py) illustrates the diagnostic work; classification is distinct from objective evaluation |
| [5](../journey/round_05/README.md) | Examined hierarchical reasoning for tabular inputs, not CNN feature maps; referred to F5's controlled R4 x2 change **0.970147 → 0.999999** and its score increase **4295.87 → 4694.32** | The F5 controlled test belongs to the prior round; a deep-learning analogy is not evidence that a CNN generated a query |
| [6](../journey/round_06/README.md) | Reported five-fold GP-versus-small-MLP comparison: F7 **0.112 vs 0.314** NRMSE and F8 **0.051 vs 0.157**; F6's controlled path contradicted a simple local extrapolation | The [Module 17 notebook](../journey/round_06/Capstone_BBO_Module17_Week6.ipynb) preserves the comparison results; the standalone fitting script has not survived |
| [7](../journey/round_07/README.md) | Tuned GP kernels, noise, restarts and local-search width; used **rolling-origin / next-return validation**; described large F2/F6 model misses and strong F8 prospective agreement | Rolling-origin validation was a test of forecast reliability; the exact standalone query-selection script is not retained |
| [8](../journey/round_08/README.md) | Recorded structured few-shot LLM assistance and **programmatic** input checks; Python and observations, not text generation, made the numerical decisions; F2's tiny coordinate move exposed a fragile local forecast | The retained source code and forecast audit distinguish LLM-assisted reasoning from programmatic candidate selection |
| [9](../journey/round_09/README.md) | Interpreted Week 8 forecast errors (F2 ~**0.69519 → 0.61309**, F3 ~**−0.01968 → −0.02966**), challenged diminishing returns assumptions, and justified query-budget discipline | The **Week 8 forecast misses** should not be confused with the separate **Week 9 F2 miss**, about 0.731 predicted versus 0.506 returned |
| [10](../journey/round_10/README.md) | Described lightweight HEBO-inspired committee and TuRBO-style fixed trust region **0.20**, with prospective F5 boundary and F8 quadratic-vertex hypotheses | The historical variants were **HEBO-inspired / TuRBO-style**, not complete library implementations; hypotheses were checked against later portal returns |
| [11](../journey/round_11/README.md) | **Explicitly reported applying DBSCAN** to 255 available own observations, Euclidean distance, `min_samples=3`, radius sensitivity; F1 had a five-point cluster with low scores and the best result outside it. Also reported contemporary F1/F8 structural checks | Clustering formed part of the Week 11 analysis. The [reproducible diagnostic and model overlay](../research/diagnostics/clustering/README.md) were assembled later, not authenticated as the original candidate generator |
| [12](../journey/round_12/README.md) | Evaluated F8 PCA on 52 recorded inputs: **48.8%** of variance explained by two PCs and **95.3%** by seven. The quadratic's modelled constrained maxima were **9.955973** (two PCs) and **9.999974** (seven), versus **10** with all inputs; reflected on F6/F7 gains and repeated queries | The [four Week 12 scripts](../journey/round_12/original/review_round12.py) document the modelling work. PCA variance is **not** the same as optimisation sensitivity |
| [13](../journey/round_13/README.md) | The reflection **_The trouble with the sixth decimal_** documents intended final-query reasoning, F4's failure of micro-refinement, feedback-based validation and one-step planning analogies | The final strategy considered a **distinct near-optimum F8 query**, but the **submitted R13 input repeated** the R10/R12 vertex. The portal record resolves the difference |

## The eight function investigations

Each [function narrative](../functions/README.md) connects the evolving strategy to the [279 recorded observations](../data/all_observations.csv), its decision history and surviving implementations.

| Function | How the strategy developed | What to keep in mind |
|---|---|---|
| [F1](../functions/F1/README.md) | Weeks 1–3 had almost no reliable signal; the Week 11 reflection discusses two oscillatory Gaussian peaks and a strong measured result | Week 11 account of a reconstruction ≠ the **later** 10-initial/13-return own-data Python fit |
| [F2](../functions/F2/README.md) | Week 8 local sensitivity, Week 9 discussion of forecast failure, Week 11 ridge change and Week 12 underperforming candidate | Differentiate an earlier forecast error from a later submitted candidate and its result |
| [F3](../functions/F3/README.md) | Cautious early exploitation, mixed GP/NN performance and alternative-region investigations | Modelled local peaks and external reports are not personal portal results |
| [F4](../functions/F4/README.md) | Week 4 classifier boundary evidence, Week 9 local accuracy, and the Week 11 wider move after millionth-size steps | **Prediction accuracy** and **achieved improvement** are separate quantities |
| [F5](../functions/F5/README.md) | Week 5 account of single-coordinate gains and Week 10 boundary hypothesis | The full power-sum equation was reconstructed later; the boundary score was actually measured |
| [F6](../functions/F6/README.md) | Week 6 model-vs-local disagreements, Week 7 fragile forecasts and original Week 12 robust selection work | Cross-cohort forecasts must not be relabelled personal returns |
| [F7](../functions/F7/README.md) | Controlled x1 path through Week 6, Week 11 multivariable move and the prospective structural R12 forecast | **R11 input and result are confirmed**, even though the original query-selection script is unavailable; see [verified facts](VERIFIED_FACTS.md) |
| [F8](../functions/F8/README.md) | Gradual GP-led improvements, Week 10 fitted-vertex decision and Week 12 PCA analysis | Week 12 PCA compression is an explanatory experiment, not evidence that two PCs locate the observed optimum |

## Reading the evidence

The [round pages](../journey/README.md) explain the decision-making in sequence. The [function pages](../functions/README.md) show what each line of investigation achieved. Numerical claims are grounded in the [portal data](../data/all_observations.csv); retrospective mathematical investigations and later benchmarks are identified as such.

Not every historical candidate-generation script survived. Where source code is missing, the narrative describes the documented method without implying that later demonstration code reproduces an original submission.
