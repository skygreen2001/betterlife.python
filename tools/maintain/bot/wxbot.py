#!/usr/bin/python
# -*- coding: UTF-8 -*-
#coding=utf-8

# 微信机器人

# [微信机器人](https://github.com/youfou/wxpy)
# [wxpy: 用 Python 玩微信](https://wxpy.readthedocs.io/zh/latest/index.html)

# pip3 install -U wxpy
# pip3 install pillow

from __future__ import unicode_literals
from wxpy import *
import logging
from threading import Timer
import requests

# from wxpy import get_wechat_logger, WeChatLoggingHandler


# 初始化机器人，扫码登陆
bot = Bot(True, True)

bot.auto_mark_as_read = True

# 向文件传输助手发送消息
bot.file_helper.send('Hello from wxpy!')
bot.file_helper.send('It\'s my first message!')

# 启用 puid 属性，并指定 puid 所需的映射数据保存/载入路径
bot.enable_puid('wxpy_puid.pkl')

# 指定一个好友
if sys.version_info < (3, 0):
    # 你朋友的微信名称，不是备注，也不是微信帐号。
    my_friend = bot.friends().search('杨俊杰'.decode("utf-8"))[0]
    my_friend.send('What\'s your liked songs?')
else:
    my_friend = bot.friends().search('杨俊杰')[0]
    my_friend.send('喜欢听什么歌曲？')
    myself = bot.friends().search('周月璞')[0]
    # myself.send('你是我吗？')
    print(myself)

print(my_friend)
print(my_friend.puid)

# 机器人账号自身
myself = bot.self
print(bot.self)

# 在 Web 微信中把自己加为好友
# bot.self.add()
# bot.self.accept()

# 发送消息给自己
# bot.self.send('Can you accept?')
# myself.send('能收到吗？')
# myself.send('Can you accept?')
# myself.send('喜欢听什么歌曲？')

# 搜索群聊
if sys.version_info < (3, 0):
    wxpy_groups = bot.groups().search('管弄小学'.decode("utf-8"))
else:
    wxpy_groups = bot.groups().search('管弄小学')
fg = ensure_one(wxpy_groups)
print(fg)
len(fg) # 这个群的成员数量

# 打印所有群成员
for member in fg:
    print(member)

# 搜索该群中所有浙江的群友
found = fg.search(province='山东')
found = fg.search(city='上海')
found = fg.search(province='上海')
print(found)

# 指定一个好友
# myself = bot.friends().search('周月璞')
# me = ensure_one(myself)
# print(me)
# me.send('Can you accept?')

# myself = bot.friends().search('周月', sex=MALE, city='上海')[0]
# myself = bot.friends().search('周月', city='上海')[0]
# myself.send('Can you accept?')

# my_friend = bot.friends().search('杨'.decode("utf-8"), sex=MALE)
# my_friend = bot.friends().search('杨'.decode("utf-8"), sex=MALE, city="河南")[0]
# my_friend = bot.friends().search('周'.decode("utf-8"), city="上海")[0]
# my_friend = bot.friends().search('', city="上海")[0]
# my_friend = bot.friends().search('游否'.decode("utf-8"), sex=MALE, city="深圳")[0]


# [python实战===教你用微信每天给女朋友说晚安](https://www.cnblogs.com/botoo/p/8622379.html)

# bot = Bot()
# linux执行登陆请调用下面的这句
#bot = Bot(console_qr=2,cache_path="botoo.pkl")
def get_news():
    
    """获取金山词霸每日一句，英文和翻译"""
    
    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    content = r.json()['content']
    note = r.json()['note']
    return content, note


def send_news():
    try:
        content, note = get_news()
        # 你朋友的微信名称，不是备注，也不是微信帐号。
        my_friend = bot.friends().search(u'杨俊杰')[0]
        my_friend.send(content)
        my_friend.send(note)
        my_friend.send(u"Have a good night!")
        # 每86400秒（1天），发送1次
        t = Timer(86400, send_news)
        t.start()
    except:
        # 你的微信名称，不是微信帐号。
        my_friend = bot.friends().search('周月璞')[0]
        my_friend.send(u"今天消息发送失败了")


if __name__ == "__main__":
    send_news()

# ###################### 发送日志到: 微信 文件传输助手 ###########################
# # 获得一个专用 Logger
# # 当不设置 `receiver` 时，会将日志发送到随后扫码登陆的微信的"文件传输助手"
# logger = get_wechat_logger()

# # 发送警告
# logger.warning('这是一条 WARNING 等级的日志，你收到了吗？')

# # 接收捕获的异常
# try:
#     1 / 0
# except:
#     logger.exception('现在你又收到了什么？')

# ###################### 发送日志到: 指定用户 ###########################
# bot = Bot(True, True)
# logger_receiver = bot.friends().search('杨俊杰')[0]

# # 指定这个群为接收者
# logger = get_wechat_logger(logger_receiver)

# logger.error('打扰您了，但这是一条重要的错误日志...')

# 堵塞线程，并进入 Python 命令行
embed()