import os
import unittest

from tinylm import Markov


class TestAddCleanupForEnv(unittest.TestCase):
    def setUp(self) -> None:
        old_mode = os.environ.get("TINYLM_MODE")
        self.addCleanup(self._restore_env, "TINYLM_MODE", old_mode)

    def _restore_env(self, key: str, old_value) -> None:
        if old_value is None:
            os.environ.pop(key, None)
        else:
            os.environ[key] = old_value

    def test_env_is_restored_even_on_failure(self) -> None:
        os.environ["TINYLM_MODE"] = "demo"
        self.assertEqual(os.environ["TINYLM_MODE"], "demo")


class TestExpectedFailure(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.model = Markov("abc")

    @unittest.expectedFailure
    def test_expected_failure_example(self) -> None:
        # in the future, we might support length-2 predictions
        # for now, this test is expected to fail
        res = self.model.predict("ab")
        self.assertEqual(res, "c")


class TestSetUpClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.model = Markov("abc")

    def test_predict_a(self) -> None:
        self.assertEqual(self.model.predict("a"), "b")

    def test_predict_b(self) -> None:
        self.assertEqual(self.model.predict("b"), "c")

