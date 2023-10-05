#!/usr/bin/python3

import sys

args = len(sys.argv) - 1

if __name__ == "__main__":
    if (len(sys.argv) > 2 or len(sys.argv) == 1):
        print(args, "arguments:")
    else:
        print(args, "argument:")
    for i in range(len(sys.argv)):
        if ( i != 0):
            print(f"{i}: {sys.argv[i]}")
