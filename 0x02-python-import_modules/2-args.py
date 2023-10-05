#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    args = len(sys.argv) - 1

    if (len(sys.argv) > 2):
        print(args, "arguments:")
    elif (len(sys.argv) == 1):
        print(args, "arguments.")
    else:
        print(args, "argument:")
    for i in range(1, len(sys.argv)):
        print("{:d}: {}".format(i, sys.argv[i]))
