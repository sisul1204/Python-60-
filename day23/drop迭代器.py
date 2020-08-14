#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:sisul
# time: 2020/7/16 15:57
# file: drop迭代器.py

'''
drop迭代器
扫描可迭代对象iterable，从不满足条件处往后全部保留，返回一个更小的迭代器。
原型如下：
    dropwhile(predicate, iterable)
'''
# from itertools import dropwhile

def dropwhile(predicate, iterable):
    it = iter(iterable)
    for x in it:
        if not predicate(x):
            yield x
            break
    for x in it:
        yield x



drop_iterator = dropwhile(lambda x:x<3, [1,0,2,4,1,1,3,5,-5])
for i in drop_iterator:
    print(i)