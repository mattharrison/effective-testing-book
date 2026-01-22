import re

from hypothesis import given
from hypothesis import strategies as st


@given(code=st.from_regex(r"[0-9]{2,4}", fullmatch=True))
def test_from_regex_fullmatch_generates_2_to_4_digits(code: str) -> None:
    assert re.fullmatch(r"[0-9]{2,4}", code) is not None


@given(token=st.text(alphabet="ab🐍", min_size=5, max_size=8))
def test_text_alphabet_and_size_constraints(token: str) -> None:
    assert 5 <= len(token) <= 8
    assert set(token) <= {"a", "b", "🐍"}

