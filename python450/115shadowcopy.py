#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:sisul
# time: 2020/7/17 13:40
# file: 115shadowcopy.py
c = ['三文鱼','电烤箱']
lst2 = ['001','2019-11-11',c]
sku_deep = lst2.copy()
sku_deep[2][0] = '龙虾'
print(sku_deep)
print(lst2)

from copy import deepcopy
a = [1,2,[3,4,5]]
ac = deepcopy(a)
ac[0] = 10
ac[2][1] = 40
print(a[0] == ac[0])
print(a[2][1] == ac[2][1])
print('*'*100)
b = [3,4,5]
c = [1,2,b]
b[0] = 0
print(c)


print('*' * 10)
def lab_three():
    dct = {'a': [1,2,3,4,5], 'b':2}
    x = dct['a']
    for i in range(5):
        x[i] = 0
    print(x)
    print(dct)
lab_three()