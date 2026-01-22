# tests/test_scope.py

import pytest
from tinylm import Markov, train_from_path, get_table
from pathlib import Path

# SESSION: Load static training data once for all tests
@pytest.fixture(scope="session")
def training_text() -> str:
    # In a real project, this might be a big string from a file or resource
    return "abcabcabcabcabc"

# MODULE: Build a Markov model once per module
@pytest.fixture(scope="module")
def model(training_text: str) -> Markov:
    return Markov(training_text, size=2)

# CLASS: Create a temporary file once per class (to simulate I/O setup)
@pytest.fixture(scope="class")
def text_file(tmp_path_factory) -> Path:
    file = tmp_path_factory.mktemp("data") / "sample.txt"
    file.write_text("tuvwxyz")
    return file

# FUNCTION: Fresh call for test-level inspection
@pytest.fixture(scope="function")
def fresh_table(training_text: str) -> dict:
    return get_table(training_text, size=1)

def test_model_has_correct_size(model):
    assert len(model.tables) == 2

def test_model_predicts_valid_next(model):
    result = model.predict("ab")
    assert result in {"c"}

def test_missing_key_raises(model):
    with pytest.raises(KeyError):
        model.predict("zz")

class TestTrainFromPath:
    def test_train_from_path(self, text_file):
        model = train_from_path(text_file, size=1)
        assert isinstance(model, Markov)
        assert model.predict("x") in {"y"}

    def test_train_raises_keyerror(self, text_file):
        model = train_from_path(text_file, size=1)
        with pytest.raises(KeyError):
            model.predict("z")  # 'z' is followed by no character in final position

def test_fresh_table_has_expected_keys(fresh_table):
    # This runs get_table(training_text, size=1) per test
    assert "a" in fresh_table
    assert "b" in fresh_table
