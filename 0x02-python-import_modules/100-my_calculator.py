#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

for args in range(len(sys.argv[i])):
    if argv[args] != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if operator == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif operator == '-':
        print("{} + {} = {}".format(a, b, sub(a, b)))
    elif operator == "*":
        print("{} + {} = {}".format(a, b, mul(a, b)))
    elif operator == '/':
        print("{} + {} = {}".format(a, b, add(a, b)))
    else:
        print("{}".format("Unknown operator. Available operators: +, -, * and /"))
