import pytest

import tinylm as mc

@pytest.fixture
def sample_text_file(tmp_path, corpus):
    path = tmp_path / "sample.txt"
    path.write_text(corpus)
    return path

def test_train_from_path(sample_text_file, corpus) -> None:
    model = mc.train_from_path(sample_text_file)
    assert model.tables[0] == mc.get_table(corpus)

def test_table_fixture(table) -> None:
    assert table == {"a": {"b": 1}, "b": {"c": 1}}


def test_parametrized_markov_fixture(corpus: str, markov) -> None:
    assert markov.predict(corpus[0]) == corpus[1]


def test_exception_with_fixture(markov) -> None:
    with pytest.raises(KeyError):
        markov.predict("_")


def test_fixture_dependency(table) -> None:
    model = mc.Markov("abc")
    assert model.tables[0] == table





def test_module_scoped_fixture_built_once(abc_model, abc_model_build_count) -> None:
    assert abc_model.predict("a") == "b"
    assert abc_model_build_count == 1


def test_yield_fixture_cleanup_pattern(scratch_file) -> None:
    assert scratch_file.read_text(encoding="utf-8") == "temporary\n"


def test_fixture_can_control_global_state(fixed_random_seed) -> None:
    model = mc.Markov("abac")
    assert model.predict("a") == "c"

@pytest.fixture
def another_fixed_seed():
    import random
    state = random.getstate()
    print(f'state: {state}')
    random.seed(42)
    yield
    random.setstate(state)  # Reset to system time or entropy source

def test_another_with_fixed_seed(another_fixed_seed):
    model = mc.Markov("abac")
    assert model.predict("a") == "b"
