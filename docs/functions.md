# Understanding the graphics

[← Project homepage](../README.md) · [Eight function stories](../functions/README.md)

Every [function page](../functions/README.md) displays three types of visual evidence: **measured score progression**, **a two-dimensional view**, and **a three-dimensional view**. The distinction between recorded measurements and model-generated values is central.

| Function | 2D/3D plot type | Axes and interpretation |
|---|---|---|
| [F1](../functions/F1/README.md) | **Observed points, plus separate reconstructed-model plots** | Original x1/x2 observed scores are preserved; additional model-only 2D/3D graphics zoom to [0.32, 0.74] to display both Gabor-type components |
| [F2](../functions/F2/README.md) | **Observed data only** | x1, x2 and measured score; no smooth function surface is implied |
| [F3](../functions/F3/README.md) | **Observed projection** | x1 and x2 are displayed; x3 differs between samples |
| [F4](../functions/F4/README.md) | **Observed projection** | x1 and x2 are displayed; x3 and x4 also vary |
| [F5](../functions/F5/README.md) | **Reconstructed-model slice** | x1 and x2 vary; x3=x4=0.999999; log1p(score) is used for visual scaling |
| [F6](../functions/F6/README.md) | **Observed projection** | x1 and x2 are displayed; x3–x5 differ between samples |
| [F7](../functions/F7/README.md) | **Positive Hartmann-6 model slice** | x1 and x2 vary; x3–x6 fixed at (0.476874,0.275332,0.311652,0.657301) |
| [F8](../functions/F8/README.md) | **Additive-quadratic model slice** | x3 and x8 vary; other six inputs fixed at their fitted vertex |

**Observed projection is not a smooth surface.** Where inputs have more than two dimensions, 3D visualisation cannot show the whole response without fixing or omitting dimensions. Models shown as slices are labelled **reconstructed mathematical hypotheses**, supported by numerical tests, not authenticated copies of the undisclosed source.

### Graph data and code

- [Observed inputs and outputs](../data/all_observations.csv) is the authoritative 279-row dataset.
- [Graph-generation script](../results/figures/build_visual_gallery.mjs) produces the 2D/3D gallery.
- Each `functions/F*/progress.svg` chart plots actual cumulative bests from the matching [selection history](../functions/F8/selection_history.csv), beginning with that function's supplied starting best.
- [F1 retrospective model and check](../src/bbo/f1_reconstruction.py) plus [modelled plot generator](../results/figures/build_f1_reconstruction.mjs) use no peer data. The new [F1 2D](../results/figures/f1_model_2d.svg) and [3D](../results/figures/f1_model_3d.svg) plots show predictions, not measurements.
- [F8 structural validation code](../src/bbo/structural_validation.py) tests the equation against observations withheld from its retrospective initial-40 fit.

The charts do not invent confidence percentages or turn modelled points into portal observations. For exact coordinates and scores, open each function's decision ledger.
