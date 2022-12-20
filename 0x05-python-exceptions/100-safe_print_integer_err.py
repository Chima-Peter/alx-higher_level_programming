#!/usr/bin/python3
import sys
try:
    if value / 1 == value:
        print("{:d}".format(value))
    return True
except TypeError as tt:
    print("Exception: {}".format(tt), file=sys.stderr)
    return False
