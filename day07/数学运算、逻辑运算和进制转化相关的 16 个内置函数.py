#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:sisul
# time: 2020/7/7 17:39
# file: 数学运算、逻辑运算和进制转化相关的 16 个内置函数.py


'''数学运算'''
#len(s)
dic = {'a':1,'b':3}
print(len(dic))

#max(iterable,*[,key,default])
print(max(3,1,4,2,1))

print(max((), default=0))

di = {'a':3,'b1':1,'c':4}
print(max(di))

a = [{'name':'xiaoming','age':18,'gender':'male'},{'name':'xiaohong','age':20,'gender':'female'}]
print(max(a, key=lambda x: x['age']))

def max_length(*lst):
    return max(*lst, key=lambda x:len(x))
print(max_length([1, 2, 3], [4, 5, 6, 7], [8]))
