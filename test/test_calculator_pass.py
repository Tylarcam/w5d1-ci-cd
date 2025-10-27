from test.calculator import add, safe_divide
import math

def test_add_simple():
    assert add(2, 2) == 4

def test_safe_divide_regular():
    assert math.isclose(safe_divide(9, 3), 3.0)
