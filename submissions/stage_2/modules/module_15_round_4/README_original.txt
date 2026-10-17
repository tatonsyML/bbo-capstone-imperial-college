Capstone BBO Week 4 / Module 15
================================

Files
-----
1. Capstone_BBO_Week4_Module15.ipynb
   Executed Jupyter notebook with the analysis and displayed results.

2. capstone_bbo_week4_module15.py
   Standalone Python version of the same analysis.

3. source_data/
   - Initial_data_points_starter(1).zip
   - inputs_rounds_1_to_3.txt
   - outputs_rounds_1_to_3.txt

4. results/
   - progression_summary.csv
   - gp_summary.csv
   - classification_cv.csv
   - rbf_support_vectors.csv
   - nn_gradient_summary.csv
   - regression_cv.csv
   - round4_queries.csv
   - round4_portal_values.txt

Method
------
- Gaussian Process is retained as the primary surrogate because it provides both a
  prediction and uncertainty.
- The top third of observed outputs are labelled 'good' for diagnostic classification.
- Logistic regression, linear SVM, Gaussian RBF-kernel SVM, and a small neural
  network classifier are compared with stratified cross-validation.
- Formal RBF-SVM support vectors are counted to assess how much of the sparse data
  is involved in defining the current boundary.
- A small one-hidden-layer NN regressor is fitted repeatedly across random seeds.
  Local input sensitivities are estimated by finite differences at the current best
  observed point. Sign consistency is used as a simple robustness check.
- Linear regression and the small NN are compared using cross-validated normalised
  RMSE. Lower is better.
- Round 4 points are stored explicitly because final selection was hybrid and
  function-specific, combining GP evidence, observed local performance, boundary
  checks, NN sensitivity, and exploration/exploitation judgement.

Verification note
-----------------
The clean reproducible rerun supports Function 5 x2/x4 particularly strongly in the
NN regression sensitivity check. For Function 7, x1 is a robust local signal, while
other dimensions vary more across fitted networks. This is useful evidence in its own
right: disagreement should reduce confidence rather than be hidden.

How to run
----------
Unzip the package, keep the source_data folder next to the notebook/script, then:

  python capstone_bbo_week4_module15.py

or open Capstone_BBO_Week4_Module15.ipynb in Jupyter and run all cells.

Dependencies
------------
numpy, pandas, scikit-learn, scipy/Jupyter (for the notebook environment).
TensorFlow is not required; the small neural network is implemented with scikit-learn's
MLP classes so the analysis is self-contained and reproducible in this environment.