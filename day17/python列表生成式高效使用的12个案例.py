#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:sisul
# time: 2020/7/13 9:14
# file: python列表生成式高效使用的12个案例.py

'''
1.数据再运算
实现对每个元素的乘方操作后，利用列表生成式返回一个新的列表

'''
a = range(11)
b = [x ** 2 for x in a]
print(b)

'''
2.一串随机数
生成10个0到1的随机浮点数，保留小数点后两个
'''
from random import random
a = [round(random(), 2) for _ in range(10)]
print(a)

from random import uniform
a = [round(uniform(0,10), 2) for _ in range(10)]
print(a)

'''
3.if和嵌套for
对一个列表里面的数据筛选，只计算[0,11)中偶数的平方
'''
a = range(11)
c = [x ** 2 for x in a if x % 2 == 0]
print(c)

'''
列表生成式中嵌套for
使用嵌套的列表，一行代码生成99乘法表的所有45个元素
'''
a = [i * j for i in range(1, 10) for j in range(1, i+1)]
print(a)

'''
4.zip和列表
'''
a = range(5)
b = ['a', 'b', 'c', 'd', 'e']
c = [str(k) + str(v) for k,v in zip(a, b)]
print(c)

'''
5.打印键值对
'''
a = {'a':1, 'b':2, 'c':3}
b = [k+ '=' + str(v) for k, v in a.items()]
print(b)

'''
6.文件列表
'''
import os
a = [d for d in os.listdir(r'E:\working\pythonAlgorithm\isTester') if os.path.isfile(d)]
print(a)

'''
7.转为小写
'''
a = ['Hello', 'World', '2020Python']
b = [s.lower() for s in a]
print(b)

'''
如上就会出现 int 对象没有方法 lower 的问题，先转化元素为 str 后再操作：
更友好的做法，使用 isinstance，判断元素是否为 str 类型，如果是，再调用 lower 做转化：
'''
a = ['Hello', 'World',2020,'Python']
b = [s.lower() for s in a if isinstance(s, str)]
print(b)

'''
8.保留唯一值
'''
def filter_non_unique(lst):
    return [item for item in lst if lst.count(item) == 1]
print(filter_non_unique([1, 2, 2, 3, 4, 4, 5]))

'''
9.筛选分组
enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
Python 2.3. 以上版本可用，2.6 添加 start 参数。
'''

def bifurcate(lst, filter):
    return [
        [x for i, x in enumerate(lst) if filter[i] == True],
        [x for i, x in enumerate(lst) if filter[i] == False]
    ]
lst = bifurcate(['beep', 'boop', 'foo', 'bar'], [True, True, False, True])
print(lst)

'''
10.函数分组
'''
def bifurcate_by(lst, fn):
    return [
        [x for x in lst if fn(x)],
        [x for x in lst if not fn(x)]
    ]
lst = bifurcate_by(['Python3', 'up', 'users', 'people'], lambda x: x[0] == 'u')
print(lst)

'''
11.差集
'''
def difference(a, b):
    _a, _b = set(a), set(b)
    return [item for item in _a if item not in _b]
print(difference([1,1,2,3,3], [1, 2, 4]))

'''
12.函数差集
列表 a、b 中元素经过 fn 映射后，返回在 a 不在 b 中的元素。
'''
def difference_by(a, b, fn):
    _b = set(map(fn, b))
    return [item for item in a if fn(item) not in _b]

from math import floor
print(difference_by([2.1, 1.2], [2.3, 3.4],floor))



