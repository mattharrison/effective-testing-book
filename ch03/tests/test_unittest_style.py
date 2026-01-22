from pathlib import Path
import tempfile
import unittest

from filecalc import sum_file


class TestSumFile(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.path = Path(self._tmp.name) / "nums.txt"
        self.path.write_text("1\n2\n3\n", encoding="utf-8")

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def test_sum_file(self) -> None:
        result = sum_file(self.path)
        self.assertEqual(result, 6)

