import pytest

import tinylm as mc


def test_predict_happy_path() -> None:
    model = mc.Markov("abc")
    assert model.predict("a") == "b"


def test_predict_raises_keyerror() -> None:
    model = mc.Markov("abc")
    with pytest.raises(KeyError, match="not found"):
        model.predict("z")


@pytest.mark.parametrize(
    "txt, expected",
    [
        ("xyxz", {"x": {"y": 1, "z": 1}, "y": {"x": 1}}),
        ("aaa", {"a": {"a": 2}}),
    ],
)
def test_get_table(txt: str, expected) -> None:
    assert mc.get_table(txt) == expected

