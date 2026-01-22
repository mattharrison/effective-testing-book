import unittest

import tinylm


class TestMarkovSizeTwo(unittest.TestCase):
    def test_size_two_is_deterministic_for_simple_training_data(self) -> None:
        model = tinylm.Markov("abcd", size=2)
        self.assertEqual(model.predict("ab"), "c")
