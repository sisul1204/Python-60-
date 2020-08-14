#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:sisul
# time: 2020/7/17 15:41
# file: 123高阶函数reduce.py

from functools import reduce

res = reduce(lambda x,y:x+y, range(101))
print(res)