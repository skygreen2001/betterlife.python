#!/usr/bin/python
# -*- coding: UTF-8 -*-
#coding=utf-8

# 安装需导入的模块
#    > sudo easy_install pip             (服务器需先安装Pip)
#    > sudo -H pip install --upgrade pip
#    > pip install pyperclip

import sys,pyperclip

# 剪贴板 📋 
text=pyperclip.paste()
#Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)): # loop through all indexes for "lines" list
    lines[i] = '* ' + lines[i] # add star to each string in "lines" list
text = '\n'.join(lines)
print(text)
pyperclip.copy(str(text))

# 设定系统字符集 
reload(sys)
sys.setdefaultencoding('utf8')
# 用其它第三方应用复制文本
if sys.version_info < (3, 0):
	response = raw_input("input:")
else:
	response = input("input:")
paste=pyperclip.paste()
print(paste)
	
pyperclip.copy("you input:"+response)
paste=pyperclip.paste()
print(paste)
	
pyperclip.copy('skygreen is cool')
paste=pyperclip.paste()
print(paste)
