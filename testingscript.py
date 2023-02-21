import pandas as pd
import pytest

# Create a dummy dataframe
data = {
    'name': ['Pawan', 'Ajay', 'Gosavi'],
    'age': [30, 25, 35]
}
df = pd.DataFrame(data)

@pytest.mark.parametrize("column", ["name"])
def test_strings_uppercase(df, column):
    assert df[column].str.isupper().all()

@pytest.mark.parametrize("column", ["name"])
def test_strings_lowercase(df, column):
    assert df[column].str.islower().all()