# Reproduce GP model replays

The shared [replay script](../scripts/replay_surrogates.py) refits a Gaussian Process to observations recorded **before** a selected round, then reports its model diagnostics and a **new unscored counterfactual candidate**. It does not claim to reproduce the exact optimiser settings or proposal from that historical submission.

For any one of **F1–F8**, choose the function and round number. For example, for F1 before Round 9:

```bash
python scripts/replay_surrogates.py --function 1 --round 9 --kernel Matern25 --acquisition EI --restarts 4 --seed 909
```

Use `--function 2` through `--function 8` to repeat for the other functions. From the repository root, install `requirements.txt` first. Supported kernel choices are `RBF`, `Matern15` and `Matern25`; acquisitions are `EI`, `PI` and `UCB`.

Each run uses only earlier, complete input/output pairs from [all_observations.csv](../data/all_observations.csv). Its report includes fitted kernel parameters, ARD lengthscales, noise, training row count, a refitted prediction at the original submitted point, and a new candidate **without a portal score**. Default assumptions include Matérn 2.5 + ARD + WhiteKernel, Yeo–Johnson transformed scores, four restarts and EI with ξ=0. An inverse-transformed GP mean is not an exact posterior expectation.

For original submitted inputs and measured results, follow the [eight function investigations](../functions/README.md) and each function's `selection_history.csv`. For the implementation, see [surrogates.py](../src/bbo/surrogates.py) and [acquisition.py](../src/bbo/acquisition.py).

**These are reproducible diagnostic refits, not reconstructed original candidate-selection scripts.**
