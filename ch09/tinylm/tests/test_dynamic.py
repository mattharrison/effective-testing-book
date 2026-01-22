from tinylm import WordMarkov
# content of tests/test_dynamic.py
def test_corpus_min_length(corpus):
    model = WordMarkov(corpus)
    # This test simply checks that the model learned at least one word
    assert len(model.tables) > 0