"""
A tiny Markov predictor used throughout this book.
"""

import random
from typing import Dict


class Markov:
    def __init__(self, txt: str, size: int = 1) -> None:
        self.tables = [get_table(txt, size=i + 1) for i in range(size)]

    def predict(self, txt: str) -> str:
        """
        Predict the next character after `txt`.

        >>> m = Markov("abc")
        >>> m.predict("a")
        'b'
        >>> m.predict("b")
        'c'
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

    >>> get_table("xyxz")
    {'x': {'y': 1, 'z': 1}, 'y': {'x': 1}}
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


if __name__ == "__main__":
    import doctest

    doctest.testmod()
