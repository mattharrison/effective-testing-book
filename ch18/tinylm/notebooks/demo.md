---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: "1.3"
      jupytext_version: 1.18.1
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# Testing in a Notebook with ipytest

```python
import ipytest

ipytest.autoconfig()
```

```python
%%ipytest -qq

def add(a, b):
    return a + b


def test_add():
    assert add(1, 2) == 3
    assert add(2, 3) == 5
```

```python
%%ipytest -qq

import tinylm


def test_markov_predict_is_deterministic_for_simple_corpus():
    model = tinylm.Markov("abc")
    assert model.predict("a") == "b"
    assert model.predict("b") == "c"
```

