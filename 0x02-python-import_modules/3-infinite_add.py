#!/usr/bin/python3

if name == "main":
    import sys, math
    result = 0
    for i in sys.argv:
        result += int(i)
        print("{}".format(result))
