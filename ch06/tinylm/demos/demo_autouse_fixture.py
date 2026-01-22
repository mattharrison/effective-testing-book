import random

import pytest

import tinylm as mc


@pytest.fixture(autouse=True)
def fixed_random_seed():
    state = random.getstate()
    random.seed(0)
    yield
    random.setstate(state)


def test_autouse_fixture_makes_predict_deterministic() -> None:
    model = mc.Markov("abac")
    assert model.predict("a") == "c"

