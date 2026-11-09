# Eight functions: a reader's guide

Each card uses **portal-observed best through Round 13**. An equation or diagnostic described below is not necessarily the method used to propose the successful input. See the [2D/3D visual gallery](visual_gallery.md), [provenance](evidence_provenance.md) and [reconstruction evidence](structural_reconstruction.md).

| Function | Best verified | First achieved | Central problem | Visuals |
|---|---:|---:|---|---|
| F1 | 1.999999999676 | R11 | Near-zero signal hid sharp structure | [2D](../results/figures/f1_2d.svg) · [3D](../results/figures/f1_3d.svg) |
| F2 | **0.744250** | **R13** | Local forecasts could fail severely | [2D](../results/figures/f2_2d.svg) · [3D](../results/figures/f2_3d.svg) |
| F3 | **−0.003753** | **R13** | Negative-valued response and difficult search | [2D](../results/figures/f3_2d.svg) · [3D](../results/figures/f3_3d.svg) |
| F4 | **0.746898** | **R13** | Accurate local prediction did not imply adequate search | [2D](../results/figures/f4_2d.svg) · [3D](../results/figures/f4_3d.svg) |
| F5 | 8,662.405 | R10 | Feasible boundary was more productive than local interior | [2D](../results/figures/f5_2d.svg) · [3D](../results/figures/f5_3d.svg) |
| F6 | −0.037519 | R12 | Weak models required fresh candidate regions | [2D](../results/figures/f6_2d.svg) · [3D](../results/figures/f6_3d.svg) |
| F7 | 3.322368 | R12 | Structural, prospective prediction succeeded | [2D](../results/figures/f7_2d.svg) · [3D](../results/figures/f7_3d.svg) |
| F8 | 10.000000 | R10 | Simple quadratic explained an 8D objective | [2D](../results/figures/f8_2d.svg) · [3D](../results/figures/f8_3d.svg) |

## F1 — Finding a narrow signal

**Best observed:** `1.9999999996761817` in R11 at `0.628540-0.628540`.

The GP initially saw almost no useful differences among near-zero outputs. A later reconstruction of Gaussian-modulated oscillatory responses helped identify a much stronger region. This mathematical reconstruction used supplementary information and is **not claimed to be inferred from personal queries alone**.

**Lesson:** reconsider the target scale and representation before spending further queries rescuing a poor fit.

## F2 — An unreliable local forecast

**Best observed:** `0.7442504263021256` in R13 at `0.864900-0.500000`.

A recorded forecast of `0.730502` returned only `0.505526`. This is a serious observed error at that location, but insufficient alone to diagnose the noise process. R13's different input region improved the earlier incumbent of `0.6953368270741286`.

**Lesson:** check forecasts against later returns; model authority depends on predictive performance.

## F3 — Improving a negative-valued objective

**Best observed:** `-0.0037530969187192596` in R13 at `0.197280-0.523429-0.470094`.

Several early search attempts underperformed. External published observations were considered separately from personal data when investigating alternative regions. The final score improved on R11's `-0.005709220275560069`. No exact F3 equation has been verified.

**Lesson:** a model's plausible extrapolation is not a substitute for returned evidence.

## F4 — Accurate prediction, poor search

**Best observed:** `0.7468979113807426` in R13 at `0.416903-0.415704-0.360320-0.415205`.

One local forecast was accurate to approximately `1.6e-9`, but a series of tiny steps achieved only marginal gains around `0.659`. A wider R11 proposal returned `0.7304594213260924`; R13 refined the result to `0.7468979113807426`.

**Lesson:** predictive success at one point does **not** validate the search policy or the neighbourhood it explores.

## F5 — The feasible boundary

**Best observed:** `8662.405001248297` in R10 at four coordinates of `0.999999`.

A controlled probe increasing one coordinate improved the return from about `4295.87` to `4694.32`. Later, the permitted upper corner was tested and produced a major gain. The interacting power-sum equation was reconstructed **after** that successful query.

At `(1,1,1,1)` the reconstructed equation predicts `8662.4825`, but the effective permitted portal upper bound is `0.999999`, yielding `8662.405001248297`.

**Lesson:** evaluate promising legal boundaries, and distinguish retrospective explanation from prospective query selection.

## F6 — Challenging unstable local models

**Best observed:** `-0.03751864724436928` in R12 at `0.415080-0.344119-0.644062-0.776818-0.076258`.

Earlier local forecasts and proposals were weak. An externally informed supplementary GP comparison contributed to a revised R10 candidate; subsequent local work improved the return in R11 and R12. F6's underlying equation remains unverified.

**Final check:** R13's `-0.07698028695699928` fell below the R12 best `-0.03751864724436928`.

**Lesson:** let sustained failure trigger alternative regions or models, without inventing a solved structure.

## F7 — A structural forecast confirmed

**Best observed:** `3.3223680113931557` in R12 at `0.201689-0.150011-0.476874-0.275332-0.311652-0.657301`.

The best after R9 was `1.786338`. A revised R10 candidate returned `3.149459`; the R11 result was `3.27896792623`; and the R12 portal result matched a **pre-recorded positive Hartmann-6 prediction** of `3.32236801`.

**Known gap:** the exact R11 F7 input coordinate was not preserved in the retained source. This does not invalidate the output, but prevents precise reproduction of that query.

**Final check:** R13 shifted x1 from `0.201689` to `0.201690`, returning `3.322368011392718`, approximately `4.38 × 10⁻¹³` below the R12 value.

**Lesson:** a prospective structural forecast provides stronger evidence than post-hoc fitting.

## F8 — The 17-coefficient quadratic

**Best observed:** `10` in R10 at `0.100000-0.150000-0.130000-0.150000-0.800000-0.500000-0.200000-0.600000`.

An additive quadratic with eight linear, eight squared and one constant coefficient fitted the response and identified this vertex. Five publicly shared outputs supported the model before the R10 query; they were not counted as personal queries.

**Retrospective check:** fitted to only the original **40 observations**, the same model structure predicted **13 later returned scores** to floating-point precision. This analysis was performed later, not in R1. A two-component PCA captured **48.8% of the input variance** but did not preserve the modelled optimum.

**Lesson:** when a simple interpretable model predicts unseen observations, it may be more useful than further acquisition tuning.

---

[Visual gallery and evidence status](visual_gallery.md) · [Final results CSV](../results/current_best_after_week13.csv) · [R13 evidence](round13_evidence.md) · [Forecast and portal evidence](round12_evidence.md) · [Reproducible mathematical checks](reproduce.md) · [Return to project overview](../README.md)
