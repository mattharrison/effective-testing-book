import tempfile
import unittest
from pathlib import Path

import tinylm as mc


class TestMarkovSizeTwo(unittest.TestCase):
    def setUp(self) -> None:
        self.model = mc.Markov("abacab", size=2)

    def test_predict_ab(self) -> None:
        self.assertEqual(self.model.predict("ab"), "a")

    def test_predict_ba(self) -> None:
        self.assertEqual(self.model.predict("ba"), "c")


class TestTrainFromPath(unittest.TestCase):
    def test_train_from_path_builds_model(self) -> None:
        tmp = tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False)
        self.addCleanup(Path(tmp.name).unlink, missing_ok=True)
        try:
            tmp.write("abc")
        finally:
            tmp.close()

        model = mc.train_from_path(tmp.name)
        self.assertEqual(model.predict("a"), "b")

