#!/usr/bin/python
# -*- coding: UTF-8 -*-
# coding=utf-8

#目标: 通用方法
# [python cheatsheet](https://zhuanlan.zhihu.com/p/26459091)
import os,sys,random,time,copy,pprint
import string
from os import getcwd
from distutils.sysconfig import get_python_lib
from itertools import product

# +. 显示系统版本信息
print(sys.version)
print('\r\n')

# +. 获取当前路径
where_am_I = getcwd()
print where_am_I
print('\r\n')

# +. 获取python安装路径
print(get_python_lib())
print('\r\n')

# +. 自定义格式输出
ISOTIMEFORMAT='%Y-%m-%d %X'
print(time.strftime( ISOTIMEFORMAT, time.localtime() ))
print('\r\n')

# +. 获取当前时间
print("[Info]NowTimeis:",time.ctime())
print('\r\n')

# +. 查看系统环境变量
print(os.environ["PATH"])
print('\r\n')

# +. 判断数据类型
print(isinstance("123",(str)))
print(isinstance("123",(int,long,float,complex)))
print(isinstance(123,(int,long,float,complex)))
print('\r\n')

# +. 字符串倒置 
a =  "codementor"
a = a[::-1]
print(a)

# +. 字符串首字母变大写
info = 'ssfef'
print(info.capitalize())
print(info.title())

# +. itertools迭代器
p = product("ABCD", repeat=3)
for n in p:
	print(n)
print('\r\n')

# +. 随机数示例
def getAnswer(answerNumber):
	if answerNumber == 1:
		return 'It is certain'
	elif answerNumber == 2:
		return 'It is decidedly so'
	elif answerNumber == 3:
		return 'Yes'
	elif answerNumber == 4:
		return 'Reply hazy try again'
	elif answerNumber == 5:
		return 'Ask again later'
	elif answerNumber == 6:
		return 'Concentrate and ask again'
	elif answerNumber == 7:
		return 'My reply is no'
	elif answerNumber == 8:
		return 'Outlook not so good'
	elif answerNumber == 9:
		return 'Very doubtful'

for i in range(9):
	r = random.randint(1, 9)
	fortune = getAnswer(r)
	print(str(r)+":"+fortune)

print('\r\n')

# +. 列表
spam = ['X', 'Y', 'Z'] * 3; # 列表复制
print(spam)

spam = ['cat', 'bat', 'rat', 'elephant'] 
del spam[2] # 从列表中删除值
spam.remove('bat') # 从列表中删除值asd
print(spam)

# copy 模块的 copy()和 deepcopy()函数
spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)
cheese[1] = 42
print spam
print cheese
cheese = spam
cheese[1] = 88
print(spam)
print('\r\n')

# 多重赋值技巧
cat = ['fat', 'black', 'loud']
size, color, disposition = cat
print (size + "," + disposition + "," + color)
print('\r\n')

# 列表去重
ids = [1,4,3,3,4,2,3,4,5,6,1]
ids = list(set(ids))
print(ids)
print('\r\n')

# 列表运算
a = [1,2,3]
b = [3,4,5]
print(set(a)&set(b)) #与
print(set(a)|set(b)) #或
print(set(a)-set(b)) #非

# 单列表元素合并成字符串
a = ["Code", "mentor", "Python", "Developer"]
print(" ".join(a))
print('\r\n')

# 多列表元素分别相加
list1 = ['a', 'b', 'c', 'd']
list2 = ['p', 'q', 'r', 's']
for x, y in zip(list1,list2):  
    print(x+y)

# 列表内元素相加
a=[1,2,3] #（数字）
print(sum(a))
print('\r\n')

# 列表用于循环
catNames = []
while True:
	print('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.):')
	if sys.version_info < (3, 0):
		name = raw_input("input:")
	else:
		name = input("input:")
	if name == '':
		break
	catNames = catNames + [name] # list concatenation
catNames.sort() # 用 sort()方法将列表中的值排序

print('The cat names are:')
for name in catNames:
	print(' ' + name)

catNames.sort(reverse=True) # 用 sort()方法将列表中的值排序
print('Confirm again the cat names are:')
for i in range(len(catNames)):
	print(str(i) +': ' + catNames[i])

# +. itertools迭代器
p = product(["A","B","C","D"], repeat=3)
for n in p:
	print(n)
print('\r\n')

# +. 字典
# 漂亮打印
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
	count.setdefault(character, 0)
	count[character] = count[character] + 1
pprint.pprint(count)

print('\r\n')

# 列举所有字母
print(string.ascii_uppercase) #所有大写字母
print(string.ascii_lowercase) #所有小写字母
print(string.ascii_letters) #所有字母（包括大小写）

# +. 获取控制台大小(多少行, 多少列)  [只能在命令行工具里执行]
# rows, columns = os.popen('stty size', 'r').read().split()
# print(rows, columns)