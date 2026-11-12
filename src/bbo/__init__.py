"""Shared implementation for the black-box optimisation capstone.

The modules in this package support Gaussian Process modelling, candidate
selection, historical data checks and mathematical reconstructions. They
operate on recorded observations or produce unscored suggestions; they do
not evaluate the course's private black-box objective functions.

The project records and initial observations remain under data/ and journey/.
For full official HEBO / TuRBO-1 post-capstone experiments, see
research/full_optimisers/ rather than treating our small historical
HEBO-inspired and TuRBO-style functions as full implementations.
"""

__version__ = '0.4.0'
