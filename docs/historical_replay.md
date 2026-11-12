# Run original weekly scripts with an isolated data adapter

[← Research journey](../journey/README.md) · [Final notebook](../notebooks/README.md)

The original Round 2, Round 4, Round 8 and Round 9 Python source is retained **unchanged** under `journey/round_XX/`. Some of those scripts expect source ZIP files and NumPy arrays that are not included in the public repository.

The helper [`historical_replay.py`](../scripts/historical_replay.py) builds **compatible input containers from the verified 279-row CSV**, copies the historical script *byte-for-byte* to a separate working directory and records the source SHA-256 and the published submitted vectors for comparison. It never inserts future portal scores into the original modelling scripts.

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

**Interpretation:** Matching original results requires more than matching inputs. Numerical-library versions, external data and historical random states can differ. Reconstructed input ZIPs are derived from published numerical rows, **not byte-identical copies of the programme's original ZIP files**. A successful execution supports the method and its reproducibility, but does not establish that a generated point was the exact historical selector for the submitted portal vector. The latter is recorded separately in each function's selection ledger. Round 12 already has its own [portable original-analysis workflow](../journey/round_12/README.md#run-the-analysis).

For a lightweight, guaranteed chronological retrospective GP demonstration across any of the eight functions and all 13 decision rounds, see [`replay_surrogates.py`](../scripts/replay_surrogates.py).
