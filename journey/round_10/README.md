# Round 10 · Module 21 | Transparent decisions, F5 boundary and F8 structure

**What happened:** The [submitted inputs](queries.txt) and [returned outputs](outputs.txt) are confirmed portal results. F5 reached **8662.405001248297** at the feasible boundary and F8 reached **10** at the fitted quadratic vertex. The document below also retains decision-time predictions that **preceded** the portal outputs.

## My reasoning at the time

After nine rounds I no longer asked only which candidate had the highest acquisition value. My central question was what evidence earned the model the right to influence an expensive portal query. I compared Gaussian Process EI and UCB proposals with controlled path fits, structural hypotheses, HEBO-inspired model committees and TuRBO-style local challengers. These were selected mechanisms, not complete official HEBO or TuRBO runs.

Prospective forecast accuracy had become a gate on model authority. F4's local prediction was accurate to about 1.6 × 10⁻⁹; F2's missed its return by roughly 0.225. The accuracy of the F4 fit supported another local diagnostic, though later evidence showed that the steps were too small. For F2 I reduced trust in the local interpolation and treated the next candidate as a test of the assumptions behind it.

I made eight distinct decisions. F1 required another chance to locate a positive-response region rather than continue polishing microscopic outputs. F3 warranted a targeted alternative basin, with external evidence attributed separately. F5's sequence of improvements suggested the upper boundary, leading me to submit four coordinates at 0.999999. F6 called for comparison with a peer-informed proposal rather than another unexamined local extrapolation. F7's speculative local vertex was challenged by an alternative region with greater potential. F8 suggested that a much simpler additive quadratic with 17 coefficients might explain the score more effectively than a complex GP.

I learnt to separate model predictions from observed returns, while recognising that adaptively selected inputs concentrate around areas I had already explored. The assumption of local smoothness remained uncertain outside tested regions.

This reflection was written before the round's results. The later F5 boundary return and F8 score of 10 belong to the confirmed technical record below, not to the certainty I held at the decision point. The week's central achievement was to make each query an accountable hypothesis.

## What I did

I compared controlled local experiments with GP/ARD forecasts, HEBO-inspired model committees, TuRBO-style local challengers, candidate-region changes and structural polynomial hypotheses. Module 21 focused on transparency, interpretability and reporting model limitations.

## What happened at the decision point (before the return)

Before the Round 10 scores were returned, I had **247 observations through Round 9** and eight candidate queries to choose.

## Decisions and reasoning

- **F1** — 0.582552-0.558941. Targeted positive-response region; exploratory near-peer evidence; unobserved.
- **F2** — 0.701500-0.959796. Tight incumbent diagnostic after Week 9 GP forecast miss.
- **F3** — 0.469634-0.620072-0.416672. Alternative-region local interpolation; external evidence; uncertain.
- **F4** — 0.420370-0.427768-0.368794-0.412497. Controlled local refinement supported by prospective accuracy.
- **F5** — 0.999999-0.999999-0.999999-0.999999. Upper-bound exploitation supported by nine observed gains and cubic challenger.
- **F6** — 0.379322-0.338275-0.586412-0.727790-0.036539. Peer-informed GP regional exploration; model forecast only.
- **F7** — 0.190478-0.171014-0.347582-0.283057-0.283946-0.639922. Alternative basin; peer-informed ensemble; substantial uncertainty.
- **F8** — 0.100000-0.150000-0.130000-0.150000-0.800000-0.500000-0.200000-0.600000. 17-coefficient additive quadratic fitted vertex; predicted score 10.

## Superseded working proposals

The following points were **provisional alternatives**, not portal evaluations. They were replaced before the final Round 10 submission:

| Function | Earlier working candidate | Submitted Round 10 candidate |
|---|---|---|
| F1 | 0.472784-0.455748 | 0.582552-0.558941 |
| F3 | 0.325355-0.003391-0.538367 | 0.469634-0.620072-0.416672 |
| F6 | 0.437642-0.275181-0.565494-0.833184-0.042658 | 0.379322-0.338275-0.586412-0.727790-0.036539 |
| F7 | 0.223588-0.369270-0.256273-0.262985-0.391467-0.834089 | 0.190478-0.171014-0.347582-0.283057-0.283946-0.639922 |

F2, F4, F5 and F8 were retained unchanged. The external data used for some experimental reranking are not part of the 247 personally observed results. These choices do **not** acquire a true score until the portal response arrives.



## What I learnt

F5's legal all-upper-bound input improved decisively and F8's 17-coefficient quadratic identified a confirmed peak. The later portal outcomes distinguish correct forecasts from speculative GP rankings. A model-generated candidate is not an observation until evaluated.

## How I approached this round

I described an **evidence-gated** comparison among GP, regional polynomial, **HEBO-inspired** committees and a **TuRBO-style** search with a fixed width of **0.20**. These were *adaptations*, not full library implementations. F5's four-coordinate boundary query and F8's quadratic vertex were **prospective hypotheses** here; only the subsequent portal returns established the reported scores.


## Original assessed work

The **unchanged** Module 21.2 assessment documents are retained under [archive/component_21_2/](archive/component_21_2/), including the [datasheet](archive/component_21_2/datasheet.md), [model card](archive/component_21_2/model_card.md) and [decision log](archive/component_21_2/decision_log.md). The original [21.1 reflection](archive/component_21_1/submission.md) is a dated submission snapshot, separate from the final model card. An [alternative draft](archive/component_21_1/alternate_draft.md) is preserved as a distinct historical reconstruction; its precise submission status was not independently verified.

Other records include the [Round 10 optimisation snapshot](optimisation.yaml), [candidate CSV](round10_candidates.csv) and [early exploratory notebooks](early_notebooks/).

## Further Round 10 model comparisons

### Comparing predictions with observed results

| Function | Comparison | Interpretation |
|---|---|---|
| F2 | Own Week 9 forecast **0.730502** versus returned **0.505526** | The earlier local GP overstated its accuracy |
| F4 | Own Week 9 forecast **0.658932869** versus returned **0.658932867** | The controlled local fit was exceptionally accurate |
| F5 | Tested additive cubic **RMSE 61.80** versus quadratic **1,033.44** on four later peer points | Polynomial degree matters; still a small, model-selected external test |
| F6 | Earlier proposal GP ensemble **−0.262**, revised proposal **−0.192** | Better **predicted** mean; model range approximately −0.249 to −0.151 |
| F7 | Earlier proposal GP ensemble **1.73**, revised proposal **2.79** | Better **predicted** mean; model range approximately 2.246 to 3.115 |
| F8 | Own-data additive quadratic predicts five later external observations at about **1.35e−10 RMSE** | Strong external corroboration of the fitted structure, not a portal-confirmed Round 10 result |

**F8 vertex:** 0.100000-0.150000-0.130000-0.150000-0.800000-0.500000-0.200000-0.600000, fitted score **10**.

The F5 all-upper-bound choice remains 0.999999 in each coordinate; its cubic model predicts approximately **8,489** there, but the real output has not been returned.

### Additional data used in model comparisons

Classmates' publicly shared records informed supplementary **experimental models** and helped reveal underexplored areas; they have **not** been counted as this participant's own portal observations.

The supplementary research used publicly shared input-output histories, model-card benchmark results and selected positive-response observations. Individual contributors' names, account identifiers and repository URLs are intentionally excluded from this public version. Their specific attribution and references should be maintained separately for authorised academic review where required.

**Data handling:** Only peer coordinates inside the legal 0.000000–0.999999 range entered the legal-input polynomial and GP comparisons. In particular, an externally reported F5 result at (1, 1, 1, 1) was excluded from those fits as **outside the course portal bounds**. The original reported value is evidence of a boundary trend, not a legal candidate.

**Validation design:** The experimental polynomial models included linear, additive quadratic, additive cubic and full quadratic feature sets with different regularisation values. GP comparisons varied RBF/Matérn kernels, length scales, fixed noise terms and target transformations. Retrospective tests held out the author's Weeks 6–9 or later peer observations, as applicable.

**Crucial limitation:** Hyperparameters were compared and selected using small holdouts, and the external query histories are themselves adaptively generated. Those best-in-grid RMSE figures are **exploratory selection statistics**, not independently estimated deployment error. Peer improvements on different runs need not be directly comparable to this participant's scores without confirming identical evaluation conditions.

**Academic-use note:** Public accessibility is not consent for unrestricted assessed use. The participant must comply with programme collaboration and attribution rules when applying peer-observed outputs to assessed query design.

[Round 10 inputs](queries.txt) · [Measured returns](outputs.txt) · [Saved candidate comparisons](round10_candidates.csv) · [Methods](../../docs/methods.md)
