import pytest

import tinylm


def test_predict_unsupported_input_length_is_clear() -> None:
    model = tinylm.Markov("abc", size=1)
    with pytest.raises(ValueError, match="exceeds model size"):
        model.predict("ab")
