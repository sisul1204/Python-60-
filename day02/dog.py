#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:sisul
# time: 2020/7/2 11:49
# file: dog.py


class Dog:
    def __init__(self, name, dtype):
        self.__name = name
        self.__dtype = dtype

    def shout(self):
        print('I\'m %s, type: %s' % (self.name, self.dtype))

    def get_name(self):
        return self.__name

wangwang = Dog('wangwang','cute_type')
print(wangwang.get_name())