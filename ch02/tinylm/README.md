# tinylm

A tiny Markov predictor used in the Effective Testing book.

To build a transition table from a training string:

    >>> from tinylm import get_table
    >>> get_table("xyxz")
    {'x': {'y': 1, 'z': 1}, 'y': {'x': 1}}

The table can be used to create a Markov model...
