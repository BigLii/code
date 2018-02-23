#! /usr/bin/env python
# -*- coding:utf-8 -*-
from functools import reduce

def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

def fn(x,y):
    return 10 * x + y

def str2float(s):
    s_new = ''
    length = len(s)
    for i in range(length):
        if s[i] != '.':
            s_new = s_new + s[i]
        else:
            num = i
    return reduce(fn,map(char2num,s_new))/(10**(length-num-1))


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')