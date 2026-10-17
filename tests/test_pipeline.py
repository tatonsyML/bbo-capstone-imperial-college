from pathlib import Path
import pandas as pd

ROOT=Path(__file__).resolve().parents[1]
EXPECTED={1:19,2:19,3:24,4:39,5:29,6:29,7:39,8:49}

def test_observation_counts():
    for fn,n in EXPECTED.items():
        df=pd.read_csv(ROOT/'data'/'accumulated'/f'function_{fn}'/'observations_through_week9.csv')
        assert len(df)==n
        assert df['output'].notna().all()
