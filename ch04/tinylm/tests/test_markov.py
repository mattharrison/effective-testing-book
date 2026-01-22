import pytest

import tinylm as mc


def test_get_table() -> None:
    assert mc.get_table("xyxz") == {"x": {"y": 1, "z": 1}, "y": {"x": 1}}


def test_predict_deterministic() -> None:
    model = mc.Markov("abc")
    assert model.predict("a") == "b"
    assert model.predict("b") == "c"


def test_predict_unknown_raises() -> None:
    model = mc.Markov("abc")
    with pytest.raises(KeyError):
        model.predict("z")

