
import pytest
from src.data_loader import DataLoader

def test_load_data():
    loader = DataLoader("data/sample_data.csv")
    df = loader.load_data()
    assert not df.empty
    assert "date" in df.columns
