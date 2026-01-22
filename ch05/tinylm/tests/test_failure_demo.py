#demonstration of a test failure in pytest

from tinylm import Markov

def test_failure_demo():
    model = Markov("abc")
    assert model.predict("a") == "b"
    assert model.predict("b") == "c"
    # this assertion is expected to fail
    assert model.predict("z") == "a"