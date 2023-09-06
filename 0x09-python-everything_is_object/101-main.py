#!/usr/bin/python3
LockedClass = __import__('101-locked_class').LockedClass

lc = LockedClass()
lc.first_name = "John"
try:
    lc.first_ame = "Snow"
    print(lc.first_name)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

