import os
import unittest

from configcalc import multiply_by_mode


class TestEnvTeardown(unittest.TestCase):
    def setUp(self) -> None:
        self._old_mode = os.environ.get("MODE")

    def tearDown(self) -> None:
        if self._old_mode is None:
            os.environ.pop("MODE", None)
        else:
            os.environ["MODE"] = self._old_mode

    def test_default_mode(self) -> None:
        os.environ.pop("MODE", None)
        self.assertEqual(multiply_by_mode(3), 3)

    def test_double_mode(self) -> None:
        os.environ["MODE"] = "double"
        self.assertEqual(multiply_by_mode(3), 6)


def test_pytest_style_restores_env_var() -> None:
    old_mode = os.environ.get("MODE")
    try:
        os.environ["MODE"] = "triple"
        assert multiply_by_mode(3) == 9
    finally:
        if old_mode is None:
            os.environ.pop("MODE", None)
        else:
            os.environ["MODE"] = old_mode

