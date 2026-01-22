import os
import sys
from importlib import import_module
from unittest.mock import patch

import pytest

import tinylm


def test_monkeypatch_random_choice(monkeypatch) -> None:
    model = tinylm.Markov("abaca")
    assert set(tinylm.get_table("abaca")["a"].keys()) == {"b", "c"}

    def pick_first(options):
        return options[0]

    monkeypatch.setattr(tinylm.random, "choice", pick_first)
    assert model.predict("a") == "b"


def test_monkeypatch_chdir(monkeypatch, tmp_path) -> None:
    monkeypatch.chdir(tmp_path)
    assert tinylm.current_working_directory() == tmp_path


def test_monkeypatch_setenv_and_delenv(monkeypatch) -> None:
    assert tinylm.read_env("TESTING_BOOK_ENV", default=None) is None

    monkeypatch.setenv("TESTING_BOOK_ENV", "hello")
    assert tinylm.read_env("TESTING_BOOK_ENV", default=None) == "hello"

    monkeypatch.delenv("TESTING_BOOK_ENV", raising=False)
    assert tinylm.read_env("TESTING_BOOK_ENV", default=None) is None


def test_monkeypatch_setenv_prepend(monkeypatch) -> None:
    monkeypatch.setenv("PATH", "AAA")
    monkeypatch.setenv("PATH", "BBB", prepend=os.pathsep)
    assert tinylm.read_env("PATH") == f"BBB{os.pathsep}AAA"


def test_monkeypatch_delitem_and_setitem(monkeypatch) -> None:
    assert tinylm.uses_cache() is True
    monkeypatch.delitem(tinylm.FEATURE_FLAGS, "use_cache", raising=False)
    assert tinylm.uses_cache() is False
    monkeypatch.setitem(tinylm.FEATURE_FLAGS, "use_cache", True)
    assert tinylm.uses_cache() is True


def test_monkeypatch_delattr(monkeypatch) -> None:
    assert tinylm.timeout_seconds() == 10
    monkeypatch.delattr(tinylm, "DEFAULT_TIMEOUT", raising=True)
    with pytest.raises(NameError):
        tinylm.timeout_seconds()


def test_patch_missing_dependency(monkeypatch) -> None:
    monkeypatch.setattr(tinylm, "list_servers", lambda: ["alpha", "beta"])
    assert tinylm.choose_server() == "alpha"


def test_patch_slow_boundary(monkeypatch) -> None:
    monkeypatch.setattr(tinylm, "expensive_hash", lambda payload: "00deadbeef")
    assert tinylm.is_payload_valid("anything") is True


def test_monkeypatch_syspath_prepend(monkeypatch, tmp_path) -> None:
    module_path = tmp_path / "tempmod.py"
    module_path.write_text("VALUE = 42\n", encoding="utf-8")

    monkeypatch.syspath_prepend(str(tmp_path))
    module = import_module("tempmod")
    # Cleanup to avoid side effects on other tests
    monkeypatch.delitem(sys.modules, "tempmod", raising=False)

    assert module.VALUE == 42


def test_monkeypatch_context_limits_scope(monkeypatch) -> None:
    assert tinylm.read_env("TESTING_BOOK_CONTEXT", default=None) is None

    with monkeypatch.context() as mp:
        mp.setenv("TESTING_BOOK_CONTEXT", "scoped")
        assert tinylm.read_env("TESTING_BOOK_CONTEXT", default=None) == "scoped"

    assert tinylm.read_env("TESTING_BOOK_CONTEXT", default=None) is None


def test_unittest_mock_patch_object() -> None:
    model = tinylm.Markov("abaca")
    with patch.object(tinylm.random, "choice", return_value="b") as choice:
        assert model.predict("a") == "b"
        choice.assert_called_once_with(["b", "c"])

