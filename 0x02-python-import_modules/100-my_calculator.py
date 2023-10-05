#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv
    from calculator_1 import add, sub, mul, div

    args = len(argv) - 1

    if args == 3:
        operator = argv[2]
        a = int(argv[1])
        b = int(argv[3])
        if operator == '+':
            answer = add(a, b)
            print('{:d} + {:d} = {:d}'.format(a, b, answer))
            exit(0)
        elif operator == '-':
            answer = sub(a, b)
            print('{:d} - {:d} = {:d}'.format(a, b, answer))
            exit(0)
        elif operator == '*':
            answer = mul(a, b)
            print('{:d} * {:d} = {:d}'.format(a, b, answer))
            exit(0)
        elif operator == '/':
            answer = div(a, b)
            print('{:d} / {:d} = {:d}'.format(a, b, answer))
            exit(0)
        else:
            print('Unknown operator. Available operators: +, -, * and /')
            exit(1)
    else:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
