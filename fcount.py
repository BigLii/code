#! /usr/bin/env python
# -*- coding: utf-8 -*-
def createCounter():
    c = [0]
    def counter():
        c[0] =c[0] +1 #以list的形式，就可以做到每次调用都在原来的基础上+1
        return c[0]                     #而不是每次都从0开始
    return counter


counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('Pass!')
else:
    print('Failed!')