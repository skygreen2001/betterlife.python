#!/usr/bin/python
# -*- coding: UTF-8 -*-
#coding=utf-8

# 目前仅python3可以使用: python3 db_handle.py
# [Install Pip](https://pip.pypa.io/en/stable/installing/)
# [Book: OReilly.Head.First.Python.2nd.Edition.2016.11.pdf] Chapter 7: Using a Database
# [Python MySQL](https://www.w3schools.com/python/python_mysql_getstarted.asp)
# [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/)
# [Python 使用MySQL](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014320107391860b39da6901ed41a296e574ed37104752000)
# [learn-python3](https://github.com/michaelliao/learn-python3)
# 安装MySQL驱动:
#    > sudo easy_install pip             (服务器需先安装Pip)
#    > sudo -H pip install --upgrade pip
#    > pip install mysql-connector
import sys
# 目前仅python3可以使用
import mysql.connector
from importlib import reload

dbconfig = {
    'host': '127.0.0.1',
    'user': 'root',
    'port': '3306',
    'password': '',
    'database': 'betterlife'
}

if sys.version_info < (3, 0):
    # 设定系统字符集
    reload(sys)
    sys.setdefaultencoding('utf8')

# 打开数据库连接
db = mysql.connector.connect(
	host=dbconfig['host'],
    port=dbconfig['port'],
	user=dbconfig['user'],
	password=dbconfig['password'],
	database=dbconfig['database']
)

db.set_charset_collation('utf8mb4', 'utf8mb4_general_ci')

#print(db)

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()
print("Database version : %s " % data)
print("\r\n")

cursor.execute('select * from bb_user_user where user_id = %s', ('1',))
values = cursor.fetchall()
print(values)
print("\r\n")

cursor.execute('select * from bb_core_blog')
values = cursor.fetchall()
print(values)
print("\r\n")

cursor.execute('select blog_id,blog_name from bb_core_blog')
for blog_id,blog_name in cursor:
    print('blog_id:{}, blog_name:{}'.format(blog_id, blog_name))
print("\r\n")

cursor.execute('select blog_id,blog_content from bb_core_blog')
for blog_id,blog_content in cursor:
    print('blog_id:%d, blog_content:%s'%(blog_id, blog_content))
print("\r\n")

# 关闭Cursor和Connection:
cursor.close()

# 关闭数据库连接
db.close()
