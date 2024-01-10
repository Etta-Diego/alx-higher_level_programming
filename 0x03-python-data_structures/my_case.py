def f(x):
    match x:
        case ["a"]:
            print("a, it is")
        case ['b']:
            print("b, it is")
        case _:
            print("Nothing")

if __name__ == "__main__":
    f(["a"])
