#!/usr/bin/python
# -*- coding: UTF-8 -*-
#coding=utf-8

# 定时执行任务

# 准备工作:chmod 0777 clean.py
# 开始:nohup ./clean.py > timer.log 2>&1 & echo $! > run.pid
# 结束:查看 ps -ef | grep timer.py
# 杀死线程:kill pid

# 参考:
# 使用python的sched和Timer执行定时任务:https://gist.github.com/hailxl/1978082
# 时间处理与定时任务:http://www.pythontab.com/html/2013/pythonjichu_0119/146.html
# [Install Pip](https://pip.pypa.io/en/stable/installing/)
# [Book: OReilly.Head.First.Python.2nd.Edition.2016.11.pdf] Chapter 7: Using a Database
# [Python MySQL](https://www.w3schools.com/python/python_mysql_getstarted.asp)
# [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/)
# [Python 使用MySQL](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014320107391860b39da6901ed41a296e574ed37104752000)
# 安装MySQL驱动:
#    > sudo -H pip install --upgrade pip
# [说明] 如果pip安装发生错误，提示locale相关的问题，执行以下操作:
#    > locale -a
#    > export LC_ALL=C
#    [解决pip install时unsupported locale setting错误](http://linfuyan.com/locale_error_unsupported_locale_setting/)

import time, calendar, datetime, os, sched
from time import gmtime, strftime,localtime
from threading import Thread, Timer
import sys


# 定时策略
#    1:指定时间，需设置 hour minute second
#    2:指定循环时间周期 inteval
strategy = 1

# 指定时间 小时 分 秒;默认:05:00:00
hour   = 11
minute = 37
second = 0

# 指定循环时间周期;默认:8小时
# inteval=8*60*60;
# inteval=12*60*60;
inteval = 2 * 60

# 是否第二天才开始执行，否则脚本一开始就执行
# is_tomorrow_start=True
is_tomorrow_start = False

# 设定系统字符集
if sys.version_info < (3, 0):
    reload(sys)
    sys.setdefaultencoding('utf8')


def print_time(name = "定时任务"):
    i = datetime.datetime.now()
    print("")
    c = calendar.TextCalendar(calendar.SUNDAY)
    sc = c.formatmonth(i.year, i.month)
    today = str(i.day)
    toLen = len(str(i.day))
    str_pos = sc.find(today, 20)
    highlight = '\033[31m' + today + '\033[0m'
    # print(str_pos)
    sc = sc[0:str_pos] + highlight + sc[(str_pos+toLen):]
    print(sc)
    if sys.version_info < (3, 0):
        print(name + "开始运行" + ":" + time.ctime())
    else:
        print(name + "开始运行", \
            ":", time.ctime())


def each_day_time(hour, min, sec, next_day = True):
    '''返回当天指定时分秒的时间'''
    struct = localtime()
    if next_day:
        day = struct.tm_mday + 1
    else:
        day = struct.tm_mday
    return time.mktime((struct.tm_year, struct.tm_mon, day,
                        hour, min, sec,
                        struct.tm_wday, struct.tm_yday, struct.tm_isdst))

def perform_command(inc, cmd):
    # 安排inc秒后再次运行自己，即周期运行
    schedule.enter(inc, 0, perform_command, (inc, cmd))
    if cmd == "":
        time = strftime("%Y-%m-%d %H:%M:%S", localtime())
        cmd  = "echo " + time
    os.system(cmd)
    do_action()

#定时触发任务
def timer_interval_task(inc = 60,cmd = ""):
    # enter用来安排某事件的发生时间，从现在起第n秒开始启动
    schedule.enter(inc, 0, perform_command, (inc, cmd))
    # 持续运行，直到计划时间队列变成空为止
    schedule.run()

def perform_action(cmd = ""):
    if cmd == "":
        time = strftime("%Y-%m-%d %H:%M:%S", localtime())
        cmd  = "echo 执行定时任务系统时间:" + time
    os.system(cmd)
    do_action()

class Job(Thread):
    def run(self):
        perform_action()

def do_job():
    job = Job()
    job.start()

def timer_fixed_action(hour = 5,minute = 00, second = 00):
    # 安排指定时间再次运行自己，即周期运行
    schedule.enterabs(each_day_time(hour, minute, second, is_tomorrow_start), 1, print_time, ())
    # 持续运行，直到计划时间队列变成空为止
    schedule.run()
    while(True):
        Timer(0, do_job, ()).start()
        time.sleep(24 * 60 * 60)

# 自定义系统任务
def do_action():
    cmd = "echo 在这里定义需要自定义的任务"
    os.system(cmd)

def main():
    if strategy==1:
        timer_fixed_action(hour, minute, second)
    else:
        #定时执行一次
        timer_interval_task(inteval)

# 第一个参数确定任务的时间，返回从某个特定的时间到现在经历的秒数
# 第二个参数以某种人为的方式衡量时间
schedule = sched.scheduler(time.time, time.sleep)
main()
