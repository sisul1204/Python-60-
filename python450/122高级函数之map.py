#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:sisul
# time: 2020/7/17 15:29
# file: 122高级函数之map.py

mylist = [1,3,2,4,1]
result = map(lambda x:x+1, mylist)
print(result, type(result))
print(list(result))

#找到同时满足第一个列表的元素为奇数，第二个列表对应位置的元素为偶数的元素
xy = map(lambda x,y:x%2==1 and y%2==0, [1,3,2,4,1],[3,2,1,2])
for i in xy:
    print(i)
