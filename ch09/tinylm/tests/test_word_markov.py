import pytest
from tinylm import WordMarkov

def test_predict_wonder():
    model = WordMarkov("Twinkle twinkle little star, how I wonder what you are")
    # In this nursery rhyme corpus, after "wonder" the next word should be "what"
    assert model.predict("wonder") == "what"

def test_predict_went():
    model = WordMarkov("Jack and Jill went up the hill to fetch a pail of water. "
                   "Jack fell down and broke his crown, and Jill came tumbling after")
    # In this nursery rhyme, after "went" the next word should be "up"
    assert model.predict("went") == "up"

@pytest.mark.parametrize("corpus, query, expected", [
    ("Twinkle twinkle little star, how I wonder what you are", "wonder", "what"),
    ("Jack and Jill went up the hill to fetch a pail of water. "
     "Jack fell down and broke his crown, and Jill came tumbling after", "went", "up"),
], ids=["Twinkle corpus: wonder->what", "JackJill corpus: went->up"])
def test_predict_next_word(corpus, query, expected):
    model = WordMarkov(corpus)
    result = model.predict(query)
    assert result == expected


@pytest.mark.parametrize("corpus, query, expected", [
    ("Twinkle twinkle little star, how I wonder what you are", "wonder", "what"),
    ("Jack and Jill went up the hill to fetch a pail of water. "
     "Jack fell down and broke his crown, and Jill came tumbling after", "went", "up"),
    pytest.param(
        "Twinkle twinkle little star, how I wonder what you are", 
        "are", "NOTUSED",
        id="no_next_word",
        marks=pytest.mark.xfail(reason="Known bug: end-of-sequence not handled")
    ),
])
def test_predict_edge_cases(corpus, query, expected):
    model = WordMarkov(corpus)
    result = model.predict(query)
    assert result == expected

def test_model_basic(model_first_second):
    model, first_word, second_word = model_first_second 
    # This test will run for each model (Twinkle and JackJill)
    # We can perform checks common to any corpus
    result = model.predict(first_word)
    assert isinstance(result, str) and result != ""


CORPUS_TWINKLE = "Twinkle twinkle little star, how I wonder what you are"
CORPUS_JACKJILL = ("Jack and Jill went up the hill to fetch a pail of water. "
                   "Jack fell down and broke his crown, and Jill came tumbling after")

@pytest.mark.parametrize("corpus, query", [
    (CORPUS_TWINKLE, "wonder"),
    pytest.param(CORPUS_TWINKLE, "went", marks=pytest.mark.skip(reason="no 'went' in Twinkle")),
    pytest.param(CORPUS_JACKJILL, "wonder", marks=pytest.mark.skip(reason="no 'wonder' in JackJill")),
    (CORPUS_JACKJILL, "went"),
])
def test_valid_combinations(corpus, query):
    model = WordMarkov(corpus)
    assert model.predict(query) is not None