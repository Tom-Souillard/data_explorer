import pytest
import pandas as pd
from data_explorer import DataExplorer

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'A': [1, 2, 2, None],
        'B': [5, None, 5, 5],
        'C': [10, 20, 20, 30]
    })

def test_load_data():
    file_path = 'examples/example_data.csv'
    data = DataExplorer.load_data(file_path)
    assert isinstance(data, pd.DataFrame), "Loaded data is not a DataFrame"
    assert not data.empty, "Loaded data is empty"

def test_clean_data(sample_data):
    clean_data = DataExplorer.clean_data(sample_data)
    assert clean_data.isnull().sum().sum() == 0, "Clean data contains null values"
    assert len(clean_data) == 2, "Clean data does not have the expected number of rows"

def test_analyze_data(sample_data):
    description, correlation = DataExplorer.analyze_data(sample_data)
    assert isinstance(description, pd.DataFrame), "Description is not a DataFrame"
    assert isinstance(correlation, pd.DataFrame), "Correlation is not a DataFrame"
    assert 'A' in description.columns, "Description does not contain column 'A'"
    assert 'B' in correlation.columns, "Correlation does not contain column 'B'"

def test_visualize_data(sample_data):
    # Since visualizations do not return values, we only ensure no errors occur.
    try:
        DataExplorer.visualize_data(sample_data)
    except Exception as e:
        pytest.fail(f"Visualization failed with exception: {e}")

if __name__ == '__main__':
    pytest.main()
