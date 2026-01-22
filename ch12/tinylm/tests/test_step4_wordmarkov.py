import pytest

from tinylm import WordMarkov


def test_context_length_outside_range_raises_keyerror() -> None:
    model = WordMarkov("a b c", size=1)
    with pytest.raises(KeyError, match=r"Context length 2 is outside the model's range"):
        model.predict("a b")
