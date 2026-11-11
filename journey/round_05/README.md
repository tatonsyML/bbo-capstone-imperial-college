# Round 5 · Module 16 | Controlled coordinate tests

**Record:** Eight submitted inputs and eight returned scores. The score values are observed. The explanatory notes below were compiled **retrospectively** from surviving records unless an original forecast is explicitly identified.

> **About this account:** Edited from my Week 5 reflection in the 52-page *Capstone Project* document. It describes my thinking at the time. The technical record below preserves the confirmed portal returns, original artefacts and evidence limitations. Any difference between a prospective claim and a returned result must be resolved using the portal record.

## My reasoning at the time

I used the idea of hierarchical feature learning to question my earlier tendency to treat every input coordinate as equally influential. Image networks progress from simple features to more complex patterns, but my BBO vectors are not images and have no natural spatial hierarchy. I did not introduce convolution merely to imitate a course topic. Instead I made the **analysis** hierarchical: individual inputs, controlled interactions, promising regions, model diagnostics and finally the query decision.

F5 supplied unusually direct evidence. In Round 4, changing **only x2 from 0.970147 to 0.999999**, with the other three inputs fixed, raised the output from approximately **4,295.87 to 4,694.32**. That controlled experiment was more useful than an untested assertion about feature importance. It supported the move towards the boundary, while leaving open the possibility of interactions or a different optimum elsewhere.

I contrasted this measured progress with less reliable explorations. A distant F1 probe found almost no useful signal. F4's sensitivity warned against assuming that any plausible local move would improve the score. The lesson I took from AlexNet and ImageNet was not to import an image architecture, but to understand how the interaction of method, data and computing resources affects performance. A sophisticated network is not necessarily an efficient or defensible use of a small, expensive black-box dataset.

I also began distinguishing a research prototype from a reproducible software project. A collection of notebooks was no longer enough to explain the process to another reader. My contemporary software-design notes proposed separating data, reusable modelling functions, candidate decisions and results, together with a record of why I changed direction. That was an **early design intention**, not a description of the repository's final directory structure. My standard for success broadened: the code should work, but the experiments and the reasoning behind each submitted point also needed to be auditable.

## Verified results, methods and original evidence

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
