#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:sisul
# time: 2020/7/14 15:07
# file: yield关键字和生成器.py
'''
yield
理解yield，可结合函数的返回值关键字return，yield是一种特殊的return。说是特殊的return，是因为执行遇到yield时，立即返回，这是与return的相似之处。
不同之处在于：下次进入函数时直接到yield的下一个语句，而return后再进入函数，还是从函数的第一行代码开始执行。
带yield的函数是生成器，通常与next函数结合用。下次进入函数，意思是使用next函数进入到函数体内
'''
def f():
    print('enter f...')
    return 'hello'

ret = f()
print(ret)
print('*'*100)

'''
send函数
'''
def f():
    print('enter f...')
    while True:
        result = yield 4
        if result:
            print('send me a value is:%d'%(result,))
            return
        else:
            print('no send')

g = f()
print(next(g))
print('ready to send')
# print(g.send(10))

print('*'*100)
'''
更多使用yield案例
1.完全展开list
'''
def deep_flatten(lst):
    for i in lst:
        if type(i) == list:
            yield from deep_flatten(i)
        else:
            yield i

gen = deep_flatten([1, ['s', 3], 4,5])
print(gen)
for i in gen:
    print(i)

'''
列表分组
'''
from math import ceil

def divide_iter(lst, n):
    if n <= 0:
        yield lst
        return
    i, div = 0, ceil(len(lst) / n)
    while i < n:
        yield lst[i * div: (i+1) * div]
        i += 1

print(list(divide_iter([1, 2, 3, 4, 5], 0)))
print(list(divide_iter([1, 2, 3, 4, 5], 2)))

'''
nonlocal关键字，声明为非局部变量
'''
def f():
    i = 0
    def auto_increase():
        nonlocal i
        if i >= 10:
            i = 0
        i += 1
    ret = []
    for _ in range(28):
        auto_increase()
        ret.append(i)
    print(ret)

f()

