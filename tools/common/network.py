#!/usr/bin/python
# -*- coding: UTF-8 -*-
# coding=utf-8

#目标: 网络操作

import socket,urllib.request
import pprint

# 域名解析为ip
domain = "www.qq.com"
ip     = socket.getaddrinfo(domain,'http')[0][4][0]
print(ip)

# 获取服务器版本信息
sUrl   = 'http://www.qq.com'
sock   = urllib.request.urlopen(sUrl)
header = sock.headers
print(header)
pp = pprint.PrettyPrinter(depth=6)
pp.pprint(header.values())

