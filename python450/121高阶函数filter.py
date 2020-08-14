#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:sisul
# time: 2020/7/17 15:22
# file: 121高阶函数filter.py

def filter_self(function, iterable):
    return iter([item for item in iterable if function(item)])

class Student:
    def __init__(self, name, sex, height):
        self.name = name
        self.sex = sex
        self.height = height

def height_condition(stu:Student):
    if stu.sex == 'male':
        return stu.height > 1.75
    else:
        return stu.height > 1.65

students = [Student('xiaoming','male',1.74),
           Student('xiaohong','female',1.68),
           Student('xiaoli','male',1.80)]
stu_satisfy = filter_self(height_condition, students)
for stu in stu_satisfy:
    print(stu.name)