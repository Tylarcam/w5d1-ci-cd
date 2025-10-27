def add(a: float, b: float) -> float:
    return a + b

def safe_divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b
