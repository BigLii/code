#!/usr/bin/env python
# -*- coding: utf-8 -*-

def trim1(s):
    while True:
        if s == ' ' or s =='':
            s = ''
            break
        elif s[0] == ' ':
            s = s[1:]
        elif s[-1] == ' ':
            s = s[:-1]
        else:
            break

    return s


def trim(s):
    length = len(s)
    head = 0
    tail = 0
    for i in range(length):
        if s[i] != ' ':
            head = i
            break
    for i in range(length-1,-1,-1):
        if s[i] != ' ':
            tail = i
            break
    if head >= tail:
        s = ''
    else:
        s = s[head:tail+1]

    return s
    



if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('成功!')