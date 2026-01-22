import unittest


class TestUnittestFeatures(unittest.TestCase):
    @unittest.skip("demo: skipping a unittest test")
    def test_skipped(self) -> None:
        self.fail("should not run")

    @unittest.expectedFailure
    def test_expected_failure(self) -> None:
        self.assertEqual(1 + 1, 3)
