#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:sisul
# time: 2020/7/9 15:11
# file: python文件操作.py

'''
python文件IO操作：
    文件读写操作
    获取文件后缀名
    批量修改后缀名
    获取文件修改时间
    压缩文件
    加密文件等常用操作
'''
'''
文件读操作
先判断文件是否存在，若存在，再读取；若不在，抛出文件不存在异常
'''
import os
def read_file(filename):
    if os.path.exists(filename) is False:
        raise FileNotFoundError('{} not exist'.format(filename))
    f = open(filename, encoding='utf-8')
    content = f.read()
    f.close()
    return content

content = read_file(r'E:\电子书\使用kubeadm快速部署一个K8s集群.md')
print(content)

'''使用with语句代替open和close'''
def read_file2(filename):
    if os.path.exists(filename) is False:
        raise FileNotFoundError('{} not exists'.format(filename))
    with open(filename, encoding='utf-8') as f:
        content = f.read()
    return content
content = read_file2(r'E:\电子书\使用kubeadm快速部署一个K8s集群.md')
print(content)

'''
文件按行读
read函数一次读取整个文件，readlines函数按行一次读取整个文件。读入文件小时，使用它们没有问题。
但是，如果读入文件大，read或readlines一次读取整个文件，内存就会面临重大挑战。
使用readline一次读取文件一行，能解决大文件读取内存溢出问题
'''

'''
读取文件a.txt，r+表示读写模式。
每次读入一行
选择正则split分词，单词间有的一个空格，有的多个。
使用defaultdict统计单词出现频次
按照频次从大到小降序
'''

from collections import defaultdict
import re

rec = re.compile('\s+')
dd = defaultdict(int)
with open('a.txt') as f:
    for line in f:
        clean_line = line.strip()
        if clean_line:
            words = rec.split(clean_line)
            for word in words:
                dd[word] += 1

dd = sorted(dd.items(), key=lambda x:x[1], reverse=True)
print('---print stat---')
print(dd)
print('---words stat done---')


'''
文件写操作
文件写操作时，需要先判断要写入的文件路径是否存在
若不存在，通过mkdir创建出路径；否则直接写入文件
'''
def write_to_file(file_path, file_name):
    if os.path.exists(file_path) is False:
        os.mkdir(file_path)

    whole_path_filename = os.path.join(file_path, file_name)
    to_write_file = 'Hey, Python' \
                    'I just love Python so much,' \
                    'and want to get the whole python stack by this 60-days column' \
                    'and believe!'

    with open(whole_path_filename, mode='w',encoding='utf-8') as f:
        f.write(to_write_file)
    print('----------write done-----------')
    print('----------begin read-----------')
    with open(whole_path_filename, encoding='utf-8') as f:
        content = f.read()
        print(content)
        if to_write_file == content:
            print('content is equal by reading and writing')
        else:
            print('----Warning: NO Equal-----------------')

write_to_file(r'E:\working\pythonAlgorithm\gitbook\day10','b.txt')

'''
获取文件名
有时拿到一个文件名时，名字带有路径。这时，使用os.path、split方法实现路径和文件的分离
'''
file_text = os.path.split('./data/py/test.py')
ipath, ifile = file_text
print(ipath, ifile)

'''
获取后缀名
os.path模块，splitext能够优雅地提取文件后缀
'''
file_extension = os.path.splitext('./data/py/test.py')
print(file_extension[0], file_extension[1])


print('*' * 100)

'''获取后缀名的文件'''
def find_file(work_dir, extension='jpg'):
    lst = []
    for filename in os.listdir(work_dir):
        print(filename)
        splits = os.path.splitext(filename)
        ext = splits[1]     #获取扩展名
        if ext == '.' + extension:
            lst.append(filename)
    return lst

r = find_file('.', 'md')
print(r)


'''
批量修改后缀
本例使用python os模块和argparse模块。
将工作目录下所有后缀名为old_ext的文件，修改为new_ext。
'''
import argparse

def get_parser():
    parser = argparse.ArgumentParser(description='工作目录中文件后缀名修改')
    parser.add_argument('work_dir', metavar='WORK_DIR', type=str, nargs=1, help='修改后缀名的文件目录')
    parser.add_argument('old_ext', metavar='OLD_EXT', type=str, nargs=1, help='原来的后缀')
    parser.add_argument('new_ext', metavar='NEW_EXT', type=str, nargs=1, help='新的后缀')
    return parser

def batch_rename(work_dir, old_ext, new_ext):
    '''
    传递当前目录，原来后缀名，新的后缀名，批量重命名后缀
    :param work_dir:
    :param old_ext:
    :param new_ext:
    :return:
    '''
    for filename in os.listdir(work_dir):
        #获取得到文件后缀
        split_file = os.path.splitext(filename)
        file_ext = split_file[1]
        if old_ext == file_ext:     #定位后缀名为old_ext的文件
            newfile = split_file[0] + new_ext
            #实现重命名操作
            os.rename(
                os.path.join(work_dir, filename),
                os.path.join(work_dir, newfile)
            )
    print('完成重命名')
    print(os.listdir(work_dir))


def main():
    parser = get_parser()
    args = vars(parser.parse_args())
    work_dir = args['work_dir'][0]
    old_dir = args['old_ext'][0]

    if old_ext[0] != '.':
        old_ext = '.' + old_ext
    new_ext = args['new_ext'][0]
    if new_ext[0] != '.':
        new_ext = '.' + new_ext
    batch_rename(work_dir, old_ext, new_ext)

'''
xls批量转成xlsx
'''
def xls_to_xlsx(work_dir):
    old_ext, new_ext = '.xls', '.xlsx'
    for filename in os.listdir(work_dir):
        #获取得到文件后缀
        split_file = os.path.splitext(filename)
        file_ext = split_file[1]

        #定位后缀名为old_ext的文件
        if old_ext == file_ext:
            #修改后文件的完整名称
            newfile = split_file[0] + new_ext
            #实现重命名
            os.rename(
                os.path.join(work_dir, filename),
                os.path.join(work_dir, newfile)
            )
    print('完成重命名')
    print(os.listdir(work_dir))

xls_to_xlsx('./')

'''
批量获取文件修改时间
os.walk生成文件树结构，os.path.getmtime返回文件的最后一次修改时间
'''
#获取目录下文件的修改时间
from datetime import datetime
print(f'当前时间：{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')

def get_modify_time(indir):
    for root, _, files in os.walk(indir):       #循环目录和子目录
        for file in files:
            whole_file_name = os.path.join(root, file)
            modify_time = os.path.getmtime(whole_file_name)
            nice_show_time = datetime.fromtimestamp(modify_time)
            print('文件{}最后一次修改时间：{}'.format(file, nice_show_time))

get_modify_time('./')

'''
批量压缩文件
导入zipfile模块，压缩和解压的python文件
'''
import zipfile
import time

def batch_zip(start_dir):
    start_dir = start_dir       #要压缩的文件夹路径
    file_news = start_dir + '.zip'      #压缩后文件夹的名字

    z = zipfile.ZipFile(file_news, 'w', zipfile.ZIP_DEFLATED)
    for dir_path, dir_names, file_names in os.walk(start_dir):
        #这一句很重要，不replace的话，就从根目录开始复制
        f_path = dir_path.replace(start_dir, '')
        f_path = f_path and f_path + os.sep     #实现当前文件夹以及包含的所有文件的压缩
        for filename in file_names:
            z.write(os.path.join(dir_path, filename), f_path + filename)
        z.close()
        return file_news
batch_zip(r'E:\working\pythonAlgorithm\gitbook\day09')