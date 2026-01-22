"""
A tiny Markov predictor used throughout this book.
"""

import random
from typing import Callable

class Markov:
    def __init__(
        self,
        txt: str,
        size: int = 1,
        *,
        tokenize: Callable[[str], list[str]] | None = None,
        join: Callable[[list[str]], str] | None = None,
    ):
        self.size = size
        self._tokenize_fn = tokenize or list
        self._join_fn = join or "".join
        self.tables = [self.get_table(txt, n=i + 1) for i in range(size)]

    def _tokenize(self, txt: str) -> list[str]:
        return list(self._tokenize_fn(txt))

    def _join(self, tokens: list[str]) -> str:
        return self._join_fn(tokens)

    def get_table(self, txt: str, n: int) -> dict[str, dict[str, int]]:
        tokens : list[str] = self._tokenize(txt)
        results : dict[str, dict[str, int]] = {}

        for i in range(len(tokens) - n):
            context = self._join(tokens[i : i + n])
            next_token = tokens[i + n]

            token_dict = results.setdefault(context, {})
            token_dict[next_token] = token_dict.get(next_token, 0) + 1

        return results

    def predict(self, txt: str, *, default: str | None = None) -> str:
        tokens = self._tokenize(txt)

        if not tokens:
            raise ValueError("context must be non-empty")

        table_idx = len(tokens) - 1

        if table_idx < 0 or table_idx >= len(self.tables):
            raise KeyError(
                f"Context length {len(tokens)} is outside the model's range (1-{self.size})."
            )

        table = self.tables[table_idx]
        key = self._join(tokens)

        next_counts = table.get(key)
        if not next_counts:
            if default is not None:
                return default
            raise KeyError(f"Context '{key}' not found.")

        options = []
        for token, count in next_counts.items():
            options.extend([token] * count)

        return random.choice(options)


class WordMarkov(Markov):
    def __init__(self, txt: str, size: int = 1):
        super().__init__(txt, size=size, tokenize=str.split, join=" ".join)


__all__ = ["Markov", "WordMarkov"]
