# Run original weekly scripts with an isolated data adapter

[← Research journey](../journey/README.md) · [Final notebook](../notebooks/README.md)

The original Round 2, Round 4, Round 8 and Round 9 Python source is retained **unchanged** under `journey/round_XX/`. Some of those scripts expect source ZIP files and NumPy arrays that are not included in the public repository.

The helper [`historical_replay.py`](../scripts/historical_replay.py) prepares input containers from the [279-row dataset](../data/all_observations.csv), places each historical script in a separate working directory and supplies the observations appropriate to the selected round.

From the repository root, using the Python dependencies in `requirements.txt`:

```bash
python scripts/historical_replay.py --round 2
python scripts/historical_replay.py --round 4
python scripts/historical_replay.py --round 8
python scripts/historical_replay.py --round 9
```

These commands **prepare only**. To run the original code in a fresh workspace, use for example:

```bash
python scripts/historical_replay.py --round 8 --workdir results/historical_replays/r8_example --execute
```

R2 runs a global GP/UCB candidate search and R4 performs substantial neural-network cross-validation. Both are computationally intensive, so execute them only when you need the detailed results. R8 refits the historical GP checks; R9 runs lightweight controlled polynomial fits. The helper refuses to overwrite an existing populated workspace.

Results depend on the Python environment and random-state settings. For the actual submitted points, consult each function's [decision history](../functions/README.md). Round 12 has its own [runnable analysis](../journey/round_12/README.md#run-the-analysis).

For a lightweight, guaranteed chronological retrospective GP demonstration across any of the eight functions and all 13 decision rounds, see [`replay_surrogates.py`](../scripts/replay_surrogates.py).
