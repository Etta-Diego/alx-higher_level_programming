#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    for ind in range(0, x):
        try:
            print(my_list[ind], end="")
            counter += 1
        except (Exception):
            break
    print()
    return counter
