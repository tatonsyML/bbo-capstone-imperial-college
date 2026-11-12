# Function-specific Datasheets | Black-Box Optimisation

[← Main dataset datasheet](../DATASHEET.md) · [Function investigations](../functions/README.md) · [Original observations](../data/all_observations.csv) · [Model card](../MODEL_CARD.md)

These concise function-specific records answer the seven sections of the **Imperial College London Module 25 datasheet template**. They complement the [main datasheet](../DATASHEET.md) and the expanded thirteen-round narratives rather than duplicating every query.

**Meaning and setting.** F1–F8 are numerical black-box objectives from a course exercise. The published evidence does not establish an individual real-world scenario or physical unit for any function. Examples below are **applications by analogy**, not verified descriptions of what Imperial College simulated. In every case the aim was to maximise the scalar score, not to minimise its magnitude.

**Data and evaluation rules.** For each Fk the programme supplied an initial NumPy input array of shape `(n, d)` and an output array of shape `(n,)`, with `n` and `d` listed below. The inputs are continuous numerical coordinates. The author made **one additional portal evaluation per function in each of thirteen rounds**; therefore each function has `n + 13` recorded observations. The permitted submitted coordinates have six decimal places and lie between 0 and 0.999999. The published CSVs keep original numeric responses, preserve repeated evaluations and do not delete outliers. Unused dimensions remain blank.

**Noise and confidence.** A GP's fitted noise parameter does not prove that the hidden function is random. Exact-query repeats, where available, provide *local repeatability* evidence only. The course did not reveal each hidden equation or a certified global bound. Personal best scores are measured results; derived optima and reconstructed surfaces are labelled separately.

**Shared preprocessing and modelling.** No categoricals need encoding. GP experiments considered RBF and Matérn kernels, ARD lengthscales, output transforms such as Yeo–Johnson or signed log, noise assumptions and acquisition parameters. These model-specific operations do not change the source observations. Detailed methods and any saved settings are in the [methods guide](methods.md), [chronological journey](../journey/README.md) and function ledgers. Missing parameters are not invented.

---

## Function 1

[Full F1 research story](../functions/F1/README.md) · [Measured progress](../functions/F1/progress.svg) · [Observations](../functions/F1/observations.csv) · [Decision ledger](../functions/F1/selection_history.csv)

- **Function overview:** F1 is a 2-dimensional numerical optimisation objective (not a verified named physical simulation). Its initial arrays have shapes `(10, 2)` for inputs and `(10,)` for scalar output scores. The target is the highest observed score, with no known physical unit.
- **Nature and evolution:** 10 initial course observations were followed by thirteen selected portal evaluations, concentrating or moving between regions as the evidence changed. Most early values were extremely close to zero, with sharp changes near narrow high-scoring regions. The exact R11 input returned the same 1.9999999996761817 in R12 and R13, providing repeatability evidence at that point, not a proof of an everywhere noiseless function.
- **Optimisation strategy:** Early exploratory candidates and a GP/UCB policy (a recorded R2 exploration setting was κ=3.0) struggled with the near-zero response. Later investigation widened the search and tested a Gaussian-modulated response hypothesis. The subsequently published two-component Gaussian–cosine fit was reconstructed retrospectively; it must not be described as the original R11 selector.
- **Data handling and preprocessing:** Original coordinates and outputs were kept intact. Very small response magnitudes made target scaling or transformation an important GP modelling consideration. RBF/Matérn and ARD GP alternatives were investigated, with no unsupported claim that a particular later reconstruction was an original query generator.
- **Weekly iteration and learning:** Early near-zero scores showed that tiny relative improvements were not useful evidence of a good region. Round 11 moved to an alternative region and returned almost 2; identical R12/R13 repeats tested stability without exploring new locations. With a fresh budget I would explore outside weak near-zero basins earlier.
- **Performance and confidence:** The best observed score was 1.9999999996761817 at (0.628540, 0.628540), first attained in R11. A later own-data-only fit using the 10 starting records predicts all 13 personal returns accurately within its supplied functional family, but the family is not an authenticated original equation or an independently certified global optimum.
- **Ethical and practical considerations:** A useful analogy is anomaly or signal detection when informative responses are rare, not a claim that F1 was designed to model contamination or a named physical process. The risk is trusting a poorly scaled surrogate and spending scarce experiments within uninformative regions.

## Function 2

[Full F2 research story](../functions/F2/README.md) · [Measured progress](../functions/F2/progress.svg) · [Observations](../functions/F2/observations.csv) · [Decision ledger](../functions/F2/selection_history.csv)

- **Function overview:** F2 is a 2-dimensional numerical optimisation objective (not a verified named physical simulation). Its initial arrays have shapes `(10, 2)` for inputs and `(10,)` for scalar output scores. The target is the highest observed score, with no known physical unit.
- **Nature and evolution:** 10 initial course observations were followed by thirteen selected portal evaluations, concentrating or moving between regions as the evidence changed. The observations suggest locally promising ridges and competing regions, rather than one securely established smooth optimum. There are no identical submitted locations across the preserved observations, so stochastic output noise cannot be distinguished from local variation using repeat tests.
- **Optimisation strategy:** The R2 notes use UCB κ=2.5 with a dense two-dimensional candidate search. Later global EI and local quadratic or GP searches alternated with tests of other regions. Exploration became more important after a confident local forecast failed.
- **Data handling and preprocessing:** The two continuous inputs needed no categorical encoding; observed values remained unaltered in the dataset. RBF/Matérn GP settings, target normalisation, numerical acquisition search and a small MLP challenger were considered. Local quadratics tested particular directions rather than modelling the whole surface.
- **Weekly iteration and learning:** A Round 9 pre-result forecast around 0.730502 returned only 0.505526. Repeating refinements in that neighbourhood was unproductive; the Round 13 alternative region delivered the personal best. I would enforce earlier chronological validation and reserve more budget for competing regions.
- **Performance and confidence:** The maximum observed score was 0.7442504263021256 at (0.864900, 0.500000), reached in R13. The large R9 forecast error limits confidence in a GP-derived optimum; neither the true maximum nor a physical target value was disclosed.
- **Ethical and practical considerations:** This resembles tuning an engineering process with several competing operating regions, without establishing F2 as any particular process. The main risk is presenting a smooth local fit or its confidence interval as evidence that a wider region has been searched.

## Function 3

[Full F3 research story](../functions/F3/README.md) · [Measured progress](../functions/F3/progress.svg) · [Observations](../functions/F3/observations.csv) · [Decision ledger](../functions/F3/selection_history.csv)

- **Function overview:** F3 is a 3-dimensional numerical optimisation objective (not a verified named physical simulation). Its initial arrays have shapes `(15, 3)` for inputs and `(15,)` for scalar output scores. The target is the highest observed score, with no known physical unit.
- **Nature and evolution:** 15 initial course observations were followed by thirteen selected portal evaluations, concentrating or moving between regions as the evidence changed. Observed scores were negative and must be maximised towards zero. Local improvements were brittle and nearby fitted curves did not always predict later values. No exact repeated query is preserved for a direct stochastic-noise test, and no global unimodality or smoothness is established.
- **Optimisation strategy:** The early GP/UCB framework was followed by local predicted-mean and EI-style tests, controlled-coordinate interpolation, then evaluation of alternative regions. Exploration increased when local fits repeatedly failed to generalise.
- **Data handling and preprocessing:** The original three numeric inputs and returned outputs are unchanged; no categorical transformations or outlier deletion is documented. RBF/Matérn GPs, ARD, local quadratics and smaller neural-network challengers were considered. Locally unusual scores were retained as evidence, not discarded.
- **Weekly iteration and learning:** The local-path forecast around R8 was too optimistic. Alternatives in R10, R11 and R13 improved the best. With another run I would compare out-of-region predictions sooner and avoid narrowing the search before establishing whether multiple basins exist.
- **Performance and confidence:** The best observed score was -0.0037530969187192596 at (0.197280, 0.523429, 0.470094) in R13. This is the highest recorded observation, not evidence that zero or any other number is the global maximum.
- **Ethical and practical considerations:** The relevant lesson for expensive experimental design is the danger of fitting a convincing local peak to too few points. Higher dimensionality and selection bias make extrapolation especially uncertain.

## Function 4

[Full F4 research story](../functions/F4/README.md) · [Measured progress](../functions/F4/progress.svg) · [Observations](../functions/F4/observations.csv) · [Decision ledger](../functions/F4/selection_history.csv)

- **Function overview:** F4 is a 4-dimensional numerical optimisation objective (not a verified named physical simulation). Its initial arrays have shapes `(30, 4)` for inputs and `(30,)` for scalar output scores. The target is the highest observed score, with no known physical unit.
- **Nature and evolution:** 30 initial course observations were followed by thirteen selected portal evaluations, concentrating or moving between regions as the evidence changed. The record contains a locally stable region near 0.659 and better points elsewhere. Exact R11/R12 repeats at the same four-input vector returned the same 0.7304594213260924. This supports repeatability at that tested location, not global smoothness.
- **Optimisation strategy:** GP/UCB/EI alternatives, sensitivity probes and fine-grained coordinate steps were assessed. Prediction checking showed that a very accurate local model could still recommend unproductive micro-steps; a wider move was selected later.
- **Data handling and preprocessing:** All four numeric coordinates and scores remained in the dataset. Noise and lengthscale assumptions were assessed through GP kernel comparisons and chronological forecasts, without removing difficult points as outliers. Local model fits are not treated as hidden source equations.
- **Weekly iteration and learning:** A local forecast was accurate to roughly 1.6 × 10⁻⁹, but progress stalled around 0.659. R11 widened the search and reached 0.730459; R13 improved to 0.746898. Next time I would track improvement per paid query, not prediction accuracy alone.
- **Performance and confidence:** The highest recorded output was 0.7468979113807426 at (0.416903, 0.415704, 0.360320, 0.415205) in R13. Local forecast precision is supported in a narrow region, but it is not a global confidence bound.
- **Ethical and practical considerations:** This is analogous to parameter tuning where a tiny, highly predictable adjustment costs as much as a wider experiment. The risk is confusing precise predictions with worthwhile decisions.

## Function 5

[Full F5 research story](../functions/F5/README.md) · [Measured progress](../functions/F5/progress.svg) · [Observations](../functions/F5/observations.csv) · [Decision ledger](../functions/F5/selection_history.csv)

- **Function overview:** F5 is a 4-dimensional numerical optimisation objective (not a verified named physical simulation). Its initial arrays have shapes `(20, 4)` for inputs and `(20,)` for scalar output scores. The target is the highest observed score, with no known physical unit.
- **Nature and evolution:** 20 initial course observations were followed by thirteen selected portal evaluations, concentrating or moving between regions as the evidence changed. The response scale is far larger than for other functions and observed performance rose sharply towards the legal upper boundary. The exact boundary query returned 8662.405001248297 in each of R10–R13. These repeats show numerical consistency at the tested point but do not establish a global optimum of the unknown function.
- **Optimisation strategy:** Initially GP/UCB (R2 κ=1.0) and local EI suggested promising steps. The strongest evidence became controlled coordinate changes towards the upper boundary. Later a power-sum equation was reconstructed, but it did not cause the R10 boundary choice.
- **Data handling and preprocessing:** Raw outputs are preserved despite their large range. Standardisation or output transforms matter for GP fitting, but must not be confused with changed measured scores. Controlled trials adjusted one coordinate while holding others near validated high settings; no outliers were deleted.
- **Weekly iteration and learning:** A series of observed gains, with marginal improvements increasing along a controlled coordinate path, justified testing all permitted upper values. I would continue to prioritise targeted boundary experiments but would test nearby alternatives to assess global claims if budget allowed.
- **Performance and confidence:** The maximum observed output was 8662.405001248297 at (0.999999, 0.999999, 0.999999, 0.999999), first returned in R10. A retrospective power-sum model agrees with the measured boundary response; its global behaviour remains a model hypothesis.
- **Ethical and practical considerations:** A useful analogy is constrained engineering design where performance can rise at a permitted boundary. Real applications require checking safety constraints and feasibility, not assuming that the numerically largest boundary is operationally acceptable.

## Function 6

[Full F6 research story](../functions/F6/README.md) · [Measured progress](../functions/F6/progress.svg) · [Observations](../functions/F6/observations.csv) · [Decision ledger](../functions/F6/selection_history.csv)

- **Function overview:** F6 is a 5-dimensional numerical optimisation objective (not a verified named physical simulation). Its initial arrays have shapes `(20, 5)` for inputs and `(20,)` for scalar output scores. The target is the highest observed score, with no known physical unit.
- **Nature and evolution:** 20 initial course observations were followed by thirteen selected portal evaluations, concentrating or moving between regions as the evidence changed. Close inputs sometimes yielded materially different negative scores, indicating steep or interacting local effects. There were no exact repeated input vectors in this record, so stochastic noise is not established; apparent instability may reflect geometry rather than randomness.
- **Optimisation strategy:** The investigation used GP/UCB/EI, local coordinate probes and tests of competing regions. A recorded R2 choice was UCB κ=1.0. Large out-of-sample errors reduced confidence in staying inside the early local neighbourhood.
- **Data handling and preprocessing:** The five continuous coordinates and all returns were retained unaltered. ARD GP, alternative kernel and small neural-network comparisons examined interactions and potential noise sensitivity; model uncertainty was checked against later actual returns rather than assumed calibrated.
- **Weekly iteration and learning:** Tiny coordinate changes disproved simple local extrapolation; an alternative region in R10 and further refinement produced the R12 best. I would test robustness along multiple coordinates sooner and explicitly differentiate noise from deterministic sensitivity.
- **Performance and confidence:** The best recorded score was -0.03751864724436928 at (0.415080, 0.344119, 0.644062, 0.776818, 0.076258) in R12. R13 returned a lower score, so the final query is not the best result. No global maximum or hidden equation is established.
- **Ethical and practical considerations:** This resembles tuning a sensitive multivariable process with potentially expensive failed experiments. Reliance on one local GP forecast without perturbation and regional checks would be risky.

## Function 7

[Full F7 research story](../functions/F7/README.md) · [Measured progress](../functions/F7/progress.svg) · [Observations](../functions/F7/observations.csv) · [Decision ledger](../functions/F7/selection_history.csv)

- **Function overview:** F7 is a 6-dimensional numerical optimisation objective (not a verified named physical simulation). Its initial arrays have shapes `(30, 6)` for inputs and `(30,)` for scalar output scores. The target is the highest observed score, with no known physical unit.
- **Nature and evolution:** 30 initial course observations were followed by thirteen selected portal evaluations, concentrating or moving between regions as the evidence changed. A controlled one-coordinate path showed smooth local gains early, but another region produced much larger scores from R10 onwards. No exact input-vector repeat is preserved; R12 and R13 differ by one millionth in x1 and their outputs differ slightly. This demonstrates local sensitivity, not necessarily stochastic noise.
- **Optimisation strategy:** UCB (R2 κ=2.0), local EI and coordinate refinement gave way to wider regional exploration. A positive Hartmann-6 structural hypothesis produced a prospective R12 forecast of 3.32236801, tested directly with the portal.
- **Data handling and preprocessing:** Six continuous inputs were retained at their recorded precision. RBF/Matérn ARD GP and restricted-path quadratic fits helped identify candidate directions; a later numerical Hartmann-6 equation check is distinguished from its prospective prediction.
- **Weekly iteration and learning:** A local x1 path improved gradually to 1.786338 in R9. R10 found a stronger region (3.149459), while the model-based R12 query returned 3.322368. With more budget I would compare the competing regions earlier and verify robustness to other coordinate perturbations.
- **Performance and confidence:** The highest observed score was 3.3223680113931557 at (0.201689, 0.150011, 0.476874, 0.275332, 0.311652, 0.657301) in R12. The pre-result prediction matched closely, but a tested fit cannot authenticate the hidden implementation or certify its global optimum.
- **Ethical and practical considerations:** This is analogous to six-parameter scientific or engineering optimisation, where exploration of different basins matters. Structural explanations are useful only if tested on genuinely later observations, not only fitted after seeing results.

## Function 8

[Full F8 research story](../functions/F8/README.md) · [Measured progress](../functions/F8/progress.svg) · [Observations](../functions/F8/observations.csv) · [Decision ledger](../functions/F8/selection_history.csv)

- **Function overview:** F8 is a 8-dimensional numerical optimisation objective (not a verified named physical simulation). Its initial arrays have shapes `(40, 8)` for inputs and `(40,)` for scalar output scores. The target is the highest observed score, with no known physical unit.
- **Nature and evolution:** 40 initial course observations were followed by thirteen selected portal evaluations, concentrating or moving between regions as the evidence changed. The observed responses are consistent with a smooth concave additive quadratic, although sparse eight-dimensional observations alone cannot verify the hidden equation everywhere. Exact R10–R13 repeats at the fitted vertex each returned 10, providing local repeatability evidence.
- **Optimisation strategy:** An early GP/UCB policy (R2 κ=1.5) used a large candidate pool, followed by local EI and controlled changes. Numerical evidence eventually supported a 17-coefficient additive quadratic, whose vertex was submitted in R10 and scored 10.
- **Data handling and preprocessing:** Eight continuous input variables and measured scores are preserved; no categorical encoding or removal of unusual points was needed. GPs compared RBF/Matérn kernel assumptions and output scaling. The quadratic fit used 49 observations available before R10; a separate retrospective validation fitted 17 coefficients on 40 initial observations and predicted 13 later returns.
- **Weekly iteration and learning:** Small GP-guided steps steadily improved the score to 9.932443 by R9. Identifying a simple structure then located a much stronger query at R10. I would test interpretable polynomial structures sooner, before investing in complex surrogate search.
- **Performance and confidence:** The maximum observed output was 10 at (0.100000, 0.150000, 0.130000, 0.150000, 0.800000, 0.500000, 0.200000, 0.600000), first attained in R10. The fitted quadratic has an analytically unique vertex at 10 and retrospectively predicts 13 later portal outputs within numerical precision; neither result proves source-code identity.
- **Ethical and practical considerations:** A useful analogy is eight-hyperparameter model tuning. Complex optimisation can be unnecessary when the response has a simpler validated form; the risk is claiming that a simulator benchmark evaluates the private portal or proves out-of-sample global correctness.

---

## Interpretation and further evidence

These per-function accounts address **function overview, data behaviour, optimisation strategy, preprocessing, iteration, results and wider implications**, as requested by the supplied datasheet template. The real-world example for each function remains unverified; no domain-specific interpretation has been invented. All observed scores and submitted inputs are checked against the [canonical dataset](../data/all_observations.csv). The [main datasheet](../DATASHEET.md) describes fields, sampling bias, collection, source rights and use limitations for the dataset as a whole.

The [round-by-round research record](../journey/README.md) provides the original chronology. The [mathematical reconstructions](reconstruction.md) and [post-capstone reference simulations](../research/full_optimisers/README.md) must not be mistaken for additional paid portal measurements.

[← Main dataset datasheet](../DATASHEET.md)
