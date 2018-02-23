#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
def count():
    def f(j):
        return j*j
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs

print(f1)
print(f2)
print(f3)

'''



def count():
    def f(j):
        def g(): ##我觉得，这个才是返回函数，外面的是在调用了？？
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f1, f2, f3 = count()
print(count())
print(f1())
print(f2())
print(f3())
