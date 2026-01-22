import tinylm as mc


def test_unit_corpus_override_is_not_parametrized(corpus: str) -> None:
    assert corpus == "123"


def test_unit_markov_uses_overridden_corpus(markov: mc.Markov) -> None:
    assert markov.predict("1") == "2"
