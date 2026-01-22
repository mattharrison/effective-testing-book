def add(a, b):
    return a + b

def test_pdb_demo():
    res = add(2, 2)
    assert res == 5  # Intentional failure to demonstrate pdb usage
        

def test_raise_exception():
    name = 'matt'
    raise ValueError("This is a test exception for pdb demonstration")

def test_no_fail_breakpoint():
    breakpoint()  # This will not cause a failure
    assert True