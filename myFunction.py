#!/usr/bin/env python3

import math

def my_abs(x):

    if x >= 0 :
        return x
    else:
        return -x



def my_abs_checkParm(x):

    if not isinstance(x, (int, float)):
        return TypeError('bad operand type')
    if x > 0:
        return x
    else:
        return -x



def move(x, y, step, angle=0):

    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)

    return nx, ny



def findMax(x):

    if not isinstance(x, list):
        return TypeError('TypeError')

    maxNumber = 0

    for item in x:
        if item > maxNumber:
            maxNumber = item

    return maxNumber



# 注意:必选参数在前,默认在后
# 默认参数降低了函数调用的难度，而一旦需要更复杂的调用时，又可以传递更多的参数来实现。无论是简单调用还是复杂调用，函数只需要定义一个
# 因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了
# 定义默认参数要牢记一点：默认参数必须指向不变对象！
def power(x, n = 2):

    s = 1

    while n > 0:
        n = n - 1
        s = s * x

    return s