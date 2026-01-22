import pytest
from tinylm import WordMarkov

CORPUS_TWINKLE = "Twinkle twinkle little star, how I wonder what you are"
CORPUS_JACKJILL = ("Jack and Jill went up the hill to fetch a pail of water. "
                   "Jack fell down and broke his crown, and Jill came tumbling after")


@pytest.fixture(params=[CORPUS_TWINKLE, CORPUS_JACKJILL], ids=["Twinkle", "JackJill"])
def model_first_second(request):
    corpus_text = request.param
    print(f"\n[SETUP] Creating model for {request.param[:8]}...")
    return WordMarkov(corpus_text), corpus_text.split()[0], corpus_text.split()[1]
    

@pytest.fixture
def markov_model(request):
    # request.param will hold the corpus string passed indirectly
    corpus_text = request.param
    print(f"\n[SETUP] Building Markov model for corpus: {corpus_text[:15]}...")
    return WordMarkov(corpus_text)

# content of tests/conftest.py (dynamic param with hook)
def pytest_addoption(parser):
    parser.addoption("--all-corpora", action="store_true", help="run tests on all corpora")

# Suppose we have some corpus data defined somewhere:
CORPUS_SMALL = "Twinkle twinkle little star, how I wonder what you are"
CORPUS_MEDIUM = "Jack and Jill went up the hill to fetch a pail of water. ... (etc)"
CORPUS_LARGE = "Call me Ishmael. Some years ago — having little or no money ... (etc)"

def pytest_generate_tests(metafunc):
    if "corpus" in metafunc.fixturenames:
        if metafunc.config.getoption("--all-corpora"):
            # Use a larger set of corpora
            corpora = [CORPUS_SMALL, CORPUS_MEDIUM, CORPUS_LARGE]
        else:
            # Default: only a quick small corpus
            corpora = [CORPUS_SMALL]
        metafunc.parametrize("corpus", corpora)