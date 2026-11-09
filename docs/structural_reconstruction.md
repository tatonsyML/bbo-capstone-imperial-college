# Structural reconstruction: equations, chronology and limits

These are numerically supported explanations of hidden functions, **not authenticated source code**. F1, F5, F7 and F8 have strong reconstructed forms; F2, F3, F4 and F6 remain unresolved or approximate.

## F8: additive quadratic

f8(x) = 10 - Σ[j=1..8] w[j] (x[j] - c[j])²

**c** = (0.10, 0.15, 0.13, 0.15, 0.80, 0.50, 0.20, 0.60)

**w** = (2, 1, 3, 1, 0.5, 1, 2, 0.1)

An additive eight-variable quadratic has 17 linear regression coefficients: a constant, eight linear terms and eight squared terms. Since all weights are positive, the fitted equation's unique maximum on the legal domain is **10** at c.

**Chronology:** A model was fitted using accumulated personal records and corroborated with five public external input-output records before submitting the predicted vertex in Round 10; the portal confirmed 10. *Retrospectively*, refitting the same structure on only the **original 40 course observations** predicted the 13 later personal returns with maximum absolute error below **2e-15**. This did not happen before Round 1.

**Reproduce:** run PYTHONPATH=src python -m bbo.structural_validation with the [53-row evidence file](../data/accumulated/function_8/observations_through_week13.csv). The code fits with the initial records only and reports held-out residuals.

## F5: interacting power-sum equation

f5(x) = 0.01 × Σ[k=1..4] (Σ[j=1..4] (4 × x[j])^k - b[k])²,

where b = (7.5, 16, 40, 120). Squared power sums introduce interactions between coordinates. At the *permitted* upper corner x=(0.999999,0.999999,0.999999,0.999999), the equation produces **8662.405001248297**, matching the returned portal result. The complete equation was reconstructed **after** the successful boundary query using additional published observations; it explained, but did not generate, that choice.

## F7: positive Hartmann-6

The [Hartmann-6 benchmark reference](https://www.sfu.ca/~ssurjano/hart6.html) describes the conventional minimisation form; the reconstructed response uses its sign-reversed positive maximisation form. Its benchmark coefficients are documented in the [reproducible figure script](../scripts/build_visual_gallery.mjs).

The function agrees numerically with the positive Hartmann-6 benchmark in the tested observations. The Round 12 structural candidate predicted **3.32236801 before evaluation**; the portal returned **3.3223680113931557**. The R13 query shifted x1 by 0.000001 and returned 3.322368011392718, approximately 4.38 × 10⁻¹³ below the R12 result. This is supported prediction and numerical agreement, not proof of identity everywhere.

## F1: Gaussian-modulated oscillations

A numerically validated oscillatory response with two narrow, Gaussian-modulated peaks guided a Round 11 query to (0.628540, 0.628540), returning **1.9999999996761817**. This wider reconstruction used supplementary published information or recognised benchmark patterns. It is not claimed as independently inferred from personal portal queries alone.

## Unresolved objectives and reproducibility scope

F2 and F3 have unstable regions and unverified structural alternatives; F4 remains model-disagreement-sensitive; F6 has imperfect approximate fits. None is labelled mathematically solved.

**Executable in this repository:** F8's initial-data-only fit and 13-return check, plus F5's boundary equation check. The historical fitting procedures for F1/F5/F7 are documented findings, not claimed to be wholly reproducible from this newly added script. The types and roles of external research are documented in the [anonymised Round 10 revision audit](../reports/round10_revision_audit.md); identifying source references should be retained separately for authorised attribution.

## Visualisation scope

[See the full 2D/3D gallery](visual_gallery.md). F5, F7 and F8 are calculated **model slices** with all other coordinates fixed. For F1, the full fitted oscillatory coefficients are not publicly retained: the charts show observed points instead. F2/F3/F4/F6 similarly show only measured evidence, not invented model surfaces. The [figure generator](../scripts/build_visual_gallery.mjs) includes the standard positive Hartmann-6 numerical coefficients and validates the F7 R12 score.
