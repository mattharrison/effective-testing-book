import unittest

import tinylm


class TestMarkov(unittest.TestCase):
    def setUp(self) -> None:
        self.model = tinylm.Markov("abc", size=1)

    def test_predict_single_character(self) -> None:
        self.assertEqual(self.model.predict("a"), "b")

    def test_predict_missing_key(self) -> None:
        with self.assertRaises(KeyError):
            self.model.predict("z")
