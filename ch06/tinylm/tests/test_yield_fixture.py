import pytest
from pathlib import Path

@pytest.fixture
def scratch_file(tmp_path: Path):
    path = tmp_path / "scratch.txt"
    path.write_text("temp\n")
    print("SETUP: file created")
    yield path
    print("TEARDOWN: deleting file")
    path.unlink(missing_ok=True)

@pytest.mark.xfail(strict=True, reason="Demo: show yield-fixture teardown on failure")
def test_failure_triggers_teardown(scratch_file: Path):
    print("TEST: failing intentionally")
    assert False, "intentional failure"
