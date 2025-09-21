import pandas as pd

def filter_by_range(df: pd.DataFrame, col: str, low: float, high: float) -> pd.DataFrame:
    """Keep rows where col is within [low, high]."""
    return df[(df[col] >= low) & (df[col] <= high)].copy()

def filter_by_category(df: pd.DataFrame, col: str, keep: list[str]) -> pd.DataFrame:
    """Keep rows where col is in the keep list."""
    if not keep:
        return df.copy()
    return df[df[col].isin(keep)].copy()
