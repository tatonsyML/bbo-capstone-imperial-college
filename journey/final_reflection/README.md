# When the Prediction Was Right but the Decision Was Wrong: Thirteen Rounds of Black-Box Optimisation

One of my most accurate predictions was also a warning that I was optimising badly. On F4, a local surrogate predicted the next result within 1.6 × 10⁻⁹. Yet I was taking steps so small that the score remained around 0.659. A wider move later returned 0.730459, and the final round reached 0.746898.

Elsewhere the problem was different. On F2, a forecast of 0.730502 returned 0.505526. On F8, the predictions were good, but I eventually found that a simple quadratic explained the function and identified its maximum of 10 using calculus.

These were three different problems: **a prediction I could not trust, an accurate prediction attached to an unproductive search, and an unnecessarily complex representation.** Learning to distinguish them became my real capstone achievement.

## 1. The starting point: build a model I could challenge

I developed my optimisation workflow from scratch, assembling established Python libraries rather than adopting a complete optimiser. I chose scikit-learn's GaussianProcessRegressor for its predicted mean and uncertainty, with NumPy, pandas and SciPy for data management, acquisition calculations and numerical searches. Jupyter notebooks made each proposal inspectable.

Course materials, published research and AI-assisted coding and critique informed experiments; recorded outputs and reproducible calculations determined what I accepted.

We began with **175 supplied observations across eight hidden functions**, ranging from two to eight dimensions, and one additional evaluation per function per round. Thirteen rounds added 104 observations, bringing the total to 279.

With so little data, a Gaussian Process (GP) was a sensible baseline. Its limitation was equally important: reported uncertainty is conditional on the chosen kernel, fitted parameters and data. It does not measure every way the representation or search policy might be wrong.

## 2. How the code and strategy changed over thirteen rounds

### Phase I: Learning to propose, Rounds 1–4

- **R1: Establishing the evidence.** I loaded the initial observations, identified the strongest responses and selected function-specific queries. F1 was almost numerically flat, while F8 had only 40 observations across eight dimensions. I treated the functions as different optimisation problems from the outset.

- **R2: Introducing UCB and reproducible search.** I implemented Upper Confidence Bound (UCB), with greater exploration for F1 (κ = 3.0) and lower settings for improving functions. Dense two-dimensional grids and up to **300,000 reproducible random candidates** in higher dimensions replaced informal selection with inspectable proposals.

- **R3: Separating prediction from acquisition.** I added Expected Improvement (EI), maximin sampling and local posterior-mean optimisation. F1 received broad exploration, F2 global EI, F3 local mean search, and F4–F8 local EI. The important code change was making acquisition and candidate-search policies configurable by function rather than applying one rule everywhere.

- **R4: Adding model challengers.** I compared logistic regression, linear/RBF Support Vector Machines and small neural networks. Classification boundaries and neural-network gradients offered alternative directional evidence, but not dependable replacements for GP uncertainty. They became supporting diagnostics. Meanwhile, a controlled change in F5's second coordinate raised its output from **4,295.87 to 4,694.32**.

### Phase II: Learning to test the model, Rounds 5–9

- **R5: Introducing controlled coordinate comparisons.** Rather than change several inputs together, I investigated individual directions. Increasing F5's first coordinate from 0.508373 to 0.558373, with the others fixed, raised its output from **4,694.32 to 4,807.99**. This gave me interpretable evidence beyond a surrogate's recommendation.

- **R6: Comparing predictive performance.** Five-fold validation showed GP versus small-MLP normalised RMSE of **0.112 versus 0.314 on F7**, and **0.051 versus 0.157 on F8**. The MLP performed slightly better on F2/F3. I added local polynomial challengers rather than assuming one model family would dominate.

- **R7: Adding chronological forecast audits.** I compared RBF/Matérn kernels, automatic relevance determination (ARD), noise settings and optimiser restarts. More importantly, I introduced rolling-origin validation: train using earlier observations, forecast a later result and measure the error. F8 missed by only **0.000025**, while F6 exposed substantial predictive weakness. This changed how I judged models, from fitting existing data to predicting unseen outcomes.

- **R8: Separating evidence from hypotheses.** I distinguished actual portal observations, pre-result forecasts, generated candidates and AI-assisted suggestions. F2 demonstrated why: changing one coordinate by **0.000407** reduced the score from **0.691315 to 0.589348**. Nearby inputs did not necessarily produce predictably similar outputs.

- **R9: Using prediction errors to challenge decisions.** An F2 forecast of **0.730502** returned **0.505526**, an error of approximately 0.225. I stopped treating a high acquisition score as sufficient justification. Historical forecast accuracy and competing fits became more important in candidate selection.

After my Round 9, the leaderboard placed me **first on F8, seventh on F4, tenth on F7 and 29th on F6** among 39 participants. Those rankings showed where improvement was needed, not which inputs or methods produced other participants' results.

### Phase III: Changing the representation and search, Rounds 10–13

- **R10: Introducing structural models and alternative search mechanisms.** I compared HEBO-inspired kernel, output-transformation and acquisition committees with TuRBO-style restricted local searches. These were adaptations, not complete HEBO or TuRBO implementations. I also used limited publicly shared observations as separately recorded validation evidence.

  For F5, the accumulated boundary trend justified a manual move to the permitted upper corner, returning **8,662.405**. For F8, a fitted 17-coefficient quadratic replaced the need for further GP search: calculus predicted **10**, and the portal confirmed it.

- **R11: Adding clustering diagnostics and widening stalled searches.** DBSCAN identified concentrations in my sampling history, but those clusters did not necessarily contain the strongest responses. An oscillatory mathematical reconstruction guided F1 to **1.999999999676**. On F4, widening the local candidate region broke the 0.659 plateau and produced **0.730459**. F2/F3 also established new bests. F8 retained its analytically derived optimum.

- **R12: Testing dimensionality reduction against the objective.** PCA explained **48.8% of F8's sampled input variance** using two components. However, restricting its fitted quadratic to those components capped the predicted maximum near **9.956**, versus **10** in eight dimensions. I had demonstrated that preserving variance does not necessarily preserve the optimum.

  F6 improved to **−0.037519**. F7 returned **3.322368011393**, matching a prediction recorded beforehand using the positive Hartmann-6 structure. Four repeated inputs returned identical scores, confirming those observations without exploring new locations.

- **R13: Applying finite-horizon decisions.** With no subsequent evaluation to benefit from learning, I favoured credible immediate improvements. A competing F2 region returned **0.744250**; F3 reached **−0.003753**, and F4 **0.746898**, all new personal bests. F6 returned −0.076980, below its incumbent, while a one-millionth F7 adjustment produced a marginally lower score.

I retained the established best inputs for F1 and F5. For F8, the reconstructed quadratic already identified the maximum of 10. I therefore submitted the same analytically derived input throughout Rounds 11–13.

### Which modifications mattered most?

Four modifications mattered most:

1. **Structural models:** F8's quadratic yielded the analytic maximum **10**; related reconstruction guided F1 to **1.999999999676** and predicted F7's **3.322368**. My biggest methodological shift.
2. **Adjustable search width:** Widening F4's stalled search raised **0.659 to 0.730459** (R11); later refinement reached **0.746898** (R13).
3. **Evidence-led override:** F5's boundary trend justified the upper-corner query (**8,662.405**, R10). Its complete equation was reconstructed afterwards.
4. **Chronological validation:** F2's **0.225** forecast error reduced trust in the local GP. Comparing other regions preceded its R13 best of **0.744250**, without proving causation.

Better decisions, rather than added complexity, drove these changes.

## 3. Results: the turning point was measurable

| Function | Initial best | Best after R9 | Final best | First achieved |
|---|---:|---:|---:|:---:|
| F1 | 7.71 × 10⁻¹⁶ | 1.92 × 10⁻¹⁵ | **1.999999999676** | R11 |
| F2 | 0.611205 | 0.691315 | **0.744250426302** | R13 |
| F3 | −0.034835 | −0.020856 | **−0.003753096919** | R13 |
| F4 | −4.025542 | 0.658933 | **0.746897911381** | R13 |
| F5 | 1,088.860 | 6,583.561 | **8,662.405001** | R10 |
| F6 | −0.714265 | −0.541448 | **−0.037518647244** | R12 |
| F7 | 1.364968 | 1.786338 | **3.322368011393** | R12 |
| F8 | 9.598482 | 9.932443 | **10.000000** | R10 |

These are **best-so-far observations**, not individual round returns; function scales differ. All eight final bests first arose in R10–13, including **three in R13**. This supports adaptation, not proof of causation.

Three limitations emerged: **F2**, prediction reliability (error **0.225**); **F4**, search adequacy (a forecast accurate to **1.6 × 10⁻⁹** accompanied unproductive micro-steps); **F8**, model suitability (a quadratic identified the maximum analytically).

My rule: **validate forecasts, challenge search regions, and test simpler structures**. Each needs independent evidence.

## 4. Mathematical reconstruction: when the black box became interpretable

For F8, I fitted a **17-coefficient additive quadratic** using my accumulated observations:

**f₈(x) = 10 − Σⱼ wⱼ(xⱼ − cⱼ)²**, with

**c = (0.10, 0.15, 0.13, 0.15, 0.80, 0.50, 0.20, 0.60)** and **w = (2, 1, 3, 1, 0.5, 1, 2, 0.1)**.

All eight weights are positive. Each partial derivative, **−2wⱼ(xⱼ − cⱼ)**, equals zero at xⱼ = cⱼ. The Hessian is diagonal with strictly negative entries, so the fitted equation has a unique global maximum of **10** at c.

Equal deviations in input 3 incur **30 times** the score penalty of equal deviations in input 8. That objective sensitivity is not the same as the variance PCA preserves.

Before R10, I checked the model against **five publicly shared external input-output results**. They corroborated the structure but did not supply my coefficients. In a separate **retrospective** test, fitting the quadratic using only the **40 original course observations** reproduced twelve subsequent portal results with maximum absolute error below **2 × 10⁻¹⁵**.

The starting data therefore supported reconstruction much earlier, but I had not recognised the equation in Round 1.

I also reconstructed and numerically checked four function families: F1's Gaussian-modulated oscillations, F5's interacting power-sum expression, F7's positive Hartmann-6 and F8's quadratic.

Unlike F8's additive response, F5 took the form:

**f₅(x) = 0.01 Σₖ [Σⱼ(4xⱼ)ᵏ − bₖ]²**, for k and j from 1 to 4, with **b = (7.5, 16, 40, 120)**.

Its squared sums introduce interactions between coordinates and help explain why the permitted upper corner scored so highly. However, I reconstructed the complete F5 equation *after* obtaining that boundary result. It explains the earlier experiment; it did not generate it.

F2, F3, F4 and F6 remained unresolved. Numerical agreement with tested observations does not authenticate the hidden source code.

## 5. Trade-offs, surprises and what I would do differently

**The trade-off was function-specific**, not simply exploring early and exploiting late. F1 needed a new representation, F4 a wider search, F2 another region and F8 no further search after its confirmed analytical optimum. More models increased complexity and assumptions. In R13, information had no later query to influence; candidates needed credible immediate upside.

**My biggest surprise:** F8's eight-dimensional function yielded a simple quadratic while lower-dimensional functions remained unresolved. Structure mattered more than dimension. Peers reinforced this: Andreia's function-specific BoTorch contrasted with Nayeem's transparent EI; Patrick and Rishin identified F8's quadratic through different approaches. No optimiser was universally superior.

**Starting again**, I would test structural models alongside GPs from R1; record forecasts before outcomes; preserve rejected candidates and settings; audit duplicates; validate chronologically; and benchmark full HEBO/TuRBO rather than confuse them with my adaptations. I would investigate unresolved F2/F3/F4/F6 further.

In Oracle HCM payroll-extract tuning, I would evaluate runtime alongside complete record reconciliation. **Speed without complete records is not improvement; predictive uncertainty does not replace production validation.**

**My central lesson:** a good prediction, a good search decision and a good mathematical explanation are different achievements. F2 taught me to challenge forecasts, F4 the search, and F8 the model.

I began asking, *Which input does my optimiser prefer?* I finished asking, *What evidence makes that the right decision?*
