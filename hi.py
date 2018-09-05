#!/usr/bin/python
#coding=utf-8

# +. python 之道
import this
"""
优美胜于丑陋（Python 以编写优美的代码为目标）
明了胜于晦涩（优美的代码应当是明了的，命名规范，风格相似）
简洁胜于复杂（优美的代码应当是简洁的，不要有复杂的内部实现）
复杂胜于凌乱（如果复杂不可避免，那代码间也不能有难懂的关系，要保持接口简洁）
扁平胜于嵌套（优美的代码应当是扁平的，不能有太多的嵌套）
间隔胜于紧凑（优美的代码有适当的间隔，不要奢望一行代码解决问题）
可读性很重要（优美的代码是可读的）
不要包容所有错误，除非你确定需要这样做（精准地捕获异常，不写 except:pass 风格的代码）
当存在多种可能，不要尝试去猜测
尽量找一种，最好是唯一一种明显的解决方案（如果不确定，就用穷举法）
这并不容易，因为你不是 Python 之父（这里的 Dutch 是指 Guide）
做也许好过不做，但不假思索就动手还不如不做（动手之前要细思量）
如果你无法向人描述你的方案，那肯定不是一个好方案；反之亦然（方案测评标准）
命名空间是一种绝妙的理念，我们应当多加利用（倡导与号召）
"""

# +. 快速搭建一个Web下载服务器
# python -m SimpleHTTPServer 8890 #(py2) 直接在命令行运行
# python3 -m http.server 8810 #(py3) 直接在命令行运行

# [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)

import os,sys
from os import path

print('\r\n')

# 加载子目录下工具包，可以不断扩展主类
sys.path.append( path.dirname( path.abspath(__file__) ) )
from tools.common import *

print('\r\n')

# +. 获取导入模块的信息
print(dir(os))
print('\r\n')

# +. 排版小技巧
print('Hello'.rjust(20, '*'))
print('Hello'.ljust(20, '-'))
print('Hello'.center(20, '='))
print('\r\n')

# +. 用 sys.exit()提前结束程序
while True:
	print('Type exit to exit.')
	if sys.version_info < (3, 0):
		response = raw_input("input:")
	else:
		response = input("input:")
	if response == 'exit':
		sys.exit()
	print('You typed ' + response + '.')

