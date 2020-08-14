#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:sisul
# time: 2020/7/17 15:48
# file: 常用函数sorted.py

a = [{'name':'xiaoming','age':20,'gender':'male'},
     {'name':'xiaohong','age':18,'gender':'female'},
     {'name':'xiaoli','age':19,'gender':'male'}]

b = sorted(a, key=lambda x:x['age'], reverse=False)
print(b)