import tinylm as mc


def test_integration_markov_uses_overridden_corpus(markov: mc.Markov) -> None:
    assert markov.predict("h") == "e"

