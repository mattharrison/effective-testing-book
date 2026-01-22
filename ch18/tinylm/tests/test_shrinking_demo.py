import pytest
from hypothesis import given, settings, Verbosity
from hypothesis import strategies as st

from tinylm import Markov, WordMarkov


@pytest.mark.xfail(strict=True, reason="Demo for Hypothesis shrinking output")
@settings(database=None)
@given(txt=st.text(min_size=0, max_size=25))
def test_shrinking_demo_failing_property(txt: str) -> None:
    model = Markov("abc", size=1)
    table = model.get_table(txt, n=1)
    transition_count = sum(sum(next_counts.values()) for next_counts in table.values())
    assert transition_count > max(len(txt) - 1, 0)

@pytest.mark.xfail(strict=True, reason="Demo for Hypothesis shrinking output")
@settings(database=None, max_examples=2,
       verbosity=Verbosity.verbose)
@given(txt=st.text(alphabet="abc ", min_size=1, max_size=50))
def test_prediction_never_returns_unknown_token(txt: str) -> None:
    model = WordMarkov("a b c", size=1)
    prediction = model.predict(txt, default="?")
    assert prediction in txt.split()