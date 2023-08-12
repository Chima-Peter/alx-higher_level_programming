#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    import sys

    if len(sys.argv) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operator = ["+", "-", "*", "/"]
    for i in operator:
        if sys.argv[2] != i:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    print("{} {} {} = {}".format(a, b, sys.argv[2], calc.add(a, b)))
    print("{} {} {} = {}".format(a, b, sys.argv[2], calc.sub(a, b)))
