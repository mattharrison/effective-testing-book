import unittest


class TestUnittestFeatures(unittest.TestCase):
    def test_subtest_demo(self) -> None:
        cases = [(1, 2, 3), (10, 20, 30)]
        for left, right, expected in cases:
            with self.subTest(left=left, right=right):
                self.assertEqual(left + right, expected)

