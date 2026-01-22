from __future__ import annotations

import os


def is_enabled(flag: str, enabled: bool) -> bool:
    if enabled:
        return True
    return os.environ.get(flag, "") != ""
