import pytest
import tinylm

# mark as expected failure due to type error
@pytest.mark.xfail(raises=TypeError)
def test_get_table_with_invalid_type():
    model = tinylm.Markov("abc", size=1)
    table = model.get_table(123, n=1)  # Wrong type!