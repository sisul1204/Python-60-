#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:sisul
# time: 2020/7/16 15:23
# file: 实现accumulate.py
import operator


def accumulate(iterable, func=operator.add, *, initial=None):
    it = iter(iterable)
    total = initial
    if initial is None:
        try:
            total = next(it)
        except StopIteration:
            return
    yield total
    for element in it:
        total = func(total, element)
        yield total

accu_iterator = accumulate([1,2,3,4,5,6], lambda x,y:x*y)
for i in accu_iterator:
    print(i)

