from tinylm import WordMarkov


def test_default_used_when_context_missing() -> None:
    model = WordMarkov("a b c")
    assert model.predict("z", default="?") == "?"
