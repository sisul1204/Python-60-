#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:sisul
# time: 2020/7/8 10:35
# file: 16个类型函数和10个类对象相关的内置函数.py

'''
函数作用域问题。
python查找变量的顺序遵守LEGB规则，即遇到某个变量时：
1、优先从它所属的函数（local）内查找
2、若找不到，并且它位于一个内嵌函数中，就再到它的父函数（enclosing）中查找
3、如果还是找不到，再去全局作用域（global）查找
4、再找不到，最后去内置作用域（build-in）查找
5、若还是找不到，报错
'''

#类型函数
#bool([x])
'''
测试一个对象是True,还是False
'''
print(bool([0,0,0]))
print(bool([]))
print(bool([1,0,1]))

#bytes([source[,encoding[,errors]]])    将一个字符串转换成字节类型
s = 'apple'
print(bytes(s, encoding='utf-8'))

#str(object='')     将字符类型、数值类型等转换为字符串类型
i = 100
print(str(i), type(str(i)))

#chr(i)     查看十进制整数对应的ASCII字符
print(chr(65), type(chr(65)))


#ord(c)     查看某个ASCII字符对应的十进制
print(ord('A'))

'''
class dict(**kwargs)
class dict(mapping, **kwargs)
class dict(iterable, **kwargs)
'''

print(dict(a='a', b='b'))
print(dict(zip(['a', 'b'], [1,2])))
print(dict([('a',1),('b',2),('c',3)]))


'''
frozenset([iterable])
创建一个不可修改的冻结集合，一旦创建不允许增删元素
'''
s = frozenset([1,1,3,2,3])
print(s)

'''
list([iterable])
返回可变序列类型：列表。如下，集合类型转列表
'''
s = {1,2,3,4}
print(list(s), type(list(s)))

'''
list函数还常用在，可迭代类型（iterable）转化为列表。
如下，使用map函数，转化列表内每一个整形元素为字符串型
m是可迭代类型，经过list转化后，看到列表l
'''
m = map(lambda i:str(i), [186,1243,3201])
l = list(m)
print(l, type(l))

'''
set([iterable])，返回一个集合对象，并允许创建后再增加、删除元素
'''
a = [1,4,2,3,1]
print(set(a))


'''
slice(stop); slice(start, stop, step)   返回一个由range(start, stop, step)所指定索引集的slice对象
'''
a = [1,4,2,3,1]
print(a[slice(0,5,2)])      #等价于a[0:5:2]

#tuple([iterable])      创建一个不可修改的元组对象：
print(tuple(range(10)))

'''
zip(*iterables)
创建一个迭代器，聚合每个可迭代对象的元素
参数前带*，意味着是可变序列参数，可传入1个，2个或多个参数
'''
#传入1个参数
for i in zip([1,2]):
    print(i, type(i))

#传入2个参数
a = range(5)
b = list('abcde')
lst = [str(y) + str(x) for x, y in zip(a, b)]
print(lst)

'''
类对象及属性
classmethod
'''
class Student:
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name

    def instance_method(self):
        print('这是实例方法')
        return self

    @classmethod
    def __annotations__(cls):
        return '学生类'

    @classmethod
    def print_type_name(cls):
        print('这是类上的方法，类名为{}，注解为{}'.format(cls.__name__, cls.__annotations__()))

Student().print_type_name()
Student().instance_method()

#使用Python装饰器@property，能实现对类上属性的定义
class Student:
    def __init__(self):
        self._name = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val

    @name.deleter
    def name(self):
        del self._name

xiaoming = Student()
xiaoming.name = 'xiaoming'
print(xiaoming.name)


#super([type[,object-or-type]])
'''
返回一个代理对象，它会将方法调用委托给type的父类或兄弟类
'''
class Parent:
    def __init__(self, x):
        self.v = x

    def add(self, x):
        return self.v + x

class Son(Parent):
    def add(self, y):
        r = super().add(y)
        print(r)
Son(1).add(2)

#callable(object)
'''
判断对象是否可被调用，能被调用的对象就是一个callable对象，比如函数str、int等都是可被调用的
'''
print(callable(str))

class Student:
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name
xm = Student()
print(callable(xm))

#如果xm能被调用：xm()，必须要重写Student类上__call__方法：

class Student:
    def __init__(self,id,name):
        self.id = id
        self.name = name

    def __call__(self, *args, **kwargs):
        print('I can be called')
        print(f'my name is {self.name}')
t = Student('001','xiaoming')
t()






