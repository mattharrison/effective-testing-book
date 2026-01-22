from hypothesis import given
from hypothesis import strategies as st


@st.composite
def ordered_pairs(draw):
    left = draw(st.integers())
    right = draw(st.integers(min_value=left))
    return left, right


@given(pair=ordered_pairs())
def test_composite_strategy_can_generate_dependent_values(pair: tuple[int, int]) -> None:
    left, right = pair
    assert left <= right


@given(data=st.data(), string=st.text(min_size=1))
def test_data_draw_can_depend_on_previous_value(data, string: str) -> None:
    index = data.draw(st.integers(min_value=0, max_value=len(string) - 1))
    assert 0 <= index < len(string)
    assert len(string[index]) == 1
