#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:sisul
# time: 2020/7/2 17:45
# file: book.py

class Book:
    def __init__(self, name, sale):
        self.__name = name
        self.__sale = sale

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_name):
        self.__name = new_name

a_book = Book('magic_book', 1000000)
a_book.name = 'red book'
print(a_book.name)
