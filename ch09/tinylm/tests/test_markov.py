import pytest

import tinylm


@pytest.mark.parametrize(
    "training, txt_in, expected",
    [
        pytest.param("abc", "a", "b", id="letters-abc"),
        pytest.param("xyz", "x", "y", id="letters-xyz"),
        pytest.param("123", "1", "2", id="digits-123"),
    ],
)
def test_predict_parametrized(training: str, txt_in: str, expected: str) -> None:
    model = tinylm.Markov(training)
    assert model.predict(txt_in) == expected


@pytest.mark.parametrize(
    "txt, expected",
    [
        pytest.param("xyxz", {"x": {"y": 1, "z": 1}, "y": {"x": 1}}, id="xyxz"),
        pytest.param("aaa", {"a": {"a": 2}}, id="aaa"),
    ],
)
def test_get_table(txt: str, expected) -> None:
    assert tinylm.get_table(txt) == expected


@pytest.mark.parametrize(
    "missing",
    [
        pytest.param("_", id="underscore"),
        pytest.param("?", id="question"),
        pytest.param("💥", id="boom"),
    ],
)
def test_predict_missing_raises(missing: str) -> None:
    model = tinylm.Markov("abc")
    with pytest.raises(KeyError, match="not found"):
        model.predict(missing)
