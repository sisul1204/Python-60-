#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:sisul
# time: 2020/7/17 9:14
# file: 113LEGB.py

'''
Python查找变量遵循LEGB规则
优先从它所属的函数（local）内查找；
若找不到，并且它位于一个内嵌函数中，就再到它的父函数（enclosing）中查找；
如果还找不到，再去全局作用域（global）查找；
再找不到，最后去内置作用域（build-in）查找。
若还是找不到，报错。
'''

'''
变量c在局部作用域（local）被发现；变量b在parent函数和son函数间（enclosing）被发现；
变量a在全局作用域(global)被发现；min函数属于python中内置函数，所以在搜寻完LEG三个区域后，最终在build-in域被找到
'''

a = 10
def parent():
    b = 20
    def son():
        c = 30
        print(b + c)
        print(a + b + c)
        print(min(a, b, c))
    son()

parent()

'''
如下变量d，在LEGB四个域都被搜寻一遍后，还是未找到，就会抛出d没有发现的异常
'''
a = 10
def parent():
    b = 20
    def son():
        c = 30          #local
        print(b + c)    #b:enclosing
        print(a + b + c)    #a:global
        print(min(a, b, c)) #min：build-in
        print(d)            #在LEGB四个域都未找到后，报错
    son()
parent()