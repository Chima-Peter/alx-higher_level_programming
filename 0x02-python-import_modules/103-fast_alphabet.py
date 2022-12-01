#!/usr/bin/python3
if __name__ == "__main__":
    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print("{}".format(i), end="") if (i != "Z") else print("{}".format("Z"))
