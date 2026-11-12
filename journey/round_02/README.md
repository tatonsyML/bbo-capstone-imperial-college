# Round 2 · Module 13 | UCB experiments and initial candidate selection

**Record:** Eight submitted inputs and eight returned scores. The score values are observed. The explanatory notes below were compiled **retrospectively** from surviving records unless an original forecast is explicitly identified.

> **About this account:** Edited from my Week 2 reflection in the 52-page *Capstone Project* document. It describes my thinking at the time. The technical record below preserves the confirmed portal returns, original artefacts and evidence limitations. Any difference between a prospective claim and a returned result must be resolved using the portal record.

## My reasoning at the time

I began this round by adding the eight returned Week 1 input-output pairs to the starting observations and refitting the surrogate models. My first round had relied heavily on different heuristics. Now I tried to use a more consistent computational rule: Gaussian Process prediction with an Upper Confidence Bound (UCB) acquisition function. I varied the exploration weight, κ, by function rather than assuming a single universal setting.

The first returns provided a useful challenge to my assumptions. F1 again produced essentially no signal, so I assigned the strongest exploration weight, **κ = 3.0**. I resisted the temptation to relabel the near-zero pattern a binary or sigmoid function. A later detection/non-detection classifier might have been useful, but the current observations would make it severely imbalanced. F2 returned **0.3791**, below its prior best of about **0.6112**: the midpoint did not establish the broad ridge I had hoped to find, so it retained a comparatively exploratory setting, **κ = 2.5**.

Other functions gave firmer grounds for exploitation. F4 improved from approximately **−4.0255 to −1.9105**, and F5 from **1,088.86 to 1,426.09**; I used **κ = 1.0** for each. F6's less-negative return also supported refining a direction while keeping possible coordinate interactions in mind. F8 improved from about **9.5985 to 9.8321** but still carried substantial eight-dimensional uncertainty, so **κ = 1.5** balanced its promising region with exploration. F3 and F7 retained intermediate settings, **κ = 2.0**.

The practical calculation differed by dimension. For two-input functions I examined UCB over a dense grid; for higher dimensions I used a reproducible random candidate pool of **300,000** points. That gave a tractable comparison without pretending to exhaust the search space. I treated feature-level trends as diagnostic checks rather than sufficient evidence to select a point, because the interaction among coordinates could matter more than any one input. This was a first attempt to impose a repeatable decision process, while allowing the observations to challenge its predictions.

## Verified results, methods and original evidence

## What I did

The Module 13 working material documents GP/UCB-based proposal selection, including a stronger uncertainty allowance on the difficult F2.

## What happened

F4 → 0.64755427; F5 → 3722.2745. That is 2 new personal bests in this round.

## What I learnt

F4 and F5 improved, while most other functions did not. A GP recommendation is only a hypothesis until the portal returns its value.

## How I approached this round

After receiving Week 1 returns, I moved from function-specific heuristics to a more consistent **GP/UCB** selection process. The recorded exploration weights were **κ = 3.0** (F1), **2.5** (F2), **2.0** (F3/F7), **1.0** (F4/F5/F6) and **1.5** (F8). Larger κ rewarded uncertainty; smaller values favoured promising incumbents. The original [working script](week2_ucb_course_aligned.py) survives separately.


## Source and limitations

The [Week 2 UCB notebook](Capstone_BBO_Week2_UCB_only.ipynb), [Python script](week2_ucb_course_aligned.py), [results CSV](week2_ucb_results.csv) and [archive ZIP](Module13_Round2_Original_Package.zip) preserve the working package assembled on 30 July 2026. It used Gaussian Processes, predicted mean and uncertainty, UCB and grid/random search. Original course `.npy` arrays are not included here; the [consolidated observations](../../data/all_observations.csv) are separate. The ZIP is retained as historical evidence rather than assumed expendable.

## Original files and evidence

| File | Purpose | Evidence status |
|---|---|---|
| [queries.txt](queries.txt) | submitted input vector | portal input, historical |
| [outputs.txt](outputs.txt) | returned output values | portal observation, historical |
| [Capstone_BBO_Week2_UCB_only.ipynb](Capstone_BBO_Week2_UCB_only.ipynb) | notebook | archived course-time work |
| [week2_ucb_course_aligned.py](week2_ucb_course_aligned.py) | Python script | archived course-time work |
| [week2_ucb_results.csv](week2_ucb_results.csv) | CSV | recorded output |
| [Module13_Round2_Original_Package.zip](Module13_Round2_Original_Package.zip) | original ZIP package | archive package |

[Complete data](../../data/all_observations.csv) · [Whole project journey](../README.md) · [Final reproducible notebook](../../notebooks/Capstone_Final_Walkthrough.ipynb)
