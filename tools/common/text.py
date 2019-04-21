#!/usr/bin/python
# -*- coding: UTF-8 -*-
# coding=utf-8

# 目标: 字符串方法
# [Book: Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)

import string

# +. String Concatenation and Replication
print('Alice' + 'Bob')
print('Alice' * 5)

# +. Escape Characters
print("Hello there!\nHow are you?\nI\'m doing fine.")

# +. Raw Strings
print(r'That is Carol\'s cat.')

# +. Multiline Strings with Triple Quotes
print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob''')

# +. 排版小技巧
print('Hello'.rjust(20, '*'))
print('Hello'.ljust(20, '-'))
print('Hello'.center(20, '='))
print('\r\n')

# +. 字符串倒置 
a =  "codementor"
a = a[::-1]
print(a)

# +. find, index, rfind, rindex
subject = "take exam: this is string example....wow!!!"
subStr = "exam"
print(subject.index(subStr))
print(subject.index(subStr, 10))
print(subject.find(subStr))
print(subject.find(subStr, 10))

# +. substring, Indexing and Slicing Strings
spam = 'Hello world!'
print(spam[0:5])

# +. in and not in Operators
print('Hello' in 'Hello World')
print('cats' not in 'cats and dogs')

# +. 字符串首字母变大写
info = 'ssfef'
print(info.capitalize())
print(info.title())

# +. upper, lower, isupper, islower, startswith, endswith
spam = 'Hello world!' 
print(spam.upper())
print(spam.isupper())
print(spam.lower())
print(spam.islower())

print('Hello world!'.startswith('Hello'))
print('Hello world!'.endswith('world!'))

# +. join and split
print(', '.join(['cats', 'rats', 'bats']))
print(' '.join(['My', 'name', 'is', 'Simon']))
print('My name is Simon'.split())
print('MyABCnameABCisABCSimon'.split('ABC'))

# +. Removing Whitespace 
spam = ' Hello World '
print(spam.strip())
print(spam.lstrip())
print(spam.rstrip())

# +. 
print()

# +. 
print()


# 列举所有字母
print(string.ascii_uppercase) #所有大写字母
print(string.ascii_lowercase) #所有小写字母
print(string.ascii_letters) #所有字母（包括大小写）