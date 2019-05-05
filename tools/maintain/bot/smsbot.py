#!/usr/bin/python
# -*- coding: UTF-8 -*-
#coding=utf-8

# [利用python库twilio来免费发送短信](https://cuiqingcai.com/5696.html)
# [使用python免费发送短信](https://blog.csdn.net/qq_40925239/article/details/86149126)
# [The Twilio Python Helper Library](https://www.twilio.com/docs/libraries/python)
# pip install twilio
# pip3 install twilio
# easy_install twilio

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC674864e248a3261f7b5f25736e1720f7"
# Your Auth Token from twilio.com/console
auth_token  = "21191f324ebaf147c1ed3621ab067883"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+86 139 1732 0293", 
    from_="+12024100217",
    body="Hello from Python!")

print(message.sid)