#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:sisul
# time: 2020/7/16 15:41
# file: 漏斗迭代器.py

'''
漏斗迭代器
compress函数，功能类似于漏斗功能，所以称它为漏斗迭代器，原型
compress(data, selectors)
经过selectors过滤后，返回一个更小的迭代器。

'''
# from itertools import compress

def compress(data, selectors):
    return (d for d, s in zip(data, selectors) if s)

compress_iter = compress('abcdefg', [1,2,3,0,5])
for i in compress_iter:
    print(i)