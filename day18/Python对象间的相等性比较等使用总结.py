#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:sisul
# time: 2020/7/14 9:27
# file: Python对象间的相等性比较等使用总结.py

'''
Python，对象相等性比较相关关键字包括is、in,比较运算符有==。

is判断两个对象的标识号是否相等
in用于成员检测
==用于判断值或内容是否相等，默认是基于两个对象的标识号比较
也就是说，如果a is b为 True且如果按照默认行为，意味着a == b也为True
'''

'''
is判断标识号是否相等
is比较的是两个对象的标识号是否相等，python中使用id()函数获取对象的标识号
'''
a = [1,2,3]
print(id(a))
b = [1,2,3]
print(id(b))
#创建的两个列表实例位于不同的内存地址，所以它们的标识号不等
print(a is b)

#即便对于两个空列表实例，它们is比较的结果也是False
a, b = [], []
print(a is b)

#对于序列类、字典型、集合型对象，一个对象实例指向另一个对象实例，is比较才返回真值
a, b = {'a':[1,2,3]},{'id':'book id', 'price':'book price'}
a = b
print(a == b, '---')
print(id(a))
print(id(b))

'''
对于值类型而言，不同的编译器可能会做不同的优化。从性能角度考虑，它们会缓存一些值类型的对象实例。
所以，使用is比较时，返回的结果看起来会有些不太符合预期。如：
'''
a = 123
b = 123
print(a is b)
c = 123456
d = 123456
print(c is d)       #pycharm结果是True，但是shell显示False
'''
Python解释器，对位于区间[-5, 256]内的小整数，会进行缓存，
不在该范围内的不会缓存
'''
#Python中的None对象是一个单例类的实例，具有唯一的标识符
print(id(None))

#在判断某个对象是否为None时，最便捷的做法:variable is None
a = None
print(a is None)
print(id(a))

'''
in 用于成员检测
如果元素i是s的成员，则i in s为True:
若不是s的成员，则返回False，也就是i not in s为True
'''
#对于字符串类型， i in s为True，意味着i是s的子串，也就是s.find(i)返回大于-1的值
print('ab' in 'abc')
print('abc'.find('ab'))
print('ab' in 'acb')
print('acb'.find('ab'))

#内置的序列类型、字典类型和集合类型，都支持in操作。对于字典类型，in操作判断i是否是字典的键
print([1, 2] in [[1,2], 'str'])

print('apple' in {'orange':1.5,'banana':2.3,'apple':5.2})

'''
对于自定义类型，判断是否位于序列类型中，需要重写序列类型的魔法函数__contains__。
具体操作步骤如下：
    自定义Student类，无特殊之处
    Students类继承list，并重写__contains__方法
'''
class Student:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val

class Students(list):
    def __contains__(self, item):
        for s in self:
            if s.name == item.name:
                return True
            return False

s1 = Student('xiaoming')
s2 = Student('xiaohong')
a = Students()
a.extend([s1, s2])
s3 = Student('xiaoming')
print(s3 in a)
s4 = Student('xiaoli')
print(s4 in a)

'''
==判断值是否相等
对于数值型、字符串、列表、字典、集合，默认只要元素值相等，==比较结果就是True
'''
str1 = "alg-channel"
str2 = "alg-channel"
print(str1 == str2)

'''
对于自定义类型，当所有属性取值完全相同的两个实例，判断==时，返回False。
但是，大部分场景下，我们希望这两个对象相等的，这样不用重复添加到列表中。
例如，判断用户是否已经登入时，只要用户所有属性与登入列表中某个用户完全一致时，就认为已经登入。
如下所示，需要重写方法__eq__，使用__dict__获取实例的所有属性
'''
print('*'*100)
class Student:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, val):
        self._age = val

    def __eq__(self, val):
        print(self.__dict__)
        return self.__dict__ == val.__dict__

a = []
xiaoming = Student('xiaoming', 29)
if xiaoming not in a:
    a.append(xiaoming)

xiaohong = Student('xiaohong', 30)
if xiaohong not in a:
    a.append(xiaohong)

xiaoming2 = Student('xiaoming', 29)
if xiaoming2 == xiaoming:
    print('对象完全一致，相等')

if xiaoming2 not in a:
    a.append(xiaoming2)
print(len(a))