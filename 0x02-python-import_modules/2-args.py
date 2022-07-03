#!/usr/bin/python3

if __name__ == "__main__":
    """HAndle basic arithmetic operations."""
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.srgv) - 1 != 3:
        print("usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

        ops = {"+": add, "-": sub, "*" : mul, "/": div}
        if sys.argv[2]not in list(ops.key()):
            print("Unknown operator. Available operator: +, -, * and/")
            sys.exit(1)

            a = int(sys.argv[1])
            b = int(sys.argv[3])
            print("{} { {} = {}".format(a, sys.srgv[2], b, ops[sys.argv[2]](a, b)))
