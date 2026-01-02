from app.config.settings import NAME, VERSION, DEBUG
from app.utils.math_ops import add, subtract, multiply, divide, power
from app.utils.file_ops import save
from app.exceptions import InvalidOperationError


def run_calc():
    print(f"App Name: {NAME}, Version: {VERSION}")
    a=int(input("Enter number 1: "))
    b=int(input("Enter number 2: "))
    op=input("Enter operation(+, -, *, /, **): ")

    if op == "+":
        result = add(a, b)
    elif op == "-":
        result = subtract(a, b)
    elif op == "*":
        result = multiply(a, b)
    elif op == "/":
        result = divide(a, b)
    elif op == "**":
        result = power(a, b)
    else:
        raise InvalidOperationError("Operation not supported")


    print("Result:", result)
    save(result)