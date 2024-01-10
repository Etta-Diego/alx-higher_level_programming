#!/usr/bin/python3
for c in range(122, 96, -1):
    alpha = ""
    if c % 2 != 0:
        alpha = c - 32
    else:
        alpha = c
    print("{}" .format(chr(alpha)), end="")
