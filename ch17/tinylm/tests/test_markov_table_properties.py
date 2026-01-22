from __future__ import annotations

from hypothesis import given, settings
from hypothesis import strategies as st

import tinylm


def _transition_count(table: dict[str, dict[str, int]]) -> int:
    return sum(sum(next_counts.values()) for next_counts in table.values())


@settings(max_examples=10)
@given(txt=st.text(min_size=0, max_size=25), n=st.integers(min_value=1, max_value=3))
def test_get_table_counts_match_token_count(txt: str, n: int) -> None:
    print(f'called with txt={txt!r} n={n}')
    model = tinylm.Markov("abc", size=1)
    table = model.get_table(txt, n=n)
    expected = max(len(txt) - n, 0)
    assert _transition_count(table) == expected


@settings(max_examples=50)
@given(txt=st.text(min_size=0, max_size=25), n=st.integers(min_value=1, max_value=3))
def test_get_table_keys_are_n_tokens(txt: str, n: int) -> None:
    model = tinylm.Markov("abc", size=1)
    table = model.get_table(txt, n=n)
    assert all(len(key) == n for key in table)


@settings(max_examples=50)
@given(txt=st.text(min_size=0, max_size=25), n=st.integers(min_value=1, max_value=3))
def test_get_table_counts_are_positive(txt: str, n: int) -> None:
    model = tinylm.Markov("abc", size=1)
    table = model.get_table(txt, n=n)
    assert all(count > 0 for next_counts in table.values() for count in next_counts.values())

if __name__ == "__main__":
    print('running test_get_table_keys_are_n_tokens()')
    test_get_table_counts_match_token_count()
    