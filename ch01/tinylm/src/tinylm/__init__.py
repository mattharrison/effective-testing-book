"""
A tiny Markov predictor used throughout this book.

The important part for Chapter 2 is that the examples are executable.

>>> get_table("xyxz")
{'x': {'y': 1, 'z': 1}, 'y': {'x': 1}}
"""

from __future__ import annotations

from __future__ import annotations

import random
from pathlib import Path
from typing import Dict


class Markov:
    def __init__(self, txt: str, size: int = 1) -> None:
        self.tables = [get_table(txt, size=i + 1) for i in range(size)]

    def predict(self, txt: str) -> str:
        """
        Predict the next character after ``txt``.

        This method uses randomness when there are multiple valid next characters.
        For doctests, prefer deterministic training text:

        >>> m = Markov("abc")
        >>> m.predict("a")
        'b'
        >>> m.predict("b")
        'c'

        Unknown inputs raise a ``KeyError``:

        >>> m.predict("z")
        Traceback (most recent call last):
          ...
        KeyError: 'z not found'
        """
        table = self.tables[len(txt) - 1]
        next_counts = table.get(txt, {})
        if not next_counts:
            raise KeyError(f"{txt} not found")
        options: list[str] = []
        for next_char, count in next_counts.items():
            options.extend([next_char] * count)
        return random.choice(options)


def get_table(txt: str, size: int = 1) -> Dict[str, Dict[str, int]]:
    """
    Build a transition table from a training string.

    The result is a nested dictionary mapping each observed token to the tokens
    that follow it and how often they appear.

    >>> get_table("xyxz")
    {'x': {'y': 1, 'z': 1}, 'y': {'x': 1}}

    A `size` larger than 1 uses substrings as keys:

    >>> get_table("abacab", size=2) == {'ab': {'a': 1}, 'ba': {'c': 1}, 'ac': {'a': 1}, 'ca': {'b': 1}}
    True
    """
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
