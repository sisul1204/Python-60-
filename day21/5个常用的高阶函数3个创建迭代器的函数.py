#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:sisul
# time: 2020/7/14 17:44
# file: 5个常用的高阶函数3个创建迭代器的函数.py

#filter(function, iterable)
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
        # if stu.height > 1.75:
        #     return stu
    else:

        return stu.height > 1.65

students = [Student('xiaoming','male',1.74),
            Student('xiaohong','female',1.68),
            Student('xiaoli', 'male',1.80)
            ]
students_satisfy = filter_self(height_condition, students)
for stu in students_satisfy:
    print(stu.name)

'''
map(function, iterable,...)
它将function映射于iterable中的每一项，并返回一个新的迭代器
'''
mylst = [1,3,2,4,1]
result = map(lambda x:x+1, mylst)
print(result, type(result))
print(list(result))

'''
同时，map函数支持传入多个可迭代对象。当传入多个可迭代对象时，输出元素个数等于较短序列长度。
如下，传入两个列表，function就需要接受两个参数，取值分别对应第一、第二个列表中的元素，
找到同时满足第一个列表的元素为奇数，第二个列表对应位置的元素为偶数的元素
'''
xy = map(lambda x,y:x%2==1 and y%2==0, [1,3,2,4,1], [3,2,1,2])
for i in xy:
    print(i)

'''
借助map函数，实现向量级运算
'''
lst1 = [1,2,3,4,5,6]
lst2 = [3,4,5,6,3,2]

def vector_add(x, y):
    return list(map(lambda i,j:i+j, x, y))
print(vector_add(lst1,lst2))

'''
reduce(function, iterable[, initializer])
提到map，就会想起reduce，前者生成映射关系，后者实现归约。
reduce函数位于functools模块中，使用前需要先导入。
from functools import reduce

reduce函数中第一个参数是函数function。function函数，参数个数必须为2，是可迭代对象iterable内的连续两项。
计算过程，从左侧到右侧，依次归约，直到最终为单个值并返回
'''
from functools import reduce
res = reduce(lambda x, y:x+y,range(10))
print(res)

'''
reversed(seq)
重新生成一个反向迭代器，对输入的序列实现反转
'''
rev = reversed([1,4,2,3,1])
print(rev, type(rev))
# print(list(rev))
for i in rev:
    print(i)

'''
sorted(iterable,*,key=None,reverse=False)
实现对序列化对象的排序
key参数和reverse参数必须为关键字参数，都可省略
'''
a = [1,4,2,3,1]
res = sorted(a, reverse=True)
print(res)

'''
如果可迭代对象的元素也是一个符合对象，如下为字典。
依据为字典键的值，sorted的key函数就会被用到。
'''
a = [{'name':'xiaoming','age':20,'gender':'male'},
     {'name':'xiaohong','age':18,'gender':'female'},
     {'name':'xiaoli','age':19,'gender':'male'}
]
b = sorted(a, key=lambda x:x['age'], reverse=False)
print(b)

'''
迭代器
iter(object[,sentinel])
返回一个严格意义上的可迭代对象，其中，参数sentinel可有可无
'''

'''
只要iterable对象支持可迭代协议，即自定义了__iter__函数，便都能配合for依次迭代输出其元素
'''
class TestIter:
    def __init__(self):
        self._lst = [1,3,2,3,4,5]

    #支持迭代协议（即定义__iter__()函数）
    def __iter__(self):
        print('__iter__ is called')
        return iter(self._lst)

#因此，对象t便能结合for，迭代输出元素
t = TestIter()
for e in t:
    print(e)

'''
next(iterator,[,default])
当迭代到最后一个元素时，再执行next，就会抛出StopIteration,迭代器终止运行
'''

'''
example：定制一个递减迭代器
编写一个迭代器，通过循环语句，对某个正整数，一次递减1，直到0
实现类Decrease,继承于Iterator对象，重写两个方法
__iter__
__next__
'''
from collections.abc import Iterator
class Decrease(Iterator):
    def __init__(self, init):
        self.init = init

    def __iter__(self):
        return self

    def __next__(self):
        while 0 < self.init:
            self.init -= 1
            return self.init
        raise StopIteration

#调用递减迭代器Decrease
decrease = Decrease(6)
for d in decrease:
    print(d)

'''
enumerate(iterable, start=0)
enumerate是很有用的内置函数，尤其要用到列表索引时。它返回可枚举对象，也是一个迭代器
'''
s = ['a', 'b', 'c']
for i, v in enumerate(s):
    print(i, v)

#也可以手动执行next，依次输出一个tuple
enum = enumerate(s)
print(next(enum))