# Round 7 · Module 18 | ARD models and prospective checks

**Evidence:** The [eight submitted inputs](queries.txt) and [eight returned outputs](outputs.txt) are historical portal records. The interpretation below is retrospective.

## What I did

The work increasingly focused on ARD kernel choices and checking what a local model predicted against later observations.

## What happened

F1 → 1.3142530e-15; F5 → 5151.0477; F7 → 1.7557182; F8 → 9.8990020. That is 4 new personal bests in this round.

## What I learnt

F7 rose to 1.755718 and F5 to 5151.048, while F1 remained numerically negligible. Further local exploration needed to be justified by measured change.

## Original weekly submission perspective

**Original Week 7 submission perspective:** I tuned GP kernel family, smoothness, noise, restarts and local-search width, and began judging forecasts with **rolling-origin validation**. F2 and F6 experienced errors larger than the models' stated uncertainty. By contrast, F8's Week 6 forecast **9.892098** was close to its actual **9.892073**. The lesson was to let forecast evidence determine how much authority a local model receives.

*Source: the author's 52-page private `Capstone Project.docx` collection of weekly submissions, reviewed during the [13-week evidence reconciliation](../../docs/WEEKLY_SUBMISSION_EVIDENCE.md). The original document remains private. Its reflections support the historical reasoning but do not replace portal returns or missing original scripts.*

## Historical documentation

The **original Week 7 written submission survives** in the private Word collection, including rolling-origin validation and comparative forecast evidence. The standalone Module 18 candidate-generating package has not been retained. The analysis and original script are separate forms of evidence; the missing code has not been reconstructed.

**Files:** [queries.txt](queries.txt) · [outputs.txt](outputs.txt) · [279-row dataset](../../data/all_observations.csv).
