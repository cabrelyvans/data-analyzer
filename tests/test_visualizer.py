
import pytest
import pandas as pd
from src.visualizer import DataVisualizer

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        "date": pd.date_range(start="2023-01-01", periods=3, freq="D"),
        "category": ["A", "B", "A"],
        "amount": [100, 200, 150],
        "customer_id": ["C1", "C2", "C1"]
    })

def test_bar_chart_by_category(sample_df):
    viz = DataVisualizer(sample_df)
    fig = viz.bar_chart_by_category()
    assert fig is not None

def test_line_chart_over_time(sample_df):
    viz = DataVisualizer(sample_df)
    fig = viz.line_chart_over_time()
    assert fig is not None
