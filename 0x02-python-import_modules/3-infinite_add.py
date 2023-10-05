#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    av = sys.argv
    total = 0

    if len(av) == 1:
        print(total)

    else:
        for i in range(1, len(av)):
            total = total + int(av[i])

        print(total)
