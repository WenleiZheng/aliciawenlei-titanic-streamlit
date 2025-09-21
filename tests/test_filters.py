import pandas as pd
from app.utils.filters import filter_by_range, filter_by_category

def test_filter_by_range():
    df = pd.DataFrame({"v":[0,5,10]})
    out = filter_by_range(df, "v", 1, 9)
    assert out["v"].tolist() == [5]

def test_filter_by_category():
    df = pd.DataFrame({"c":["A","B","A"], "x":[1,2,3]})
    out = filter_by_category(df, "c", ["A"])
    assert len(out) == 2
    assert set(out["c"]) == {"A"}
