import tinylm as mc

def test_constructor() -> None:
    model = mc.Markov("abc")
    assert isinstance(model, mc.Markov)
    