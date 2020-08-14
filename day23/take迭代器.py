#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:sisul
# time: 2020/7/16 16:17
# file: take迭代器.py

'''
take迭代器
扫描列表，只要满足条件就从可迭代对象中返回元素，直到不满足条件为止，原型如下：
takewhile(predicate, iterable)
'''
# from itertools import takewhile
def takewhile(predicate, iterable):
    iterable = iter(iterable)
    for i in iterable:
        if predicate(i):
            yield i
        else:
            break

take_iterator = takewhile(lambda x:x<5, [1,4,9,4,1])
for i in take_iterator:
    print(i)