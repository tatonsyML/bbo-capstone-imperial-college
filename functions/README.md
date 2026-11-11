# Explore the eight function stories

[← Project homepage](../README.md) · [Mathematical reconstructions](../reconstruction/README.md) · [Visual gallery](../visualisations/README.md) · [Historical archive](../journey/README.md) · [Complete data](../data/all_observations.csv)

**One function, thirteen decisions.** Start with the behaviour and final result, open any weekly section, then inspect the progress chart, original evidence, model code and 2D/3D visualisations. The weekly sections collapse by default so the page stays readable.

| Function | What to look for | Final best | First reached |
|---|---|---:|:---:|
| [F1 · Finding the signal](F1/README.md) | Near-zero outputs, target scaling, oscillatory reconstruction | **1.999999999676** | R11 |
| [F2 · When the forecast failed](F2/README.md) | EI/UCB evolution, miscalibration and competing regions | **0.744250426302** | R13 |
| [F3 · Brittle local peaks](F3/README.md) | Controlled local tests versus alternative regions | **−0.003753096919** | R13 |
| [F4 · Precise but unproductive](F4/README.md) | Tiny accurate steps and a later wider search | **0.746897911381** | R13 |
| [F5 · Towards the boundary](F5/README.md) | Controlled coordinate changes and later power-sum reconstruction | **8,662.405001** | R10 |
| [F6 · Unstable local behaviour](F6/README.md) | Failed predictions and regional changes | **−0.037518647244** | R12 |
| [F7 · From local to structural](F7/README.md) | One-coordinate path, alternative basin and Hartmann-6 forecast | **3.322368011393** | R12 |
| [F8 · Quadratic recovery](F8/README.md) | GP refinement, mathematical solution and held-out validation | **10.000000** | R10 |

[Evidence and editorial standards](../docs/EVIDENCE_RULES.md)

## How to read a round

Each expandable section separates the same five things:

**What was known → What was predicted → What was submitted → What was observed → What changed afterwards.**

Where a model hyperparameter, seed or exact selection script was not retained, it is described as **not retained**. The detailed [decision ledgers](F2/selection_history.csv), [historical code](../journey/README.md) and [279-row master dataset](../data/all_observations.csv) provide a numerical audit without requiring readers to navigate duplicate CSV files first.

## How to interpret the graphics

- **Progress:** best observed score after each round, including the initial supplied best.
- **F1:** original observed-point projections remain available. Separately labelled [reconstructed 2D/3D charts](F1/README.md#reconstructed-function-modelled-2d3d-views) show model predictions, not portal observations.
- **F2/F3/F4/F6:** scatter or 3D projections of observed points only; no invented continuous surfaces.
- **F5/F7/F8:** clearly labelled fixed-coordinate slices of reconstructed mathematical functions. Only two inputs vary in each slice.

[Graph descriptions and assumptions](../docs/functions.md) · [Rebuild graph source](../results/figures/build_visual_gallery.mjs)

The project history remains intact in [journey/](../journey/README.md). It is an evidence archive, **not** a second set of independently edited experimental results.
