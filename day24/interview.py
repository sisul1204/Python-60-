#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:sisul
# time: 2020/8/14 13:38
# file: interview.py

#1、一行代码生成[1,3,5,7,9,11,13,15,17,19]
a = [2*i+1 for i in range(10)]
print(a)

#2、写一个等差数列，产生一个首相为10， 公差为12， 末项不大于100的列表
a = list(range(10,100,12))
print(a)

#3、一行代码求1到10000内整数和
s = sum(range(10000))
print(s)

from functools import reduce
s = reduce(lambda x, y:x+y, range(10000))
print(s)

#4、打乱一个列表
#使用random模块，shuffle函数打乱原来列表，值得注意的是in-place打乱
import random
b = list(range(10))
random.shuffle(b)
print(b)

#5、字典按value排序并返回新字典
d = {'a':12, 'b':50, 'c': 1, 'd': 20}
d_new = dict(sorted(d.items(), key=lambda item: item[1]))
print(d_new)

#6、如何删除list里重复元素，并保证元素顺序不变
a = [3,2,2,2,1,3]
a_new = []
for ele in a:
    if ele not in a_new:
        a_new.append(ele)
print(a_new)


#7、怎么找出两个列表的相同元素和不同元素
def ana(a, b):
    aset, bset = set(a), set(b)
    same = aset.intersection(bset)
    differ = aset.difference(bset).union(bset.difference(aset))
    return same, differ

a = [3,2,2,2,1,3]
b = [1,4,3,4,5]
print(ana(a, b))

#8、字符串处理字典
string1 = 'k0:10|k1:2|k2:11|k3:5'
lst1 = string1.split('|')
print(type(lst1))
dct = {}
for s in lst1:
    a, b = s.split(':')
    dct.update({a:int(b)})
print(dct)

m = map(lambda x: x.split(':'), string1.split('|'))
d = {mi[0]:int(mi[1]) for mi in m}
print(d)


#10、遍历目录与子目录，抓取.py文件
'''
os.walk()，返回的是一个三元组(root, dirs, files)
root所指的是当前正在遍历的这个文件夹的本身的地址
dirs是一个list，内容是该文件中所有的目录的名字（不包含子目录）
files同样是一个list，内容是该文件夹所有的文件（不包括目录）
'''
import os
def get_files(directory, ext):
    res = []
    for root, dirs, files in os.walk(directory):
        for filename in files:
            name, suf = os.path.splitext(filename)
            if suf == ext:
                res.append(os.path.join(root, filename))
    return res

print(get_files(r'E:\pythontest\APITesting2', '.py'))