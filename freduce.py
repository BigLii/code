#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import reduce

def product2(num1,num2):
    return num1*num2
   
def prod(L):
    return reduce(product2,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')