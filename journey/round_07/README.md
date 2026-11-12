# Round 7 · Module 18 | ARD models and prospective checks

**Evidence:** The [eight submitted inputs](queries.txt) and [eight returned outputs](outputs.txt) are historical portal records. The interpretation below is retrospective.

## My reasoning at the time

My attention shifted towards the hyperparameters that genuinely changed a query: **kernel family and smoothness, noise or regularisation, optimiser restarts and local-region width**. For F5, the large scale of the output also made the log transformation a modelling decision worth retaining and testing. I wanted to know not simply which Gaussian Process fitted existing points, but whether a change of setting produced a stable, better-informed next candidate.

I increasingly used **rolling-origin validation**. I could fit on observations that were available before a given portal return, record a forecast and compare it with the actual result. This mattered because adaptively gathered data are concentrated in places I previously chose to visit. A strong in-sample fit could therefore hide poor extrapolation. F2 and F6 had forecasts whose errors exceeded the model's reported uncertainty. Those failures made me less willing to interpret a narrow credible interval as a trustworthy decision.

F8 gave an instructive contrast: a Week 6 forecast of about **9.892098** was close to the actual **9.892073**. That strengthened confidence in the particular local pattern being tested, without proving the model globally correct. F1 still offered too little useful signal for ordinary local refinement. I continued to compare Matérn and RBF options, ARD length-scales and local-search geometry, but I wanted to stop tuning when plausible settings became indistinguishable in their decisions.

The strongest lesson in my weekly reflection was about **false precision**. An incomplete model should not be presented as more certain simply because its numerical predictions contain many decimal places. When a proposed gain is smaller than typical prospective forecast error, I should reconsider whether the portal query would answer anything useful. The original candidate-generating package for this particular round is not present in the surviving repository; the recorded methods and measured outputs are therefore evidence of my evolving approach, not proof of a newly reconstructed executable historical script.

## What I did

The work increasingly focused on ARD kernel choices and checking what a local model predicted against later observations.

## What happened

F1 → 1.3142530e-15; F5 → 5151.0477; F7 → 1.7557182; F8 → 9.8990020. That is 4 new personal bests in this round.

## What I learnt

F7 rose to 1.755718 and F5 to 5151.048, while F1 remained numerically negligible. Further local exploration needed to be justified by measured change.

## How I approached this round

I tuned GP kernel family, smoothness, noise, restarts and local-search width, and began judging forecasts with **rolling-origin validation**. F2 and F6 experienced errors larger than the models' stated uncertainty. By contrast, F8's Week 6 forecast **9.892098** was close to its actual **9.892073**. The lesson was to let forecast evidence determine how much authority a local model receives.


## Historical documentation

The Week 7 analysis covers rolling-origin validation and comparative forecast evidence. The standalone Module 18 candidate-generating package has not been retained, so these documented methods are not presented as a reproduced original script.

**Files:** [queries.txt](queries.txt) · [outputs.txt](outputs.txt) · [279-row dataset](../../data/all_observations.csv).
