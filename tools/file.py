#!/usr/bin/python
# -*- coding: UTF-8 -*-
#coding=utf-8

dest_dir = "/Users/skygreen/Workspace/ittrconsole/"
# 目标: 文件操作
import os, glob
# 输出一个目录下所有文件名称
def search(path):
    export = []
    for root,dirs,files in os.walk(path):
        for file in files:
            print(root + "/" + file)

# def search(path):
#     if os.path.isdir(path):  #如果是目录
#         files=os.listdir(path)  #列出目录中所有的文件
#         for file in files:
#             i=os.path.join(path,file)  #构造文件路径
#             search(i)           #递归
#     elif os.path.isfile(path): #如果是文件
#         print(path)   #输出文件名

search(dest_dir)

# 文件查找
# 查找文件只用到三个匹配符：”*”, “?”, “[]“
# ”*”匹配0个或多个字符；
# ”?”匹配单个字符；
# ”[]“匹配指定范围内的字符，如：[0-9]匹配数字。
print(glob.glob(dest_dir + "*.py"))     #返回的是一个列表









