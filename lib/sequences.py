#!/usr/bin/env python3

# def print_fibonacci(length):
#     list = []
#     print(list)

def print_fibonacci(length):
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    else:
        a, b = 0, 1
        result = [a]
        while len(result) < length:
            a, b = b, a + b
            result.append(a)
        print(result)

    