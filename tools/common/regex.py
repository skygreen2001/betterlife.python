#!/usr/bin/python
# -*- coding: UTF-8 -*-
#coding=utf-8

# 目标: 正则表达式示例
import re

# 匹配 Regex 对象
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
print('Phone number found: ' + str(mo.group()))

phones = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(phones)

phoneNumRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo2 = phoneNumRegex.search('My number is 555-4242')
print(str(mo2.group()))

atRegex = re.compile(r'.at')
ats = atRegex.findall('The cat in the hat sat on the flat mat.')
print(ats)

# 不区分大小写的匹配: re.I
robocop = re.compile(r'robocop', re.I)
ros=robocop.search('RoboCop is part man, part machine, all cop.').group()
print(ros)

# 替换字符串
agentNamesRegex = re.compile(r'Agent (\w)\w*')
anr = agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(anr)


# Create email regex.
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # username
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4}){1,2} # dot-something
    )''', re.VERBOSE)


email=emailRegex.search('my name is skygreen,my email is skygreen2001@gmail.com,my nickname is pupu.').group()
print(email)
