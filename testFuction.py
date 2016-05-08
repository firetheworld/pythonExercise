#!/usr/bin/env python3

from myFunction import *
from functools import reduce

# print(my_abs(-12))

# x, y = move(100, 100, 60, math.pi / 6)
# print(x, y)

# numberList = [1, 20, -23, 234, 3458973,-1231231]
# print(findMax(numberList))


# name = input('Please input your name: ')
# print('hello, ',name)


# r = map(power,[1, 2, 3, 4])
# print(list(r))


def add(x, y):
    return x * 10 + y

r = reduce(add, [1, 2 ,3])
print(r)

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))

print(str2int('123456'))