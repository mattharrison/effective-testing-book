from ..shared.helpers import add


def test_can_import_helper() -> None:
    assert add(1, 2) == 3
