#!/usr/bin/python
# -*- coding: UTF-8 -*-
# coding=utf-8

# 目标: 命令行中显示选择列表
# [create curses based interactive selection list in the terminal](https://github.com/wong2/pick)
# [python curses addrstr中文乱码问题](https://blog.csdn.net/whwq2012/article/details/51076857)
# 安装需导入的模块
#    > sudo pip install pick
#    > sudo python3 -m pip install --upgrade pip (python3 安装包)
#    > sudo python3 -m pip install pick (python3 安装包)
# 注释: 本示例必须在命令行工具内使用
from __future__ import print_function
from pick import pick
from pick import Picker
import sys,curses,locale

# pick使用了python curses screen addrstr的方法, 参考: [python curses addrstr中文乱码问题] 解决办法
locale.setlocale(locale.LC_ALL, '')

print(sys.getdefaultencoding())

# 示例: 控制台字体颜色控制
red = '\033[1;31m'
green = '\033[1;32m'
yellow = '\033[1;33m'
white = '\033[1;37m'
reset = '\033[0m'

print(red + "红色" + reset)
print(green + "绿色" + reset)
print(yellow + "黄色" + reset)

# 示例: 单选
title = 'Please choose your favorite programming language: '
options = ['Java', 'JavaScript', 'Python', 'PHP', 'C++', 'Erlang', 'Haskell']
option, index = pick(options, title)
print(option, index)
print(option)
print(index)
curses.endwin()

# 示例: 多选
title = 'Please choose your favorite programming language (press SPACE to mark, ENTER to continue): '
options = ['Java', 'JavaScript', 'Python', 'PHP', 'C++', 'Erlang', 'Haskell']
selected = pick(options, title, multi_select=True, min_selection_count=1)
print(selected)

# 示例: 替换选中指示符
title = 'Please choose your favorite programming language: '
options = ['Java', 'JavaScript', 'Python', 'PHP', 'C++', 'Erlang', 'Haskell']
option, index = pick(options, title, indicator='=>', default_index=2)
print(option, index)
print(option)
print(index)
curses.endwin()

# 示例: 鼠标滚动选择
title = 'Select:'
options = ['只为更好%s.db.bak' % x for x in range(1, 71)]
option, index = pick(options, title)
print(option, index)

# 示例: Register custom handlers(键入向左键盘时，退出)
def go_back(picker):
    return (None, -1)

title = 'Please choose your favorite programming language: '
options = ['Java', 'JavaScript', 'Python', 'PHP', 'C++', 'Erlang', 'Haskell']

picker = Picker(options, title)
picker.register_custom_handler(curses.KEY_LEFT, go_back)
option, index = picker.start()
print(option, index)

# 示例: Options Map Function
title = 'Please choose your favorite fruit: '
options = [
    { 'name': 'Apples', 'grow_on': 'trees' },
    { 'name': 'Oranges', 'grow_on': 'trees' },
    { 'name': 'Strawberries', 'grow_on': 'vines' },
    { 'name': 'Grapes', 'grow_on': 'vines' },
]

def get_description_for_display(option):
    # format the option data for display
    return '{0} (grow on {1})'.format(option.get('name'), option.get('grow_on'))

option, index = pick(options, title, indicator='=>', options_map_func=get_description_for_display)
print(option, index)
