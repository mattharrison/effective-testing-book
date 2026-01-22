import pytest

from tinylm import WordMarkov


def test_predicts_next_word_for_simple_training() -> None:
    model = WordMarkov("a b c")
    assert model.predict("a") == "b"


def test_missing_context_raises_keyerror() -> None:
    model = WordMarkov("a b c")
    with pytest.raises(KeyError, match="Context 'z' not found"):
        model.predict("z")
