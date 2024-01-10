#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args_sum = 0
    """
    for arg in sys.argv[1:]:
        args_sum += int(arg)"""
    count = len(sys.argv)
    if count == 0:
        print("{:d}".format(args_sum))
    else:
        for args in range(1, count):
            args_sum += int(sys.argv[args])
    print("{:d}".format(args_sum))
