#! /usr/bin/env python
# -*- coding: utf-8 -*-
import time, functools
'''
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start = time.time()
        result = fn(*args, **kw)
        T = time.time() - start
        print('%s executed in %s ms' % (fn.__name__, T))
        return result
    return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
print('f=',f)
s = slow(11, 22, 33)
print('s=',s)
if f != 33:
    print('Failed!')
elif s != 7986:
    print('Failed!')
else:
    print('Passed')

'''

def log(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        print('begin calls %s() ' % fn.__name__)
        result = fn(*args, **kw)
        print('end calls %s() ' % fn.__name__)
        return result
    return wrapper

@log
def now():
    print("I'm not happy")

now()