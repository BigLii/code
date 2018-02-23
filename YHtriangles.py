#!/usr/bin/env python
# -*- coding:utf-8 -*-


#def triangles():
#    L = [1]
#    while True:
#        yield L
#        length = len(L)
#        L1 = [0] + L + [0]
#        L = []
#        for i in range(length+1): 
#            L.append(L1[i] + L1[i+1])

def triangles1():
    L = [1]
    while True:
        LL = L[:]
        yield LL
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]


def triangles():
    L = [1]
    while True:
        LL = L[:]
        yield L
        LL.append(0)
        L = [LL[i - 1] + LL[i] for i in range(len(LL))]       

n = 0
results = []
for t in triangles():
   # print(t)
    results.append(t)
    print ('results = ',results)
    print('t = ',t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
    print(results)