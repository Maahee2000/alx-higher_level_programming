#!/usr/bin/python3

def main():
    arglen = len(argv) - 1
    if not arglen:
        print("0 argument. ")
        return

    print("{:d} argument{:s}:".format(arglen, "s" if arglen > 1 else ""))

    """loop through argument and print"""
    for index in range(1, arglen + 1):
        print(f"{index:d}: {argv[index]:s}")

        if __name__ == "__mai__":
            main()
