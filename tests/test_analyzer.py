
import pytest
import pandas as pd
from src.analyzer import DataAnalyzer

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        "date": pd.date_range(start="2023-01-01", periods=3, freq="D"),
        "category": ["A", "B", "A"],
        "amount": [100, 200, 150],
        "customer_id": ["C1", "C2", "C1"]
    })

def test_summary_statistics(sample_df):
    analyzer = DataAnalyzer(sample_df)
    stats = analyzer.summary_statistics()
    assert "mean" in stats.columns

def test_top_categories(sample_df):
    analyzer = DataAnalyzer(sample_df)
    top = analyzer.top_categories()
    assert not top.empty
