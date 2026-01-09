from app.main import run_calc
import sys

if __name__ == "__main__":
    args = sys.argv

    if len(args) == 4:
        a = int(args[1])
        b = int(args[2])
        op = args[3]
        run_calc(a, b, op)
    else:
        run_calc()
