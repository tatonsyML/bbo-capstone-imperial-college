# Round 6 · Module 17 | Model comparison and local path fitting

**Record:** Eight submitted inputs and eight returned scores. The score values are observed. The explanatory notes below were compiled **retrospectively** from surviving records unless an original forecast is explicitly identified.

## What I did

The surviving Module 17 comparison evaluates GP, ridge and small MLP prediction errors alongside controlled path fits.

## What happened

F2 → 0.69131487; F3 → -0.020856155; F5 → 4957.5717; F7 → 1.7006597; F8 → 9.8920726. That is 5 new personal bests in this round.

## What I learnt

F2 improved to 0.691315 and F3 to −0.020856, while F6 weakened. The value of an alternative model depends on its out-of-sample evidence, not complexity.

## How I approached this round

With five-fold validation after Round 5, I reported **GP vs small MLP normalised RMSE** of **0.112 vs 0.314** for F7 and **0.051 vs 0.157** for F8. F6's next controlled move contradicted a simple local extrapolation. I rejected convolutional models for these tabular coordinates and treated **held-out loss** as more reliable than complexity alone.


## Source and limitations

Surviving course-time work compares Ridge, a small one-layer MLP and a GP using five-fold validation; controlled paths often took priority over a globally smoothed model. CNNs were not used because the numeric coordinate vectors lack an image's translation structure. This archive came from the original Module 17 ZIP dated **3 September 2026**. The original standalone fitting script is missing; the [notebook](Capstone_BBO_Module17_Week6.ipynb) presents recorded CSV comparisons without claiming to rerun the missing code.

## Original files and evidence

| File | Purpose | Evidence status |
|---|---|---|
| [queries.txt](queries.txt) | submitted input vector | portal input, historical |
| [outputs.txt](outputs.txt) | returned output values | portal observation, historical |
| [Capstone_BBO_Module17_Week6.ipynb](Capstone_BBO_Module17_Week6.ipynb) | notebook | archive, displays retained results |
| [results/model_comparison_round5.csv](results/model_comparison_round5.csv) | CSV | saved model comparison |
| [results/controlled_local_experiments.csv](results/controlled_local_experiments.csv) | CSV | saved controlled tests |
| [results/round6_queries.csv](results/round6_queries.csv) | CSV | saved query rationale |

[Complete data](../../data/all_observations.csv) · [Whole project journey](../README.md) · [Final reproducible notebook](../../notebooks/Capstone_Final_Walkthrough.ipynb)
