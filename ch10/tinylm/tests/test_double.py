import tinylm

class StubWordMarkov(tinylm.WordMarkov):
    def predict(self, txt: str) -> str:
        # Bypass randomness with a fixed response
        return "world"

def test_wordmarkov_with_test_double():
    model = StubWordMarkov("hello world hello there")
    
    # This test doesn't care how the model predicts — just that we can use it
    response = model.predict("hello")
    
    assert response == "world"
