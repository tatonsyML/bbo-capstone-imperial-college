# Round 1 · Module 12 | An initial GP and acquisition baseline

**Record:** Eight submitted inputs and eight returned scores. The score values are observed. The explanatory notes below were compiled **retrospectively** from surviving records unless an original forecast is explicitly identified.

> **About this account:** Edited from my Week 1 reflection in the 52-page *Capstone Project* document. It describes my thinking at the time. The technical record below preserves the confirmed portal returns, original artefacts and evidence limitations. Any difference between a prospective claim and a returned result must be resolved using the portal record.

## My reasoning at the time

I began with the supplied observations, not a known function or a gradient. The functions differed markedly: F1 and F2 had only ten initial observations each, while F8 had forty across eight dimensions. All submissions had to stay within the permitted input interval. I first identified the best observed points and asked what evidence justified the next expensive evaluation. I considered Gaussian-process predictions, uncertainty and Expected Improvement as decision ideas; I did not have evidence that a complete, reusable optimiser was already in place.

The main decision was **not to treat eight different surfaces as one problem**. Almost every F1 response was effectively zero. Local optimisation around a zero response would have been an unsupported assumption, so I chose a sparsely investigated region and treated signal detection as the immediate goal. F8 had the opposite difficulty: forty observations sounded relatively generous, but spread over eight inputs they provided sparse coverage. A broader probe was more defensible than claiming to have located its best neighbourhood.

F2's strongest starting observations shared a similar first coordinate while differing substantially on the second. I selected an intermediate point to test whether they represented one broad promising area or separate regions. For F3, where higher means closer to zero, I preferred cautious refinement near strong observations. F4 warranted a nearby but distinct perturbation. F5's apparent single-peak structure suggested following the stronger chemical-yield readings. In F6 I considered the directional pattern, especially a relatively high fourth coordinate and low fifth coordinate. For F7 I modified several coordinates around a strong configuration to investigate whether the favourable region continued.

These were hypotheses, not discoveries about the hidden equations. I planned to append each new input and return to the historical data, update the model, compare EI with UCB and change search scale when observations justified it. My operating principle was already taking shape: **a query should answer a specific question**, rather than add another number to the dataset.

## Verified results, methods and original evidence

## What I did

The first round analysed the supplied observations, tested one exploratory setting per function and used Gaussian Process/acquisition **ideas** to frame the trade-off. A fully executable original Week 1 candidate generator is not retained.

## What happened

F4 → -1.9105442; F5 → 1426.0898; F6 → -0.60398063; F8 → 9.8321124. That is 4 new personal bests in this round.

## What I learnt

The returns did not support using the same exploration weight everywhere. F1 stayed near zero, while F5 and F8 showed much stronger signal.

## How I approached this round

I began with the 175 supplied observations and chose a different exploratory question for each function, guided by observed bests, sparsely sampled regions and **GP/EI ideas**. F1 needed signal detection; F8 remained difficult because 40 starting points covered eight dimensions sparsely. The submission does **not** establish that a complete Python GP/acquisition candidate generator was executed or preserved for this round.


## Source and limitations

Module 12 introduced Gaussian Process surrogates, prediction uncertainty and exploration versus exploitation. The original full Week 1 optimiser was not retained. The [Module 12.1 coursework notebook](supporting_coursework/Required_assignment_12_1_Tamer_ready.ipynb) is retained as supporting course work, not presented as the exact portal-selection script.

**Notebook execution status:** The original supporting coursework notebook is an unexecuted historical snapshot. Its unexecuted cells are retained as source material; it is not presented as the exact Round 1 portal candidate generator.

## Original files and evidence

| File | Purpose | Evidence status |
|---|---|---|
| [queries.txt](queries.txt) | submitted input vector | portal input, historical |
| [outputs.txt](outputs.txt) | returned output values | portal observation, historical |
| [supporting_coursework/Required_assignment_12_1_Tamer_ready.ipynb](supporting_coursework/Required_assignment_12_1_Tamer_ready.ipynb) | coursework notebook | original exercise artefact |

[Complete data](../../data/all_observations.csv) · [Whole project journey](../README.md) · [Final reproducible notebook](../../notebooks/Capstone_Final_Walkthrough.ipynb)
