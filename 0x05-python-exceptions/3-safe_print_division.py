#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        return result
    except (ZeroDivisionError, ValueError):
        return None
    finally:
        if b == 0:
            result = None
            print("Inside result: {}".format(result))
        else:
            print("Inside result: {}".format(result))
