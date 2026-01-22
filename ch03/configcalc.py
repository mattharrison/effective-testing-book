from __future__ import annotations

import os


def multiply_by_mode(value: int) -> int:
    mode = os.environ.get("MODE", "").lower().strip()
    if mode == "double":
        return value * 2
    if mode == "triple":
        return value * 3
    return value

