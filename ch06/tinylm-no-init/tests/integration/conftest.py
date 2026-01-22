import pytest


@pytest.fixture
def corpus() -> str:
    return "hello fixtures\n"

