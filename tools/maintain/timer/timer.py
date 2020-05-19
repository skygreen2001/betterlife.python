#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#coding=utf-8

# 定时执行任务

# 安装python3 [Ubuntu服务器]
#   sudo apt update
#   sudo apt install software-properties-common
#   sudo add-apt-repository ppa:deadsnakes/ppa
#   sudo apt update
#   sudo apt install python3.7

# 准备工作:chmod 0777 timer.py
# 开始:nohup ./timer.py > timer.log 2>&1 & echo $! > run.pid
# 结束:查看 ps -ef | grep timer.py
# 杀死线程:kill pid

# 参考:
# 使用python的sched和Timer执行定时任务:https://gist.github.com/hailxl/1978082
# 时间处理与定时任务:http://www.pythontab.com/html/2013/pythonjichu_0119/146.html
# [Install Pip](https://pip.pypa.io/en/stable/installing/)
# [Linux服务器CPU、内存、磁盘空间、负载情况查看python脚本](https://yq.aliyun.com/articles/331675)
# 安装requests:
#    > sudo easy_install pip
#    > sudo -H pip install --upgrade pip
#    > pip install requests
#    > pip list
#
#    > sudo apt install python3-pip [python3]
#    > pip3 install requests
#    > pip3 list
# [说明] 如果pip安装发生错误，提示locale相关的问题，执行以下操作:
#    > locale -a
#    > export LC_ALL=C
#    [解决pip install时unsupported locale setting错误](http://linfuyan.com/locale_error_unsupported_locale_setting/)

import sys, os, platform
import re
import time, calendar, datetime, sched
from time import gmtime, strftime, localtime
from threading import Thread, Timer
import requests

# 定时策略
#    1:指定时间，需设置 hour minute second
#    2:指定循环时间周期 inteval
strategy = 1

# 指定时间 小时 分 秒;默认:05:00:00
hour   = 9
minute = 37
second = 0

# 指定循环时间周期;默认:8小时
# inteval=8*60*60;
# inteval=12*60*60;
inteval = 2 * 60

# 是否第二天才开始执行，否则脚本一开始就执行
# is_tomorrow_start=True
is_tomorrow_start = False

# 需清理日志所在的路径
# log_dir_clear = "/var/log/msg_server"
# log_dir_clear = "/root/bak/app"

log_dir_clears = [
    "/root/debug/tomcat9/logs",
    "/var/log/msg_server"
    # "/var/log/msg_server"
    # "/root/bak/app"
]

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

# 查看磁盘空间大小
def safe_disk():

    diskinfo = os.popen('df -h')
    #此时打开的diskinfo是一个对象，如果直接打印的话是对象内存地址

    text = diskinfo.read()
    #要用read（）方法读取后才是文本对象

    # print(text)
    diskinfo.close()#打印后还需将对象关闭

    for line in text.splitlines():
        print(line)
    

    statvfs = os.statvfs('/')

    total_disk_space = statvfs.f_frsize * statvfs.f_blocks
    free_disk_space = statvfs.f_frsize * statvfs.f_bfree
    disk_usage = (total_disk_space - free_disk_space) * 100.0 / total_disk_space
    disk_usage = int(disk_usage)
    disk_tip = "硬盘空间使用率（最大100%）：" + str(disk_usage)+"%"
    print(disk_tip)
    if (disk_usage >=85):
        print('\033[31m' + "磁盘不足，需要进行清理！" + '\033[0m')

# 清理内存
def clear_cache():
    pt = platform.system()
    if(pt =="Windows"):
        print ("Windows")
    elif(pt == "Linux"):
        os.system("sync; echo 1 > /proc/sys/vm/drop_caches")
    elif(pt == "Darwin"):
        print("Mac OS")
    else:
        print ("Other System")

# 清理日志文件
# 只保留7天的日志(包括今天在内)
def clear_logs():
    date = strftime("%Y-%m-%d", localtime())
    # print("logFile." + date + ".log")

    # tdate = strftime("%Y%m%d", localtime())
    # for root,dirs,files in os.walk(log_dir_clear):
    #     for file in files:
    #         date = ''.join([x for x in file if x.isdigit()])
    #         if (date and int(date) <= int(tdate) - 7):
    #             os.remove(root + "/" + file)

    tdate = time.time()
    clearTime = 7 * 24 * 60 * 60
    for log_dir_clear in log_dir_clears:
        for root, dirs, files in os.walk(log_dir_clear):
            nameMap = {}
            # 将所有文件进行分类
            for file in files:
                date = ''.join([x for x in file if not(x.isdigit())])
                # 判断是否存在 不存在设置为【】
                nameMap.setdefault(date, [])
                nameMap[date].append(file)
            if (any(nameMap)):
                # 遍历多有类型
                for key in nameMap.keys():
                    value = nameMap[key]
                    # 只保留最后七个
                    if (len(value) > 7):
                        value.sort()
                        for file in value[0: (len(value) - 7)]:
                            os.remove(root + "/" + file)
                            print(root + "/" + file)

# [Requests: HTTP for Humans™](https://2.python-requests.org)
def visit_http():
    # r = requests.get('https://api.github.com/events')
    # print(r.text)
    r = requests.get("http://open.iciba.com/dsapi/")
    content = r.json()['content']
    note = r.json()['note']
    print(content)
    print(note)

# 自定义系统任务
def do_action():
    cmd = "echo 在这里定义需要自定义的任务"
    os.system(cmd)
    clear_cache()
    clear_logs()
    safe_disk()
    visit_http()

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
