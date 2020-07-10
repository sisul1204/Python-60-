#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:sisul
# time: 2020/7/7 13:56
# file: dict和set基本操作.py

'''
五种创建方法
'''
#1.手动创建
empty = {}
dict_1 = {'a':1, 'b':2}

#2.使用dict()函数构造
dict_2 = dict(a=1, b=2, c=3)
print(dict_2)

#3.键值对+关键字参数
dict_3 = dict({'a':1, 'b':2},c=3, d=4)
print(dict_3)

#4.可迭代对象    列表，元素又为一个元组，后面再加一系列关键字参数
dict_4 = dict([('a',1),('b',2)],c=3)
print(dict_4)

#5.fromkeys()方法     已知键集合（keys），values为初始值：
dict_5 = {}.fromkeys(['k1', 'k2', 'k3'], [1,2,3])
print(dict_5)

dict_6 = {'a':1,'b':2}.fromkeys(['c','d'],[1,2])
print(dict_6)



'''
基本操作：
    创建字典
    遍历字典
    获取所有键集合（keys）
    获取所有值集合（values）
    获取某键对应的值
    添加、修改或删除一个键值对
'''
#创建字典
d = {'a':1, 'b':2, 'c':3}
#遍历容器每一项
for k,v in d.items():
    print(k, v)
#获取所有键集合
print('获取所有键集合',set(d))
print('获取所有键集合',set(d.keys()))

#获取所有值集合
print('获取所有值集合', set(d.values()))

#判断键是否在字典中
if 'c' in d:
    print('键c在字典中')

if 'e' not in d:
    print('键e不在字典中')

#获取某键对应的值
print(d.get('c'))

#添加或修改一个键值对
#method1
d['d'] = 4
print(d)
#method2
d.pop('c')
print(d)

#删除一个键值对
del d['d']
print(d)

print(list(d.items()))


#集合     判断一个列表中是否含有重复元素，可以借助set
def duplicated(lst):
    return len(lst) != len(set(lst))

#求并集
a = {1,3,5,7}
b, c = {3,4,5,6}, {6,7,8,9}
d = a.union(b, c)
print(d)

#求差集
d = a.difference(b, c)
print(d)

#求交集
d = a.intersection(b, c)
print(d)
