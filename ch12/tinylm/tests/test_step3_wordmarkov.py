import pytest

from tinylm import WordMarkov


def test_empty_context_raises_valueerror() -> None:
    model = WordMarkov("a b c")
    with pytest.raises(ValueError, match="context must be non-empty"):
        model.predict("")
