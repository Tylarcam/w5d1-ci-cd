from app.calculator import add, safe_divide
import pytest

def test_add_incorrect_on_purpose():
    # Intentional mistake to trigger a failing CI run.
    # You will fix this later to == 5.
    assert add(2, 3) == 6

def test_safe_divide_zero_error():
    with pytest.raises(ZeroDivisionError):
        safe_divide(1, 0)
