import sys

def demo() -> None:
    """
    takes the args from system input and 
    prints them out, as well as giving
    the total args given
    """
    args = sys.argv
    print("=== Command Quest ===")
    if len(args) == 1:
        print("No arguments provided!")
    print("Program name:", args[0])
    if len(args) > 1:
        print("Arguments received:", len(args) - 1)
    i = 1
    while i < len(args):
        print(f"Argument {i}: {args[i]}")
        i += 1
    print("Total arguments:", len(args))


demo()

