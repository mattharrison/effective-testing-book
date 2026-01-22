import pytest


@pytest.mark.xfail(reason="demo: show assert rewriting")
def test_assert_introspection_and_capture() -> None:
    got = {"a": [1, 2]}
    expected = {"a": [1, 3]}
    print("debug: comparing got vs expected")
    assert got == expected

