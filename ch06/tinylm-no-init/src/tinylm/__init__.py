"""
A tiny Markov predictor used throughout this book.

Chapter 6 uses this code to demonstrate pytest fixtures.
"""

from __future__ import annotations

import random
from pathlib import Path
from typing import Dict


class Markov:
    def __init__(self, txt: str, size: int = 1) -> None:
        self.tables = [get_table(txt, size=i + 1) for i in range(size)]

    def predict(self, txt: str) -> str:
        table = self.tables[len(txt) - 1]
        next_counts = table.get(txt, {})
        if not next_counts:
            raise KeyError(f"{txt} not found")
        options: list[str] = []
        for next_char, count in next_counts.items():
            options.extend([next_char] * count)
        return random.choice(options)


def get_table(txt: str, size: int = 1) -> Dict[str, Dict[str, int]]:
    results: Dict[str, Dict[str, int]] = {}
    for i in range(len(txt)):
        chars = txt[i : i + size]
        try:
            out = txt[i + size]
        except IndexError:
            break
        char_dict = results.get(chars, {})
        char_dict.setdefault(out, 0)
        char_dict[out] += 1
        results[chars] = char_dict
    return results


def train_from_path(path: str | Path, size: int = 1) -> Markov:
    txt = Path(path).read_text(encoding="utf-8")
    return Markov(txt, size=size)


def main() -> None:
    print("Hello from tinylm!")

