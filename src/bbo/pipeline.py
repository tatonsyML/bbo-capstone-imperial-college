from __future__ import annotations
from pathlib import Path
import pandas as pd
from .diagnostics import load_function, current_best, f8_additive_quadratic
from .optimizer import hebo_inspired_committee, turbo_style_candidate


def run(repo_root=None):
    root=Path(repo_root or Path(__file__).resolve().parents[2])
    print('Current best through Week 9')
    print(current_best(root).to_string(index=False))
    print('\nChallenger summary')
    rows=[]
    for fn in range(1,9):
        X,y=load_function(root,fn)
        h=hebo_inspired_committee(X,y,seed=100+fn)
        t=turbo_style_candidate(X,y,seed=900+fn)
        rows.append({'Function':fn,'HEBO_inspired':h.sort_values('robust_rank').iloc[-1]['candidate'],'TuRBO_style':t['candidate']})
    print(pd.DataFrame(rows).to_string(index=False))
    _,x,y,err=f8_additive_quadratic(root)
    print(f'\nF8 structural candidate: {"-".join(f"{v:.6f}" for v in x)} -> {y:.12f}; max residual {err:.3e}')


if __name__=='__main__':
    run()
