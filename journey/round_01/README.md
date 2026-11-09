# Round 1 · Module 12 | An initial GP and acquisition baseline

**Record:** Eight submitted inputs and eight returned scores. The score values are observed. The explanatory notes below were compiled **retrospectively** from surviving records unless an original forecast is explicitly identified.

## What I did

The first round established a Gaussian Process/acquisition baseline and tested one proposed setting per function.

## What happened

F4 → -1.9105442; F5 → 1426.0898; F6 → -0.60398063; F8 → 9.8321124. That is 4 new personal bests in this round.

## What I learnt

The returns did not support using the same exploration weight everywhere. F1 stayed near zero, while F5 and F8 showed much stronger signal.

## Source and limitations

Module 12 introduced Gaussian Process surrogates, prediction uncertainty and exploration versus exploitation. The original full Week 1 optimiser was not retained. The [Module 12.1 coursework notebook](supporting_coursework/Required_assignment_12_1_Tamer_ready.ipynb) is retained as supporting course work, not presented as the exact portal-selection script.

## Original files and evidence

| File | Purpose | Evidence status |
|---|---|---|
| [queries.txt](queries.txt) | submitted input vector | portal input, historical |
| [outputs.txt](outputs.txt) | returned output values | portal observation, historical |
| [supporting_coursework/Required_assignment_12_1_Tamer_ready.ipynb](supporting_coursework/Required_assignment_12_1_Tamer_ready.ipynb) | coursework notebook | original exercise artefact |

[Complete data](../../data/all_observations.csv) · [Whole project journey](../README.md) · [Final reproducible notebook](../../notebooks/Capstone_Final_Walkthrough.ipynb)
