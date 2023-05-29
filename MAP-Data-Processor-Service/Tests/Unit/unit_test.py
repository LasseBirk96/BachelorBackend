
def cool_method(a, b):
    c = a + b
    return c


def test_cool_method():
    value = cool_method(2, 1)
    assert value == 3