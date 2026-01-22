from __future__ import annotations

from pathlib import Path


def sum_file(path: Path) -> int:
    return sum(int(line) for line in path.read_text(encoding="utf-8").splitlines())

