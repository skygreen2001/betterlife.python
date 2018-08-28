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
import sys,random,copy,pprint
from os import getcwd

print '\r\n'

print(sys.version)

print '\r\n'

where_am_I = getcwd()
print where_am_I

print '\r\n'

print('Hello'.rjust(20, '*'))
print('Hello'.ljust(20, '-'))
print('Hello'.center(20, '='))

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

print '\r\n'
	

# +. 列表
spam = ['X', 'Y', 'Z'] * 3; # 列表复制
print spam;

spam = ['cat', 'bat', 'rat', 'elephant'] 
del spam[2] # 从列表中删除值
spam.remove('bat') # 从列表中删除值asd

print spam;

# copy 模块的 copy()和 deepcopy()函数
spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)
cheese[1] = 42
print spam
print cheese
cheese = spam
cheese[1] = 88
print spam

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
	
# 多重赋值技巧
cat = ['fat', 'black', 'loud']
size, color, disposition = cat
print (size + "," + disposition + "," + color)
	
print '\r\n';

# +. 字典
# 漂亮打印
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
	count.setdefault(character, 0)
	count[character] = count[character] + 1
pprint.pprint(count)

print '\r\n';
	
# +. Collatz 序列（考拉咨猜想）包含有 递归写法
def collatz(number):
	print(number)
	if number == 1:
		print 'Collatz Test End'
		# sys.exit()
	elif number % 2 == 1:
		t=3 * number + 1
		collatz(t)
	else:
		t=number // 2
		collatz(t)
		
def collatz_test():
    print('Enter number:')
    try:
        number  = int(input())
        collatz(number)
    except ValueError as verror:
        print('ValueError: You need input digital.')
    except:
        print('ValueError: You need input any digital.')
         
collatz_test()

print '\r\n'

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