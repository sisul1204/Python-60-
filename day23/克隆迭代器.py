#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:sisul
# time: 2020/7/16 16:33
# file: 克隆迭代器.py

'''
克隆迭代器
tee实现对原迭代器的复制，原型如下：
tee(iterable, n=2)
'''
from itertools import tee

from collections import deque

def tee(iterbale, n=2):
    it = iter(iterbale)
    deques = [deque() for i in range(n)]
    def gen(mydeque):
        while True:
            if not mydeque:
                pass



a = tee([1,4,6,4,1],2)
print(a)
print(a[0])
print(a[1])
print(next(a[0]))
print(next(a[1]))