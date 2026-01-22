import tinylm as mc

def test_basic_markov_functionality() -> None:
    model = mc.Markov("abc")
    assert model.predict("a") == "b"
    assert model.predict("b") == "c"
