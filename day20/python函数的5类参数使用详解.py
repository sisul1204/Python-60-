#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:sisul
# time: 2020/7/14 17:28
# file: python函数的5类参数使用详解.py

from inspect import signature

def f(*,a, **b):
    print(f'a:{a}, b:{b}')

for name, val in signature(f).parameters.items():
    print(name, val.kind)

f(d=1, a=2, c=3)