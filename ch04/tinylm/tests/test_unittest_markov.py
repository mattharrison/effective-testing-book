import random
import unittest

import tinylm as mc


class TestMarkov(unittest.TestCase):
    def setUp(self) -> None:
        self.model = mc.Markov("abc")

        old_state = random.getstate()
        random.seed(0)
        self.addCleanup(random.setstate, old_state)

    def test_predict_deterministic(self) -> None:
        self.assertEqual(self.model.predict("a"), "b")
        self.assertEqual(self.model.predict("b"), "c")

    def test_predict_unknown_raises_keyerror(self) -> None:
        with self.assertRaises(KeyError):
            self.model.predict("z")

    def test_get_table_subtests(self) -> None:
        cases = [
            ("xyxz", {"x": {"y": 1, "z": 1}, "y": {"x": 1}}),
            ("abca", {"a": {"b": 1}, "b": {"c": 1}, "c": {"a": 1}}),
        ]
        for txt, expected in cases:
            with self.subTest(txt=txt):
                self.assertEqual(mc.get_table(txt), expected)


@unittest.skipIf(True, "example skip for the book")
class TestSkipping(unittest.TestCase):
    def test_skipped_example(self) -> None:
        self.fail("should be skipped")

