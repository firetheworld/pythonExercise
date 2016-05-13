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


# def add(x, y):
#     return x * 10 + y
#
# r = reduce(add, [1, 2 ,3])
# print(r)
#
# def str2int(s):
#     def fn(x, y):
#         return x * 10 + y
#     def char2num(s):
#         return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
#     return reduce(fn, map(char2num, s))
#
# print(str2int('123456'))


# #filter
# def is_odd(n):
#     return n % 2 == 1
#
# l = list(filter(is_odd, [1, 2, 3, 4, 5, 6]))
# print(l)
#
# def _odd_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n
#
# def _not_divisible(n):
#     return lambda x: x % n > 0
#
# def primes():
#     yield 2
#     it = _odd_iter()
#     while True:
#         n = next(it)
#         yield n
#         it = filter(_not_divisible(n), it)
#
# for n in primes():
#     if n < 1000:
#         print(n)
#     else:
#         break


# #返回函数
# def lazy_sum(*args):
#     def sum():
#         sumNum = 0
#         for n in args:
#             sumNum = sumNum + n
#         return sumNum
#
#     return sum
#
# f = lazy_sum(1,2,3)
# print(f())

#装饰器

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return  func(*args, **kw)
    return wrapper

@log
def now():
    print('2016-05-08')


class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        if value == 'female' or value == 'male':
            self._gender = value
        else:
            raise ValueError('Must Female or Male')

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)

print('bart.name =', bart.name)
print('bart.score =', bart.score)
bart.print_score()

print('grade of Bart:', bart.get_grade())
print('grade of Lisa:', lisa.get_grade())

lisa.gender = 'female'
bart.gender = 'asd'
print(lisa.gender)
print(bart.gender)