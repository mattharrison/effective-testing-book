import pytest


def test_passes() -> None:
    assert 1 + 1 == 2


def test_skipped() -> None:
    pytest.skip("demo: skipping a test")


@pytest.mark.xfail(reason="demo: expected failure")
def test_xfail() -> None:
    assert 1 + 1 == 3

