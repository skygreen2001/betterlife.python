#!/usr/bin/python
# -*- coding: UTF-8 -*-
#coding=utf-8

# 安装需导入的模块
#    > sudo easy_install pip             (服务器需先安装Pip)
#    > sudo -H pip install --upgrade pip
#    > pip install pyperclip

import sys,pyperclip

# 设定系统字符集 
reload(sys)
sys.setdefaultencoding('utf8')

# 剪贴板 📋 
pyperclip.copy('skygreen is cool')
paste=pyperclip.paste()
print(paste)

if sys.version_info < (3, 0):
	response = raw_input("input:")
else:
	response = input("input:")
	
pyperclip.copy('skygreen input:' + response)
paste=pyperclip.paste()
print(paste)

# 用其它第三方应用复制文本
if sys.version_info < (3, 0):
	response = raw_input("input:")
else:
	response = input("input:")
paste=pyperclip.paste()
print(paste)