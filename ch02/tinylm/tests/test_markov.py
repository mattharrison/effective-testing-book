"""
Basic tests for tinylm
"""
import tinylm


def test_get_table():
    assert tinylm.get_table("xyxz") == {"x": {"y": 1, "z": 1}, "y": {"x": 1}}


def test_predict_deterministic():
    model = tinylm.Markov("abc")
    assert model.predict("a") == "b"
    assert model.predict("b") == "c"
