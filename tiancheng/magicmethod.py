#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:sisul
# time: 2020/8/17 10:33
# file: magicmethod.py

'''
__init__，负责初始化
'''
class Person:
    def __init__(self, name, age):
        print('in __init__')
        self.name = name
        self.age = age

p = Person('Tiancheng', 20)
print("p: ", p)
print('*'*50)

'''
__new__，构造方法：__new__(cls, [...])new 是python中对象实例化时所调用的第一个函数，
在init之前被调用。new将class作为他的第一个参数，并返回一个这个class的instance。而init是将instance
作为参数，并将这个instance进行初始化操作。每个实例创建都会调用new函数
'''

class Person2:
    def __new__(cls, *args, **kwargs):
        print('in __new__')
        instance = super().__new__(cls)
        return instance

    def __init__(self, name, age):
        print('in __init__')
        self.name = name
        self.age = age

p2 = Person2('sisul', 31)
print('p2: ', p2)

print('*'*50)

'''
使用new方法实现单例
'''
class SingleTon(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

s1 = SingleTon()
s2 = SingleTon()
print(s1)
print(s2)

'''
__call__方法，先需要明白什么是可调用对象，平时自定义的函数、内置函数和类都属于
可调用对象，但凡是可以把一对括号()应用到某个对象身上都可称之为可调用对象，判断对象
是否为可调用对象可以用函数callable。
'''

class A:
    def __init__(self):
        print('__init__')
        super(A, self).__init__()

    def __new__(cls):
        print('__new__')
        return super().__new__(cls)

    def __call__(self):         #可以定义任意参数
        print('__call__')

a = A()
print('-'*10)
a()     #执行a(）才会打印出__call__。a是一个实例化对象，也是一个可调用对象
print(callable(a))

print('*'*50)

'''
__del__
析构函数，当删除一个对象时，则会执行此方法，对象在内存中销毁时，会自动调用此方法。
'''

class Person3:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):  #在对象被删除的条件下，自动执行
        print('执行__del__')

obj = Person3('lizh', 23)
del obj

print('*'*50)

'''
闭包和自省
什么是闭包，如果在一个内部函数里，对在外部作用域（但不是在全局作用域）的变量
进行引用，那么内部函数就被认为是闭包（closure）
'''

def addx(x):
    def adder(y):
        return x + y
    return adder

c = addx(8)
print(type(c))
print(c.__name__)
print(c(10))

print('-'*50)


'''
实现一个闭包并可以修改外部变量
'''
def foo():
    a = 1
    def bar():
        nonlocal a
        a = a + 1
        return a
    return bar
c = foo()
print(c())

print('-'*50)

'''
自省（反射）
检查某些事物以确定它是什么、它知道什么以及它能做什么

hasattr(object, name)   检查对象是否具有name属性。返回bool
getattr(object, name, default)  获取对象的name属性
setattr(object, name, default)  给对象设置name属性
delattr(object, name)   给对象删除name属性
dir([object])   获取对象大部分属性
isinstance(name, object)    检查name是不是object对象
type(object)    查看对象的类型
callable(object)    判断对象是否是可调用对象
'''

'''
装饰器和迭代器
装饰器本质上是一个python函数或类，它可以让其他函数或类在不需要做任何代码修改的前提下增加额外功能
（设计模式中的装饰器模式），装饰器的返回值也是一个函数/类对象。它经常用于有切面需求的场景，比如：
插入日志、性能测试、事物处理、缓存、权限校验等场景
'''

print('-'*50)

def my_logging(func):

    def wrapper():
        print('{} is running.'.format(func.__name__))
        return func()
    return wrapper

@my_logging
def foo():
    print('this is foo function')

foo()

print('-'*50)
'''
my_logging就是一个装饰器，它是一个普通函数，它把执行真正业务逻辑的函数func包裹在其中，
看起来像foo被my_logging装饰了一样，my_logging返回的也是一个函数，这个函数的名字叫wrapper。

如果foo带有参数，如何将参数带到wrapper中了？
'''

def my_logging(func):

    def wrapper(*args, **kwargs):
        print('{} is running.'.format(func.__name__))
        return func(*args, **kwargs)
    return wrapper

@my_logging
def foo(x, y):
    print('this is foo function')
    return x + y
print(foo(1,111))

print('-'*50)
'''
带参数的装饰器
装饰器的语法允许在调用时，提供其他参数，比如@decorator(a)。这样就大大增加了灵活性，
比如在日志告警场景中，可以根据不同的告警定告警等级：info/warn等。
'''
def my_logging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == 'info':
                print('{} is running. level: '.format(func.__name__), level)
            elif level == 'warn':
                print('{} is running. level: '.format(func.__name__), level)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@my_logging(level='info')
def foo(name='foo'):
    print('{} is running'.format(name))

@my_logging(level='warn')
def bar(name='bar'):
    print('{} is running'.format(name))

foo()
bar()
'''
上面的my_logging是允许带参数的装饰器。它实际上是对原有装饰器的一个函数封装，并返回一个装饰器。
可以将它理解为一个含有参数的闭包。当使用@my_logging(level='info')调用的时候，python能够发现这
一层的封装，并把参数传递到装饰器的环境中。
'''
print('-'*50)

'''
类装饰器
相比较函数装饰器，类装饰器具有灵活度大、高内聚、封装性等优点。使用类装饰器主要依靠类的__call__方法，当使用
@形式将装饰器附加到函数上时，就会调用此方法。
'''

class MyLogging:
    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        print('class decorator starting')
        a = self._func(*args, **kwargs)
        print('class decorator end.')
        return a

@MyLogging
def foo(x, y):
    print('foo is running')
    return x + y
print(foo(1, 2))

print('-'*50)
'''
functools.wraps
Python中还有一个装饰器的修饰函数functools.wraps。原函数被装饰函数装饰后，发生了一些变化
'''
def my_logging(func):

    def wrapper(*args, **kwargs):
        print('{} is running'.format(func.__name__))
        return func(*args, **kwargs)
    return wrapper

@my_logging
def foo(x, y):
    '''
    add function
    :param x:
    :param y:
    :return:
    '''
    print('this is foo function.')
    return x + y

print(foo(1, 2))
print('function name: ', foo.__name__)      #wrapper
print('doc: ', foo.__doc__)       #None
print('-'*50)

'''
func name应该打印出foo才对，而doc也不为None。由此发现原函数被装饰函数装饰之后，
元信息发生了改变，这明显不是想要的结果，python里可以通过functools.wraps来解决，
保持原函数元信息
'''
from functools import wraps

def my_logging(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('{} is running.'.format(func.__name__))
        return func(*args, **kwargs)
    return wrapper

@my_logging
def foo(x, y):
    '''
    add function
    :param x:
    :param y:
    :return:
    '''
    print('this is foo function.')
    return x + y

print(foo(1, 2))
print('func name: ', foo.__name__)
print('doc: ', foo.__doc__)
print('-'*50)

'''
迭代器VS生成器
container(容器)
container可以理解为把多个元素组织在一起的数据结构，container中的元素可以
逐个的迭代获取，可以用in,not in关键字判断元素是否包含在容器中。在Python中，
常见的container对象
list, deque
set, frozensets
dict, defaultdict, OrderedDict, Counter,
tuple, namedtuple
str
'''

'''
可迭代对象（iterables） VS 迭代器（iterator）
大部分的container都是可迭代对象，比如list or set都是可迭代对象
'''
x = [1,2,3]
y = iter(x)
print(next(y))
print(next(y))
print(type(x))
print(type(y))
print('-'*50)
'''
x是可迭代对象，也叫container。y是迭代器，且实现了__iter__和__next__方法。
iterable->iter()->iterator
通过iter方法就是迭代器。它是一个带状态的对象，调用next方法的时候返回容器的下一个值，
可以说任何实现了iter和next方法的对象都是迭代器，iter返回迭代器自身，next返回容器中的下一个值，
如果容器中没有更多元素了，则抛出异常。
'''

'''
生成器（generator）
生成器一定是迭代器，是一种特殊的迭代器，特殊在于它不需要再像上面的iter()和next方法了，
只需要yield关键字
'''

def fib(n):
    prev, curr = 0, 1
    while n > 0:
        yield curr
        prev, curr = curr, curr + prev
        n -= 1

y = fib(10)
print(next(y))
print(type(y))
print(next(y))
print(next(y))
'''
当执行f=fib()返回的是一个生成器对象，此时函数体中的代码并不会执行，只有显示或
隐式的调用next的时候才会真正执行里面的代码。
假设有千万个对象，需要顺序调取，如果一次加载到内存，对内存是极大的压力，有生成器
之后，可以
'''