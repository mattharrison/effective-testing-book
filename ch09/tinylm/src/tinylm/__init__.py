"""
A tiny Markov predictor used throughout this book.

>>> get_table("xyxz")
{'x': {'y': 1, 'z': 1}, 'y': {'x': 1}}
"""


from __future__ import annotations
import random
from typing import Dict, List, Sequence

class Markov:
    def __init__(self, txt: str, size: int = 1) -> None:
        self.size = size
        # Build tables for all n-gram lengths up to 'size'
        self.tables = [self.get_table(txt, n=i + 1) for i in range(size)]

    def _tokenize(self, txt: str) -> Sequence[str]:
        """Default tokenizer: splits into characters."""
        return list(txt)

    def _join(self, tokens: Sequence[str]) -> str:
        """Default joiner: combines characters into a string."""
        return "".join(tokens)

    def get_table(self, txt: str, n: int) -> Dict[str, Dict[str, int]]:
        tokens = self._tokenize(txt)
        results: Dict[str, Dict[str, int]] = {}
        
        for i in range(len(tokens) - n):
            context = self._join(tokens[i : i + n])
            next_token = tokens[i + n]
            
            token_dict = results.setdefault(context, {})
            token_dict[next_token] = token_dict.get(next_token, 0) + 1
            
        return results

    def predict(self, txt: str) -> str:
        tokens = self._tokenize(txt)
        # Choose table based on the number of tokens provided in the context
        table_idx = len(tokens) - 1
        
        if table_idx < 0 or table_idx >= len(self.tables):
            raise KeyError(f"Context length {len(tokens)} is outside the model's range (1-{self.size}).")

        table = self.tables[table_idx]
        key = self._join(tokens)
        
        next_counts = table.get(key)
        if not next_counts:
            raise KeyError(f"Context '{key}' not found.")

        # Weighted random choice
        options = []
        for token, count in next_counts.items():
            options.extend([token] * count)
        
        return random.choice(options)


class WordMarkov(Markov):
    def _tokenize(self, txt: str) -> List[str]:
        """Word tokenizer: splits by whitespace."""
        return txt.split()

    def _join(self, tokens: Sequence[str]) -> str:
        """Word joiner: joins words with a single space."""
        return " ".join(tokens)

def main() -> None:
    print("Hello from tinylm!")
