# Round 3 · Module 14 | Function-specific acquisition choices

**Record:** Eight submitted inputs and eight returned scores. The score values are observed. The explanatory notes below were compiled **retrospectively** from surviving records unless an original forecast is explicitly identified.

> **About this account:** Edited from my Week 3 reflection in the 52-page *Capstone Project* document. It describes my thinking at the time. The technical record below preserves the confirmed portal returns, original artefacts and evidence limitations. Any difference between a prospective claim and a returned result must be resolved using the portal record.

## My reasoning at the time

By the third round, I had stopped believing that a common exploration policy deserved equal authority on every function. Earlier returns were uneven. F4 had moved from roughly **−4.03 to −1.91**, F5 from about **1,089 to 1,426**, and F8 from **9.60 to 9.83**, while F1 remained nearly flat and F2, F3 and F7 had failed to improve at different points. A Gaussian Process could report uncertainty confidently without supplying enough evidence that its proposed region was useful.

I therefore separated acquisition strategies by function. I used **maximin exploration for F1**, where detecting a non-zero response mattered more than polishing the present best; **global Expected Improvement for F2**; **local predicted-mean optimisation for F3**; and **local Expected Improvement for F4–F8**. My EI exploration margin was **1% of the standard deviation of observed outputs**. I used target normalisation and candidate searches appropriate to dimensionality, including dense grids in two dimensions and large, reproducible candidate pools elsewhere. These settings were recorded in my study notes, although the exact original generator is not preserved for this round.

I understood exploitation as an evidence-dependent choice, not the default objective. Promising regions in F4, F5, F6 and F8 merited attention, yet even there an excessively large local jump risked abandoning useful information. F1 still needed exploration; F2, F3 and F7 needed a mixture of local testing and alternatives. The limited query budget made indiscriminate exploration costly, while pure exploitation presumed that the current best region contained the global maximum.

I also investigated whether a Support Vector Machine could support the search. A soft-margin or RBF SVM might classify candidate inputs as promising or unpromising, particularly where response regions were curved. But **classification is not maximisation**, and an SVM supplies neither the continuous maximum nor the GP's uncertainty estimate. I considered it a secondary filter or challenge to the GP. False negatives would be especially costly if they excluded the best basin. The change in judgement was more significant than any particular model: I wanted a policy that could be defended function by function and revised after each new return.

## Verified results, methods and original evidence

## What I did

The study broadened function-specific acquisition choices, including Expected Improvement and continued comparisons of local versus wider candidates.

## What happened

F2 → 0.65386761; F5 → 4295.8677; F6 → -0.56977905; F7 → 1.6137963; F8 → 9.8634786. That is 5 new personal bests in this round.

## What I learnt

Five functions improved, but F1 and F4 did not. This suggested separate query policies by function instead of one global kernel/acquisition rule.

## How I approached this round

I stopped applying one acquisition rule to every function. I used **F1 maximin exploration, F2 global Expected Improvement, F3 local predicted-mean optimisation and F4–F8 local EI**. I evaluated **501 × 501** candidate grids for two-input functions, **300,000** random candidates for higher dimensions, **eight optimiser restarts** and an EI margin of **1% of observed-output standard deviation**. These settings are recorded in my contemporaneous notes; the exact candidate-generation script is not preserved. An SVM was considered as a **secondary classification filter**, not a substitute for the GP.


## Source and limitations

The Week 3 method settings are documented, but the exact standalone query-generating code is **not** preserved. The confirmed portal inputs and outputs remain separate from the method description.

## Original files and evidence

| File | Purpose | Evidence status |
|---|---|---|
| [queries.txt](queries.txt) | submitted input vector | portal input, historical |
| [outputs.txt](outputs.txt) | returned output values | portal observation, historical |

[Complete data](../../data/all_observations.csv) · [Whole project journey](../README.md) · [Final reproducible notebook](../../notebooks/Capstone_Final_Walkthrough.ipynb)
