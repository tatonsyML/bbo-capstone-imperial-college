# Round 4 · Module 15 | Alternative models and controlled tests

**Record:** Eight submitted inputs and eight returned scores. The score values are observed. The explanatory notes below were compiled **retrospectively** from surviving records unless an original forecast is explicitly identified.

## My reasoning at the time

Round 3 made several earlier assumptions less comfortable. Some observations behaved *like* support vectors, in the informal sense that they marked sensitive regions, but they were not formal support vectors of the optimisation problem. F4 was a warning: a modest movement reduced a score from roughly **0.648 to 0.315**, while a controlled adjustment on F5 increased the score from **3,722 to 4,296**. I began treating observations close to a good/bad classification boundary as places worth investigating, not as fences around unknown territory.

I continued to regard the **Gaussian Process as my main optimisation surrogate** because it supplied both expected response and uncertainty. I compared logistic regression, linear and RBF support-vector classifiers and a small neural network as secondary diagnostics. I used the top part of the observed score distribution to construct good/bad labels, then compared models with cross-validation. The mistakes were asymmetric: a false positive wasted a query, but a false negative might hide an excellent region. I did not want an attractive classification score to override the objective values actually returned by the portal.

I also inspected **surrogate gradients** and repeated neural-network fits from different initialisations. I placed more trust in the *direction* of a gradient if its sign was stable and agreed with controlled observations. F7 provided a useful example. After a disappointing Round 2 response near **1.0204**, a controlled Round 3 refinement reached about **1.6138**. The possible influence of x1 and x6 was worth testing further, but one gradient estimate did not establish causality or global structure.

The neural network represented nonlinear behaviour unavailable to simple linear models, yet it did not consistently demonstrate enough predictive advantage to replace the GP. The SVM was useful for checking regions, and the neural network for local sensitivity, while the GP remained responsible for uncertainty-aware proposals. In parallel, I examined which hyperparameters were continuous, which were discrete and how much modelling effort each justified. The guiding question was whether changing a setting improved a later decision, not whether a more elaborate fit looked impressive. This was a **hybrid diagnostic workflow**, rather than a claim that three model families had been combined into one validated optimiser.

## What I did

The Module 15 notebook examines GP baselines alongside SVM and small neural-network diagnostics for selected functions.

## What happened

F3 → -0.031281597; F5 → 4694.3173; F6 → -0.54144783; F8 → 9.8754708. That is 4 new personal bests in this round.

## What I learnt

The F5 score increased through a controlled region change, while some apparently plausible proposals failed. Classification and model agreement were treated as diagnostics, not substitutes for returned scores.

## How I approached this round

I compared GP-led reasoning with logistic regression, linear/RBF SVM and a small neural network for **high-/low-performing classification**. I also examined **surrogate gradients**, including F7's sensitivity to x1 and x6. Classification was deliberately a *second opinion*: false negatives might exclude the best region, and classification scores did not replace measured function scores.


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
