import pytest

CORPUS_TWINKLE = "Twinkle twinkle little star, how I wonder what you are"
CORPUS_JACKJILL = ("Jack and Jill went up the hill to fetch a pail of water. "
                   "Jack fell down and broke his crown, and Jill came tumbling after")

@pytest.mark.parametrize("markov_model, query, expected", [
    (CORPUS_TWINKLE, "wonder", "what"),
    (CORPUS_JACKJILL, "went", "up"),
], indirect=["markov_model"])
def test_predict_with_fixture(markov_model, query, expected):
    # The "markov_model" fixture received the corpus text and built a Markov instance
    result = markov_model.predict(query)
    assert result == expected