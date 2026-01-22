import random

import pytest

import tinylm as mc

_BUILD_COUNTS = {"abc_model": 0}


@pytest.fixture
def table():
    """A basic Markov table for 'abc'."""
    return mc.get_table("abc")


@pytest.fixture(params=["abc", "xyz", "123"], ids=["letters-abc", "letters-xyz", "digits-123"])
def corpus(request) -> str:
    return request.param


@pytest.fixture
def markov(corpus: str) -> mc.Markov:
    return mc.Markov(corpus)


@pytest.fixture
def sample_text_file(tmp_path):
    path = tmp_path / "sample.txt"
    path.write_text("hello fixtures\n", encoding="utf-8")
    return path


@pytest.fixture(scope="module")
def abc_model() -> mc.Markov:
    _BUILD_COUNTS["abc_model"] += 1
    return mc.Markov("abc")


@pytest.fixture
def abc_model_build_count() -> int:
    return _BUILD_COUNTS["abc_model"]


@pytest.fixture
def scratch_file(tmp_path):
    path = tmp_path / "scratch.txt"
    path.write_text("temporary\n", encoding="utf-8")
    yield path
    path.unlink(missing_ok=True)


@pytest.fixture
def fixed_random_seed():
    state = random.getstate()
    random.seed(0)
    yield
    random.setstate(state)

