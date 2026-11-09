# When the Prediction Was Right but the Decision Was Wrong: Thirteen Rounds of Black-Box Optimisation

> **Update:** This reflection predates receipt of final portal returns. See the [verified Round 13 addendum](round13_addendum.md) for the new results without changing the original pre-result interpretation.

One of my most accurate predictions was also a warning that I was optimising badly. On F4, a local surrogate predicted the next result within **1.6 × 10⁻⁹**. Yet I was taking steps so small that the score remained around 0.659. A wider move later returned **0.730459**.

Elsewhere the problem was different. On F2, a forecast of **0.730502** returned **0.505526**. On F8, the predictions were good, but I eventually found that a simple quadratic explained the function and identified its maximum of **10**.

These were **three different failures**: a prediction I could not trust, an accurate prediction attached to an unproductive search, and an unnecessarily complex representation. Learning to distinguish them became my real capstone achievement.

## 1. The starting point: build a model I could challenge

I developed my optimisation workflow **from scratch**, assembling established Python libraries rather than adopting a complete optimiser. I chose scikit-learn's GaussianProcessRegressor for its predicted mean and uncertainty, with NumPy, pandas and SciPy for data management, candidate searches and optimisation. Jupyter notebooks made each proposal inspectable. Course materials, published research and AI-assisted coding and critique informed experiments; recorded outputs and reproducible calculations determined what I accepted.

We began with **175 supplied observations** across eight hidden functions, from two to eight dimensions, and one additional evaluation per function per round. With so little data, a Gaussian Process (GP) was a sensible baseline. Its limitation was equally important: a reported uncertainty is conditional on the chosen kernel, fitted parameters and data. It does not measure every way the representation or search policy might be wrong.

**Repository:** https://github.com/tatonsyML/bbo-capstone-imperial-college

## 2. How the strategy changed over thirteen rounds

### Phase I: Learning to propose, Rounds 1–4

**R1:** I inspected the initial observations and ranked promising regions. F1 was almost numerically flat; F8 had only 40 observations across eight dimensions. I treated the functions as different problems from the outset.

**R2:** I implemented Upper Confidence Bound (UCB), with greater exploration on F1 (κ=3), plus dense two-dimensional grids and searches of up to **300,000 reproducible random candidates** in higher dimensions. This replaced informal selection with auditable proposals.

**R3:** I added Expected Improvement (EI), maximin sampling and local posterior-mean optimisation. F1 received broad exploration, F2 global EI, F3 local mean search, and F4–F8 local EI. The acquisition policy became function-specific.

**R4:** I tested logistic regression, linear/RBF Support Vector Machines and small neural networks. Their classifications and gradients suggested alternative directions, but they were not reliable substitutes for GP uncertainty. I retained them as challengers, not automatic decision-makers.

### Phase II: Learning to test the model, Rounds 5–9

**R5:** Controlled coordinate probes changed one input at a time. Raising F5's second coordinate increased its output from **4,295.87 to 4,694.32**; lowering F7's first coordinate worsened its result. Direct observations now checked model-suggested directions.

**R6:** Five-fold validation showed GP versus small-MLP normalised RMSE of **0.112 versus 0.314 on F7**, and **0.051 versus 0.157 on F8**. The MLP did slightly better on F2 and F3. I introduced local polynomial fits instead of assuming one surrogate was best everywhere.

**R7:** I compared RBF/Matérn kernels, automatic relevance determination, noise settings and restarts. More importantly, I introduced **rolling-origin tests**: train on earlier observations, forecast a later result and check the error. An F8 forecast missed by only **0.000025**; F6 exposed substantial overconfidence.

**R8:** I began separating portal observations, pre-result forecasts, generated candidates and AI-assisted hypotheses. On F2, moving one coordinate by **0.000407** reduced the score from **0.691315 to 0.589348**. Nearby inputs were not necessarily predictably similar.

**R9:** The decisive F2 forecast of **0.730502** returned **0.505526**. I stopped treating a high acquisition score as sufficient justification. I checked forecast errors and alternative fits before letting the model influence another expensive query.

The published leaderboard after Round 9 sharpened this problem: I was **first on F8**, seventh on F4, tenth on F7, but **29th on F6** among 39 participants. Most entries showed stronger *outcomes*, not the inputs responsible. That was evidence of room to improve, not a ready-made solution.

### Phase III: Changing the representation and search, Rounds 10–13

**R10:** Inspired by the NeurIPS 2020 challenge, I tried HEBO-inspired kernel/transform/acquisition committees and TuRBO-style restricted local searches. These were **adaptations, not full implementations**. Limited public input-output records helped redirect some F1, F3 and F6 proposals and informed F5/F7 comparisons; I logged them separately from my evaluations. F5 reached **8,662.405** at the permitted upper boundary. My structural model of F8 predicted **10**, confirmed by the portal.

**R11:** DBSCAN revealed where I had sampled repeatedly, not where the objective was necessarily strongest. An oscillatory mathematical reconstruction guided F1 to **1.999999999676**. On F4, a wider local move escaped the plateau and returned **0.730459**. F2 and F3 also established new personal bests.

**R12:** PCA explained **48.8% of F8's sampled input variance** with two components, but restricting the fitted quadratic to them capped its predicted maximum near **9.956**, compared with **10** in eight dimensions. F6 improved to **−0.037519**; F7 returned **3.322368**, matching a pre-recorded prediction from the positive Hartmann-6 structure. Four exact repeats confirmed returns at those settings without exploring their neighbourhoods.

**R13:** With no later evaluations to benefit from learning, my final-round plan favoured plausible immediate gains, such as a competing F2 region. It also included a distinct F8 perturbation as a sensitivity test. Since the fitted quadratic already peaked at 10, that proposal offered **validation, not a credible higher score**. In hindsight, a final scoring opportunity was an expensive place for that test. R13 returns were not available when I prepared this retrospective.

## 3. Results: the turning point was measurable

| Function | Initial best | Best after R9 | Best through R12 |
|---|---:|---:|---:|
| F1 | 7.71 × 10⁻¹⁶ | 1.92 × 10⁻¹⁵ | **1.999999999676** |
| F2 | 0.611205 | 0.691315 | **0.695337** |
| F3 | −0.034835 | −0.020856 | **−0.005709** |
| F4 | −4.025542 | 0.658933 | **0.730459** |
| F5 | 1,088.860 | 6,583.561 | **8,662.405** |
| F6 | −0.714265 | −0.541448 | **−0.037519** |
| F7 | 1.364968 | 1.786338 | **3.322368** |
| F8 | 9.598482 | 9.932443 | **10.000000** |

These are best-so-far *observations*, not each round's return; the functions have different scales. **All eight final confirmed bests arose in Rounds 10–12:** F5/F8 in R10, F1–F4 in R11, F6/F7 in R12. The concentration of progress followed a change towards function-specific, evidence-tested decisions; it does not prove one technique caused every gain.

The results also revealed **three kinds of modelling failure**:

- **F2, predictive reliability:** A forecast error of approximately **0.225** was large relative to the improvements sought. GP uncertainty conditional on its assumptions was not a guarantee of accuracy. One miss was evidence to investigate, not proof of universal miscalibration.
- **F4, search adequacy:** A local forecast could be accurate to **1.6 × 10⁻⁹**, yet micro-steps from **0.658930 to 0.658962** did little to challenge the region. Widening the search produced **0.730459**. Predicting a chosen point well is not the same as choosing a useful point.
- **F8, mathematical suitability:** A GP forecast had already been accurate to **0.000025**. But a structural equation could explain the response and identify the optimum analytically, without another round of GP tuning.

My new decision rule became: **test predictive reliability, challenge the search region, then test whether a simpler structure explains the data**. These are separate checks; passing one does not establish the others.

## 4. Mathematical reconstruction: when the black box became interpretable

For F8, I fitted a **17-coefficient additive quadratic** using my accumulated observations:

**f₈(x) = 10 − Σⱼ wⱼ(xⱼ − cⱼ)²**, with

**c = (0.10, 0.15, 0.13, 0.15, 0.80, 0.50, 0.20, 0.60)** and **w = (2, 1, 3, 1, 0.5, 1, 2, 0.1)**.

All eight weights are positive, so the fitted equation has a unique maximum of **10** at **c**. Equal deviations in input 3 incur **30 times** the score penalty of equal deviations in input 8. That objective sensitivity is not the same thing as the variance PCA preserves.

Before my Round 10 submission, I checked the model against **five publicly shared external input-output results**. They corroborated the structure but did not supply my fitted coefficients. In a separate **retrospective** test, fitting this structure with **only the 40 original course observations** reproduced my twelve subsequent portal outputs with maximum absolute error below **2 × 10⁻¹⁵**. That is evidence that the starting data already supported recovery, not that I had recognised the equation in Round 1.

I subsequently reconstructed and numerically checked **four of the eight** function families: F1's Gaussian-modulated oscillations, F5's interacting power-sum expression, F7's positive Hartmann-6, and F8's quadratic. Unlike F8's additive response, F5 took the form **f₅(x) = 0.01 Σₖ [Σⱼ(4xⱼ)ᵏ − bₖ]²**, for k and j from 1 to 4, with **b = (7.5, 16, 40, 120)**. Its squared sums introduce interactions between coordinates and explain why the permitted upper corner scored so highly. But I recovered the complete F5 equation *after* achieving that boundary result: the equation explains the earlier experiment; it did not generate it. F2, F3, F4 and F6 remained unresolved. Numerical agreement with tested observations does not authenticate the hidden source code.

## 5. What surprised me, and what I would do differently

**The biggest surprise** was that an eight-dimensional function yielded a simple, highly predictive equation while several lower-dimensional functions remained difficult. Dimensionality was not a reliable measure of difficulty; *structure, observation quality and the assumptions of the surrogate* mattered more.

I also learnt that exploration versus exploitation was not simply a gradual reduction in step size. F4 needed a wider search late in the project, while F8 needed no further search once its structure was supported. At the final horizon, a query justified only by possible learning had little scoring value if no subsequent decision could use it.

Starting again, I would test simple structural hypotheses alongside GPs from the first round; track forecasts before outcomes; audit duplicates and rejected candidates; and benchmark complete HEBO/TuRBO implementations rather than treating selected mechanisms as equivalents. I would document the provenance of limited shared records, and distinguish leaderboard evidence that a better score *exists* from input-output evidence about *where to investigate*. Reviewing different approaches reinforced that no algorithm deserved automatic priority.

In my work as an Oracle HCM solution architect, the same reasoning applies when tuning payroll data extracts. I would explore batch sizes and concurrency settings in controlled tests, predict runtime and reconciliation outcomes, then refine only configurations that proved complete and reliable. A faster run with missing records is not an improvement; a narrow prediction interval is not a substitute for validation before production deployment.

**The most important lesson I learnt:** a good prediction, a good search decision and a good mathematical explanation are not the same achievement. F2 taught me to challenge a forecast, F4 to challenge the search, and F8 to challenge the model itself. I began asking, *Which input does my optimiser prefer?* I finished asking, *What evidence makes that the right question?*
