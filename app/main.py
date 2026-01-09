from app.config.settings import NAME, VERSION, DEBUG
from app.utils.math_ops import add, subtract, multiply, divide, power
from app.utils.file_ops import save
from app.exceptions import InvalidOperationError, NegativeNumberError
import logging

logging.basicConfig(level=logging.INFO)
def run_calc(a=None, b=None, op=None):
    logging.info("App Started")
    print(f"App Name: {NAME}, Version: {VERSION}")
    try:
        a=int(input("Enter number 1: "))
        b=int(input("Enter number 2: "))

        if a<0 or b<0:
            raise NegativeNumberError("No negative numbers")
        else:
            pass
        op=input("Enter operation(+, -, *, /, **): ")
        logging.info(f"Operation {op} was chosen")

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
        logging.info("Calculation successful")

    except ValueError:
        logging.warning("Invalid number input")
        print("Please enter valid numbers.")

    except InvalidOperationError as e:
        logging.warning(str(e))
        print("Error:", e)

    except NegativeNumberError as e:
        logging.warning(str(e))
        print("Error:", e)

