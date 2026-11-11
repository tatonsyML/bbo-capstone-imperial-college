# Round 4 · Module 15 | Alternative models and controlled tests

**Record:** Eight submitted inputs and eight returned scores. The score values are observed. The explanatory notes below were compiled **retrospectively** from surviving records unless an original forecast is explicitly identified.

## What I did

The Module 15 notebook examines GP baselines alongside SVM and small neural-network diagnostics for selected functions.

## What happened

F3 → -0.031281597; F5 → 4694.3173; F6 → -0.54144783; F8 → 9.8754708. That is 4 new personal bests in this round.

## What I learnt

The F5 score increased through a controlled region change, while some apparently plausible proposals failed. Classification and model agreement were treated as diagnostics, not substitutes for returned scores.

## Original weekly submission perspective

**Original Week 4 submission perspective:** I compared GP-led reasoning with logistic regression, linear/RBF SVM and a small neural network for **high-/low-performing classification**. I also examined **surrogate gradients**, including F7's sensitivity to x1 and x6. Classification was deliberately a *second opinion*: false negatives might exclude the best region, and classification scores did not replace measured function scores.

*Source: the author's 52-page private `Capstone Project.docx` collection of weekly submissions, reviewed during the [13-week evidence reconciliation](../../docs/WEEKLY_SUBMISSION_EVIDENCE.md). The original document remains private. Its reflections support the historical reasoning but do not replace portal returns or missing original scripts.*

## Source and limitations

The [Module 15 notebook](Capstone_BBO_Week4_Module15.ipynb) and [Python analysis](capstone_bbo_week4_module15.py) preserve GP, classifier and small neural-network diagnostics. The earlier script expects programme-supplied `.npy` arrays and a `source_data/` folder absent from the public repository. Its [original package inventory](README_original.txt) describes the historical working folder, not the current clone.

## Original files and evidence

| File | Purpose | Evidence status |
|---|---|---|
| [queries.txt](queries.txt) | submitted input vector | portal input, historical |
| [outputs.txt](outputs.txt) | returned output values | portal observation, historical |
| [Capstone_BBO_Week4_Module15.ipynb](Capstone_BBO_Week4_Module15.ipynb) | notebook | historical with some saved outputs |
| [capstone_bbo_week4_module15.py](capstone_bbo_week4_module15.py) | Python script | historical, external dependencies |
| [README_original.txt](README_original.txt) | package inventory | historical text |

[Complete data](../../data/all_observations.csv) · [Whole project journey](../README.md) · [Final reproducible notebook](../../notebooks/Capstone_Final_Walkthrough.ipynb)
