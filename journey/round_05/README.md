# Round 5 · Module 16 | Controlled coordinate tests

**Record:** Eight submitted inputs and eight returned scores. The score values are observed. The explanatory notes below were compiled **retrospectively** from surviving records unless an original forecast is explicitly identified.

## What I did

This phase used controlled coordinate probes to check local sensitivity instead of only trusting a smooth GP surface.

## What happened

F2 → 0.65484987; F4 → 0.65892696; F5 → 4807.9861; F7 → 1.6384401; F8 → 9.8850021. That is 5 new personal bests in this round.

## What I learnt

F4 reached about 0.658927 while F5, F7 and F8 also improved. A local response pattern is useful, but not proof that a larger optimum has been found.

## How I approached this round

I distinguished genuine coordinate evidence from claims about deep neural-network feature hierarchies. For **Round 4 F5**, where increasing only **x2 from 0.970147 to 0.999999** while holding the other three coordinates fixed raised the score **4295.87 → 4694.32**. This controlled test informed my decisions; I did not treat the deep-learning analogy as proof that a CNN generated the next query.


## Source and limitations

My Week 5 analysis distinguishes measured, controlled experiments from conceptual neural-network analogies. The exact Week 5 candidate-selection script has not been retained; later explanations remain labelled retrospective.

## Original files and evidence

| File | Purpose | Evidence status |
|---|---|---|
| [queries.txt](queries.txt) | submitted input vector | portal input, historical |
| [outputs.txt](outputs.txt) | returned output values | portal observation, historical |

[Complete data](../../data/all_observations.csv) · [Whole project journey](../README.md) · [Final reproducible notebook](../../notebooks/Capstone_Final_Walkthrough.ipynb)
