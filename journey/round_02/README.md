# Round 2 · Module 13 | UCB experiments and initial candidate selection

**Record:** Eight submitted inputs and eight returned scores. The score values are observed. The explanatory notes below were compiled **retrospectively** from surviving records unless an original forecast is explicitly identified.

## What I did

The Module 13 working material documents GP/UCB-based proposal selection, including a stronger uncertainty allowance on the difficult F2.

## What happened

F4 → 0.64755427; F5 → 3722.2745. That is 2 new personal bests in this round.

## What I learnt

F4 and F5 improved, while most other functions did not. A GP recommendation is only a hypothesis until the portal returns its value.

## Source and limitations

The [Week 2 UCB notebook](Capstone_BBO_Week2_UCB_only.ipynb), [Python script](week2_ucb_course_aligned.py), [results CSV](week2_ucb_results.csv) and [archive ZIP](Module13_Round2_Recovered_Package.zip) preserve the working package assembled on 30 July 2026. It used Gaussian Processes, predicted mean and uncertainty, UCB and grid/random search. Original course `.npy` arrays are not included here; the [consolidated observations](../../data/all_observations.csv) are separate. The ZIP is retained as historical evidence rather than assumed expendable.

## Original files and evidence

| File | Purpose | Evidence status |
|---|---|---|
| [queries.txt](queries.txt) | submitted input vector | portal input, historical |
| [outputs.txt](outputs.txt) | returned output values | portal observation, historical |
| [Capstone_BBO_Week2_UCB_only.ipynb](Capstone_BBO_Week2_UCB_only.ipynb) | notebook | archived course-time work |
| [week2_ucb_course_aligned.py](week2_ucb_course_aligned.py) | Python script | archived course-time work |
| [week2_ucb_results.csv](week2_ucb_results.csv) | CSV | recorded output |
| [Module13_Round2_Recovered_Package.zip](Module13_Round2_Recovered_Package.zip) | original ZIP package | archive package |

[Complete data](../../data/all_observations.csv) · [Whole project journey](../README.md) · [Final reproducible notebook](../../notebooks/Capstone_Final_Walkthrough.ipynb)
