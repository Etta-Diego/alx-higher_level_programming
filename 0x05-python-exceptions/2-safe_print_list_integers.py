#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    for ind in range(x):
        try:
            print("{:d}".format(my_list[ind]), end="")
            counter += 1
        except (ValueError, TypeError):
            pass
    print()
    return counter
