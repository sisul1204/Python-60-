#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:sisul
# time: 2020/7/16 10:44
# file: Python应用迭代器和生成器的9个案例.py

a = [1,3,5,7]
a_iter = iter(a)

from collections.abc import Iterator
print(isinstance(a_iter, Iterator))

#第一遍
for i in a:
    print(i)

for i in a_iter:
    print(i)

#第二遍
for i in a:
    print(i)

for i in a_iter:
    print(i)

'''
列表a和迭代器a_iter的区别
    1.列表不论遍历多少次，表头位置始终是第一个元素；
    2.迭代器遍历结束，不再指向原来的表头位置，而是为最后元素的下一个位置
只有迭代器对象才能与内置函数next结合使用，next一次，迭代器就前进一次，指向一个新的元素
所以，要想迭代器a_iter重新指向a的表头，需要重新创建一个新的迭代a_iter_copy：

a_iter_copy = iter(a)

调用next，输出迭代器指向a的第一个元素
next(a_iter_copy)

ps：无法通过len获取迭代器的长度，只能迭代到最后一个末尾元素时，才知道其长度
'''

#获取迭代器指向a的长度
a = [1,3,5,7]
a_iter_copy2 = iter(a)
iter_len = 0
try:
    while True:
        temp = next(a_iter_copy2)
        print(temp)
        iter_len += 1
except StopIteration:
    print("iterator stops")
print('a的长度是:{}'.format(iter_len))

'''
带yield的函数是生成器，而生成器也是一种迭代器。
'''
#节省内存案例
def accumulate_div(a):
    if a is None or len(a) == 0:
        return []
    it = iter(a)
    total = next(it)
    yield total
    for i in it:
        total = total * i
        yield total

acc = accumulate_div([1,2,3,4,5,6])
for i in acc:
    print(i)

'''
拼接迭代器
chain函数实现元素拼接，原型如下，参数*表示可变的参数：
chain(*iterable)
'''
from itertools import chain, accumulate

chain_iterator = chain(['I', 'love'], ['python'], ['very', 'much'])
print(chain_iterator, type(chain_iterator))
for i in chain_iterator:
    print(i)

'''
join只是一次串联一个序列对象。而chain能串联多个可迭代对象，形成一个更大的可迭代对象
'''
from collections.abc import Iterator
print(isinstance(chain_iterator, Iterator))

'''
累积迭代器
返回可迭代对象的累积迭代器，函数原型
accumulate(iterable[,func,*,initial=None])
应用如下，返回的是迭代器，通过结合for打印出来
如果func不提供，默认求累积和
'''
accu_iterator = accumulate([1,2,3,4,5,6])
for i in accu_iterator:
    print(i)

#如果func提供，func的参数个数要求为2，根据func的累积行为返回结果
accu_iterator = accumulate([1,2,3,4,5,6], lambda x, y:x*y)
for i in accu_iterator:
    print(i)