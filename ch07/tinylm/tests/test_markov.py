import time

import pytest

import tinylm


@pytest.fixture
def model() -> tinylm.Markov:
    return tinylm.Markov("abc", size=1)


@pytest.mark.fast
def test_predict_single_character(model: tinylm.Markov) -> None:
    assert model.predict("a") == "b"


@pytest.mark.fast
def test_predict_raises_keyerror(model: tinylm.Markov) -> None:
    with pytest.raises(KeyError, match="z not found"):
        model.predict("z")


@pytest.mark.fast
def test_get_table_counts() -> None:
    assert tinylm.get_table("xyxz") == {"x": {"y": 1, "z": 1}, "y": {"x": 1}}


@pytest.mark.slow
def test_slow_demo() -> None:
    time.sleep(0.02)
    assert True
