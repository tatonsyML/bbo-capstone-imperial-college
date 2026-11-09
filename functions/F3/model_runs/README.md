# Function 3: fitted GP replay (NOT historical selection code)

The original submitted inputs and actual scores remain in [selection_history.csv](../selection_history.csv). **No complete archive of original fitted GP parameters exists for every round.** This page explains how to fit a fresh model without leaking later portal outputs.

From the repository root, with `requirements.txt` installed, run:

```bash
python scripts/replay_surrogates.py --function 3 --round 9 --kernel Matern25 --acquisition EI --restarts 4 --seed 909
```

The code filters [the authoritative dataset](../../../data/all_observations.csv) to **earlier rounds only**. Its output reports the newly fitted kernel, ARD lengthscales, noise, training counts, a model prediction at the actual submitted point (if known), and a **new unscored counterfactual suggestion**.

The current replay assumptions are Matérn 2.5 + ARD + WhiteKernel, Yeo–Johnson transformed outputs, marginal-likelihood fitting with four restarts and Expected Improvement with ξ=0. You can compare RBF or Matérn 1.5, PI or UCB and alternative seeds. **None of these defaults is asserted as the historical choice for a given Round.**

The [related historical notes](../README.md) identify what original code survives. The complete HEBO / adaptive TuRBO reference algorithms were added only after the challenge.

[Shared replay script](../../../scripts/replay_surrogates.py) · [surrogate implementation](../../../src/bbo/surrogates.py) · [all functions](../../README.md).
