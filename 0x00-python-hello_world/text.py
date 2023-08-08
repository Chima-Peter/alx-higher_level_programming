#!/usr/bin/python3
import dis

def add(a, b):
    a ** b
    return a + b
print(dis.dis(add))
