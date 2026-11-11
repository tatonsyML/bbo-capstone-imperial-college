# Round 3 · Module 14 | Function-specific acquisition choices

**Record:** Eight submitted inputs and eight returned scores. The score values are observed. The explanatory notes below were compiled **retrospectively** from surviving records unless an original forecast is explicitly identified.

## What I did

The study broadened function-specific acquisition choices, including Expected Improvement and continued comparisons of local versus wider candidates.

## What happened

F2 → 0.65386761; F5 → 4295.8677; F6 → -0.56977905; F7 → 1.6137963; F8 → 9.8634786. That is 5 new personal bests in this round.

## What I learnt

Five functions improved, but F1 and F4 did not. This suggested separate query policies by function instead of one global kernel/acquisition rule.

## Original weekly submission perspective

**Original Week 3 submission perspective:** I stopped applying one acquisition rule to every function. The reflection documents **F1 maximin exploration, F2 global Expected Improvement, F3 local predicted-mean optimisation and F4–F8 local EI**. It describes **501 × 501** candidate grids for two-input functions, **300,000** random candidates for higher dimensions, **eight optimiser restarts** and an EI margin of **1% of observed-output standard deviation**. These are *reported historical method settings*, not proof that the exact original submission-generating script remains available. An SVM was considered as a **secondary classification filter**, not a substitute for the GP.

*Source: the author's 52-page private `Capstone Project.docx` collection of weekly submissions, reviewed during the [13-week evidence reconciliation](../../docs/WEEKLY_SUBMISSION_EVIDENCE.md). The original document remains private. Its reflections support the historical reasoning but do not replace portal returns or missing original scripts.*

## Source and limitations

The author's **Week 3 submitted discussion and method explanation survive** in the private 52-page Word collection. The exact standalone query-generating code has **not** been recovered. The portal record and method description are preserved separately, without claiming a script was reconstructed.

## Original files and evidence

| File | Purpose | Evidence status |
|---|---|---|
| [queries.txt](queries.txt) | submitted input vector | portal input, historical |
| [outputs.txt](outputs.txt) | returned output values | portal observation, historical |

[Complete data](../../data/all_observations.csv) · [Whole project journey](../README.md) · [Final reproducible notebook](../../notebooks/Capstone_Final_Walkthrough.ipynb)
