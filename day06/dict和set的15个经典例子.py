#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:sisul
# time: 2020/7/7 14:57
# file: dict和set的15个经典例子.py


#1.update   已有字典中批量插入键值对：
d = {'a':1, 'b':2}
#方法一:
d.update({'c':3,'d':4,'e':5})
print(d)

#方法二:
d = {'a':1, 'b':2}
d.update([('c',3),('d',4),('e',5)])
print(d)

#方法三
d = {'a':1, 'b':2}
d.update([('c',3),('d',4)],e=5)
print(d)

#2、setdefault   如果仅当字典中不存在某个键值对时，才插入到字典中；如果存在，不必插入（也就不会修改键值对）
d = {'a':1, 'b':2}
r = d.setdefault('c',3)
print(r)
print(d)

r = d.setdefault('c', 33)   # r:3，已经存在'c':3的键值对，所以setdefault时d无改变
print(r)
print(d)


#3.字典并集
def f(d:dict) -> dict:
    return {**d}

print(f({'a':1, 'b':3}))
'''
{**d1, **d2}实现合并d1和d2，返回一个新字典
'''
def merge(d1:dict, d2:dict) -> dict:
    return {**d1, **d2}

print(merge({'a':1,'b':2},{'c':3}))

#4.字典差
def difference(d1:dict,d2:dict) -> dict:
    return dict([(k, v) for k, v in d1.items() if k not in d2])             #创建字典的第二种方法

print(difference({'a':1,'b':2,'c':3},{'b':2}))

#5.按键排序
def sort_by_key(d:dict):
    return sorted(d.items(), key=lambda x:x[0])
print(sort_by_key({'a':3,'b':1,'c':2}))

#6.按值排序
def sort_by_value(d:dict):
    return sorted(d.items(), key=lambda x:x[1])
print(sort_by_value({'a':3,'b':1,'c':2}))

#7.最大键      通过keys拿到所有键，获取最大键，返回（最大键，值）的元组
def max_key(d:dict):
    if len(d) == 0:
        return []
    max_key = max(d.keys())
    return (max_key,d[max_key])
print(max_key({'a':3,'c':3,'b':2}))

#8.最大字典值
def max_key(d:dict):
    if len(d) == 0:
        return []
    max_val = max(d.values())
    return [(key, value) for key, value in d.items() if value == max_val]
print(max_key({'a':3,'c':3,'b':2}))

#9.集合最值     找出集合中的最大值、最小值，并装到元组中返回：
def max_min(s:set):
    return (max(s), min(s))
print(max_min({1,3,5,7}))

#10.单字符串    若组成字符串的所有字符仅出现一次，则被称为单字符串
def single(s:str) -> bool:
    return len(s) == len(set(s))
print(single('love_python'))
print(single('python'))

#11.更长集合
def longer(s1, s2):
    return max(s1,s2, key=lambda x:len(x))
print(longer({1,3,5,7},{1,5,7}))


#12.重复最多
'''
在两个列表中，找出重叠次数最多的元素。默认只返回一个。

解决思路：

求两个列表的交集
遍历交集列表中的每一个元素，min(元素在列表 1 次数, 元素在列表 2 次数) ，就是此元素的重叠次数
求出最大的重叠次数
'''
def max_overlap(lst1:list, lst2:list):
    overlap = set(lst1).intersection(lst2)
    ox = [(x, min(lst1.count(x), lst2.count(x))) for x in overlap]
    return max(ox, key=lambda x:x[1])

print(max_overlap([1,2,2,2,3,3],[2,2,3,2,2,3]))

#13.topn键
'''
找出字典前n个最大值，对应的键。导入python内置模块heapq中的nlargest函数，获取字典中的前n个最大值。key函数定义按值比较大小
'''
from heapq import nlargest
def topn_dict(d, n):
    return nlargest(n, d, key=lambda k:d[k])
print(topn_dict({'a': 10, 'b': 11, 'c': 9, 'd': 10}, 3))

#14.一键对多值字典
d = {}
lst = [(1,'apple'),(2,'orange'),(1,'compute')]
for k, v in lst:
    if k not in d:
        d[k] = []
    d[k].append(v)

print(d)

from collections import defaultdict
lst = [(1,'apple'),(2,'orange'),(1,'compute')]
d = defaultdict(list)
print('---------')
print(d)
for k, v in lst:
    d[k].append(v)
    print(k, v)
print(d)

#15.逻辑上合并字典
dic1 = {'x': 1, 'y': 2 }
dic2 = {'y': 3, 'z': 4 }
merged = {**dic1, **dic2}
print(merged)
merged['x'] = 10
print(merged, dic1)


from collections import ChainMap
dic1 = {'x': 1, 'y': 2 }
dic2 = {'y': 3, 'z': 4 }
merged = ChainMap(dic1,dic2)
print(merged)
merged['x'] = 10
print(dic1)
