import os
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
def test_get_table_counts() -> None:
    assert tinylm.get_table("xyxz") == {"x": {"y": 1, "z": 1}, "y": {"x": 1}}


@pytest.mark.skip(reason="demo: skipping a test with a fixed reason")
def test_skip_demo() -> None:
    raise AssertionError("skipped tests do not execute")


@pytest.mark.skipif(
    os.getenv("FEATURE_ALPHA") != "1",
    reason="missing feature flag: FEATURE_ALPHA",
)
def test_skipif_demo(model: tinylm.Markov) -> None:
    assert model.predict("a") == "b"


@pytest.mark.xfail(reason="demo: expected failure without breaking the suite")
def test_xfail_demo() -> None:
    assert 1 + 1 == 3


@pytest.mark.slow
def test_slow_demo() -> None:
    time.sleep(0.02)
    assert True
