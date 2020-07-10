#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:sisul
# time: 2020/7/8 15:39
# file: python字符串和正则.py

#反转字符串
s = 'python'
rs = ''.join(reversed(s))
print(rs)

print(s[::-1])

#字符串切片操作
java, python = 'java', 'python'
jl, pl = len(java), len(python)


#join串联字符串      用下划线_连接字符串mystr
mystr = ['I', 'love', 'Python']
res = '_'.join(mystr)
print(res)

#分割字符串          使用split
#join与split可看做一对互逆操作
res_list = 'I_love_python'.split('_')
print(res_list)

#替换     字符串替换，使用replace
s = 'i love python'.replace('o', 'O')
print(s)

#子串判断       判断a串是否为b串的子串
#方法1，使用in:
a = 'our'
b = 'flourish'
r = True if a in b else False
print(r)

#方法2，使用方法find，返回字符串b中匹配子串a的最小索引
a = 'our'
b = 'flourish'
print(b.find(a))

'''
去空格
清洗字符串时，位于字符串开始和结尾的空格，有时需要去掉，strip方法能实现
如下字符串，使用strip，清理字符串开头和结尾的空格和制表符
'''
a = '   \tI love python     \b\n'
print(a)
print(a.strip())

#字符串的字节长度   encode方法对字符串编码后
def str_byte_len(mystr):
    mystr_bytes = mystr.encode('utf-8')
    return len(mystr_bytes)

print(str_byte_len('i love python'))


#正则表达式  导入所需模块re
'''
. 匹配除 "\n" 和 "\r" 之外的任何单个字符。
^ 匹配字符串开始位置
$ 匹配字符串中结束的位置
* 前面的原子重复 0 次、1 次、多次
? 前面的原子重复 0 次或者 1 次
+ 前面的原子重复 1 次或多次
{n} 前面的原子出现了 n 次
{n,} 前面的原子至少出现 n 次
{n,m} 前面的原子出现次数介于 n-m 之间
( ) 分组，输出需要的部分
'''
#常用的通用字符
'''
\s 匹配空白字符
\w 匹配任意字母/数字/下划线
\W 和小写 w 相反，匹配任意字母/数字/下划线以外的字符
\d 匹配十进制数字
\d 匹配十进制数字
[0-9] 匹配一个 0~9 之间的数字
[a-z] 匹配小写英文字母
[A-Z] 匹配大写英文字母
'''

import re
#search第一个匹配串
s = 'i love python very much'
pat = 'python'
r = re.search(pat, s)
print(r.span())


'''
match与search不同
1、match在原字符串的开始位置匹配
2、search在字符串的任意位置匹配
'''
s = 'flourish'
#寻找模式串our，使用match方法
recom = re.compile('our')
print(recom.match(s))           #返回None，找不到匹配

#使用search方法
res = recom.search(s)
print(res.span())               #匹配成功，our在原字符串的其实索引为2

'''
finditer匹配迭代器
使用正则模式，finditer方法，返回所有子串匹配位置的迭代器
通过返回的对象re.Match，使用它的方法span找出匹配位置
'''
s = '山东省潍坊市青州第1中学高三1班'
pat = '1'
r = re.finditer(pat, s)
for i in r:
    print(i)

'''
findall所有匹配
正则模块，findall方法能找出子串的所有匹配
'''
s = '一共20行代码运行时间13.59s'
#目标查找出所有数字：通用字符\d匹配一位数字[0-9]，+表示匹配数字前面的一个字符1次或多次
pat = r'\d+'
r = re.findall(pat, s)
print(r)

'''
匹配浮点数和整数
?表示前一个字符匹配0或1次
.?表示匹配小数点（.）0次或1次
匹配浮点数和整数，r'\d+\.?\d+'
'''
s = '一共20行代码运行时间13.59s'
pat = r'\d+\.?\d+'
r = re.findall(pat, s)
print(r)

#上述数匹配模式无法匹配1位数
s = '一共2行代码运行时间1.66s'
pat = r'\d+\.?\d+'
r = re.findall(pat, s)
print(r)

#r'\d+\.?\d*'
pat = r'\d+\.?\d*'
r = re.findall(pat, s)
print(r)

'''
案例：匹配正整数
^[1-9]\d*$
'''
s = [-16, 1.5, 11.43, 10, 5, 1, 0]
pat = r'^[1-9]\d*$'
res = [i for i in s if re.match(pat,str(i))]
print(res)

'''
re.I忽略大小写
如下，找出字符串中所有字符t或T的位置，不区分大小写
'''
s = 'That'
pat = r't'
r = re.finditer(pat, s, re.I)
for i in r:
    print(i.span())\

'''
split分割字符串
正则模块中split函数强大，能够处理复杂的字符串任务。
如果一个规则简单的字符串，直接使用字符串split函数
'''
s = 'id\tname\taddress'
res = s.split('\t')
print(res)
#分隔符复杂的字符串，可能的分隔符有,;\t |
s = 'This,,,   module ; \t   provides|| regular ; '
words = re.split('[,\s;|]+', s)
print(words)

'''
sub替换匹配串
'''
content="hello 12345, hello 456321"
pat = re.compile(r'\d+')        #要替换的部分
m = pat.sub('666', content)
print(m)

'''
compile预编译
如果要用同一匹配模式，做很多次匹配，可以使用compile预先编译串
example：从一系列字符串中，挑选出所有正浮点数
正则表达式为：^[1-9]\d+\.\d*|0.\d*$
'''
s = [-16,'good',1.5, 0.2, 0.002,-0.1, '11.43', 10, '5e10']
rec = re.compile(r'^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$')
res = [ i for i in s if rec.match(str(i))]
print(res)