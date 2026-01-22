from __future__ import annotations

from pathlib import Path

import tinylm.cli


def test_predict_prints_one_character(capsys) -> None:
    exit_code = tinylm.cli.main(["predict", "--training", "abc", "--prefix", "a"])
    assert exit_code == 0
    assert capsys.readouterr().out == "b\n"


def test_predict_can_read_training_from_file(tmp_path: Path, capsys) -> None:
    training_file = tmp_path / "training.txt"
    training_file.write_text("abc", encoding="utf-8")

    exit_code = tinylm.cli.main(
        ["predict", "--training-file", str(training_file), "--prefix", "a"]
    )
    assert exit_code == 0
    assert capsys.readouterr().out == "b\n"


def test_generate_emits_start_plus_generated_characters(capsys) -> None:
    exit_code = tinylm.cli.main(["generate", "--training", "abc", "--start", "a", "--count", "2"])
    assert exit_code == 0
    assert capsys.readouterr().out == "abc\n"


def test_generate_can_be_made_deterministic_with_seed(capsys) -> None:
    exit_code = tinylm.cli.main(
        ["generate", "--training", "abaca", "--start", "a", "--count", "5", "--seed", "0"]
    )
    assert exit_code == 0
    assert capsys.readouterr().out == "acabac\n"


def test_predict_reports_missing_training_as_exit_code_2(capsys) -> None:
    exit_code = tinylm.cli.main(["predict", "--prefix", "a"])
    assert exit_code == 2
    assert "training text is required" in capsys.readouterr().err


def test_predict_reports_invalid_prefix_length_cleanly(capsys) -> None:
    exit_code = tinylm.cli.main(["predict", "--training", "abc", "--prefix", "ab", "--size", "1"])
    assert exit_code == 2
    assert "exceeds model size" in capsys.readouterr().err

