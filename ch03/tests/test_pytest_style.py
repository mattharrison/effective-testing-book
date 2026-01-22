from pathlib import Path
import tempfile

from filecalc import sum_file


def test_sum_file_happy_path() -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        path = Path(tmpdir) / "nums.txt"
        path.write_text("1\n2\n3\n", encoding="utf-8")

        result = sum_file(path)

        assert result == 6


def test_sum_file_raises_valueerror_on_non_int() -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        path = Path(tmpdir) / "nums.txt"
        path.write_text("1\nnope\n3\n", encoding="utf-8")

        try:
            sum_file(path)
        except ValueError:
            pass
        else:
            raise AssertionError("expected ValueError")

