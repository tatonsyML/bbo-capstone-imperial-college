# Round 6 · Module 17 | Model comparison and local path fitting

**Round summary:** Eight submitted inputs, eight measured results and the decisions behind them.

## My reasoning at the time

I returned to the distinction between importing a machine-learning idea and importing an unsuitable architecture. My inputs were tabular coordinates with no translation-invariant structure, so CNN layers would impose an assumption the data had not earned. The useful lesson from progressive feature extraction was a **hierarchy of evidence**: raw returns, controlled coordinate changes, local interactions, surrogate validation and only then the next query.

F7 helped make this concrete. Holding the other coordinates fixed while increasing x1 from **0.015000 to 0.046316 and 0.060000** had raised the output from roughly **1.5516 to 1.6138 and 1.6384**. The direction had survived a controlled test. My next step therefore pressed that coordinate further, rather than changing all six dimensions and forfeiting attribution. F6 offered the counterexample: a seemingly reasonable local extrapolation weakened when tested, reminding me that stable nearby patterns are not guaranteed.

I compared the GP with simpler and more flexible alternatives under five-fold validation. For F7, the GP's normalised RMSE was approximately **0.112** versus **0.314** for a small MLP; for F8, approximately **0.051** versus **0.157**. These checks favoured the GP in those measured comparisons, not as a universal theorem. More complexity and additional random initialisations were only worthwhile if held-out performance or a proposed experiment improved. A CNN was not a serious candidate for these unstructured vectors.

The contemporaneous technical note also explained my choice of tools and the need for modular, reproducible work. I wanted to separate the code that fits and diagnoses a surrogate from the decisions that spend a portal query; keep package assumptions and chronological data visible; and distinguish reviewed evidence from hypotheses suggested by reading or a model. I considered comparison with established optimisation and black-box benchmarks, including BoTorch and COCO/BBOB, as a future validation exercise rather than a completed historical benchmark. The practical lesson was to let research narrow the next experiment, not decorate a README.

## What I did

The surviving Module 17 comparison evaluates GP, ridge and small MLP prediction errors alongside controlled path fits.

## What happened

F2 → 0.69131487; F3 → -0.020856155; F5 → 4957.5717; F7 → 1.7006597; F8 → 9.8920726. That is 5 new personal bests in this round.

## What I learnt

F2 improved to 0.691315 and F3 to −0.020856, while F6 weakened. The value of an alternative model depends on its out-of-sample evidence, not complexity.

## How I approached this round

With five-fold validation after Round 5, I reported **GP vs small MLP normalised RMSE** of **0.112 vs 0.314** for F7 and **0.051 vs 0.157** for F8. F6's next controlled move contradicted a simple local extrapolation. I rejected convolutional models for these tabular coordinates and treated **held-out loss** as more reliable than complexity alone.


## Model comparison and implementation

The [Round 6 input choices](results/round6_queries.csv), [per-function rationale](results/round6_query_rationale.csv) and [modelling notebook](Capstone_BBO_Module17_Week6.ipynb) cover the GP, Ridge and small MLP comparisons. The notebook presents saved five-fold validation and controlled-coordinate results. CNNs were not used because the inputs have no image-like spatial structure.

## Inputs, results and code

| File | Purpose | Description |
|---|---|---|
| [queries.txt](queries.txt) | submitted input vector | Submitted input |
| [outputs.txt](outputs.txt) | returned output values | Measured score |
| [Capstone_BBO_Module17_Week6.ipynb](Capstone_BBO_Module17_Week6.ipynb) | notebook | archive, displays retained results |
| [results/model_comparison_round5.csv](results/model_comparison_round5.csv) | CSV | saved model comparison |
| [results/controlled_local_experiments.csv](results/controlled_local_experiments.csv) | CSV | saved controlled tests |
| [results/round6_queries.csv](results/round6_queries.csv) | CSV | saved query rationale |

[Complete data](../../data/all_observations.csv) · [Whole project journey](../README.md) · [Final reproducible notebook](../../notebooks/Capstone_Final_Walkthrough.ipynb)
