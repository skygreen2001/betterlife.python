#!/usr/bin/python
# -*- coding: UTF-8 -*-
#coding=utf-8

# 目标: 定时执行数据库备份任务
# 准备工作:chmod 0777 db_mysql_timer_bak.py
# 开始:nohup ./trip_user_summary_bak.py > dbbak.log 2>&1 & echo $! > run.pid
# 结束:查看 ps -ef | grep db_mysql_timer_bak.py
# 杀死线程:kill -9 pid

# 参考:
#    使用python的sched和Timer执行定时任务:https://gist.github.com/hailxl/1978082
#    时间处理与定时任务:http://www.pythontab.com/html/2013/pythonjichu_0119/146.html
#    Python备份数据库:http://www.jb51.net/article/15461.htm
#    python写的备份mysql自动上传ftp服务器:http://deidara.blog.51cto.com/400447/342687/

# 准备工作:
#    http://bbaobelief.blog.51cto.com/3838275/901598
#    由于系统默认会查找/usr/bin下的命令，如果这个命令不在这个目录下，当然会找不到命令
#    1.首先得知道mysqldump命令的完整路径，可以使用find命令查找:find  / -name mysqldump
#    2.ln -s /usr/local/webserver/mysql/bin/mysqldump /usr/bin/mysqldump

import time, os, sched
import ftplib
import traceback
from time import gmtime, strftime,localtime
from threading import Thread, Timer

# config vars
# 路径分割符，*nix用"/" win32用"\\"
systempathchr="/"

# 数据库用户名
dbuser="root"

# 数据库密码
dbpwd=""
# dbpwd=""

# 需要备份那些数据库
dbnamelist=["bb","betterlife"]

# 本地备份文件夹
workdir="/root/zyp/"
#workdir="/Users/pupu/python/bak/"

# 定时策略
#    1:指定时间，需设置 hour minute second
#    2:指定循环时间周期 inteval
strategy=1

# 指定时间 小时 分 秒;默认:05:00:00
hour=5
minute=0
second=0

# 指定循环时间周期;默认:8小时
inteval=8*60*60;

def each_day_time(hour,min,sec,next_day=True):
    '''返回当天指定时分秒的时间'''
    struct = localtime()
    if next_day:
        day = struct.tm_mday + 1
    else:
        day = struct.tm_mday
    return time.mktime((struct.tm_year,struct.tm_mon,day,
        hour,min,sec,struct.tm_wday, struct.tm_yday,
        struct.tm_isdst))

def print_time(name="机器人"):
    print name, ":","开始运行",\
        time.time()," :", time.ctime()

def dumpdb(dbname):
    if strategy==1:
        timeformat="%Y%m%d"
    else:
        timeformat="%Y%m%d%H%M%S"

    sqlvalformat="mysqldump -u%s -p\"%s\" \"%s\" >\"%s\""
    tarvalformat="tar --directory=\"%s\" -zcf \"%s\" \"%s\""
    nowdate=time.strftime(timeformat)
    #print(nowdate)
    timeF=strftime("%Y%m%d%H%M%S", localtime())
    dumpfile=os.path.join(workdir,dbname+timeF+".sql.bak")
    zipfile=os.path.join(workdir,dbname+nowdate+".tar.gz")
    sqlval=sqlvalformat % (dbuser,dbpwd,dbname,dumpfile)
    if not os.path.isdir(workdir):
        os.mkdir(workdir)
    result=os.system(sqlval)
    tarval=tarvalformat % (workdir,zipfile,dbname+timeF+".sql.bak")
    result=os.system(tarval)
    os.remove(dumpfile)

def getfilename(path):
    pt=path.rfind(systempathchr)
    return path[pt+1:]

def perform_command(inc,cmd):
    # 安排inc秒后再次运行自己，即周期运行
    schedule.enter(inc, 0, perform_command, (inc,cmd))
    if cmd=="":
        time=strftime("%Y-%m-%d %H:%M:%S", localtime())
        cmd="echo "+time
    os.system(cmd)
    for dbname in dbnamelist:
        dumpdb(dbname)

# 定时触发任务
def timming_interval_task(inc = 60,cmd=""):
    # enter用来安排某事件的发生时间，从现在起第n秒开始启动
    schedule.enter(inc, 0, perform_command, (inc,cmd))
    # 持续运行，直到计划时间队列变成空为止
    schedule.run()

def perform_mysql_bak(cmd=""):
    if cmd=="":
        time=strftime("%Y-%m-%d %H:%M:%S", localtime())
        cmd="echo 数据库备份时间:"+time
    os.system(cmd)
    for dbname in dbnamelist:
        dumpdb(dbname)

class Job(Thread):
    def run(self):
        perform_mysql_bak()

def do_mysql_bak():
    job = Job()
    job.start()

def timming_mysql_bak(hour=05,minute=00,second=00):
    # 安排指定时间再次运行自己，即周期运行
    schedule.enterabs(each_day_time(hour,minute,second,True), 1, print_time, ())
    # 持续运行，直到计划时间队列变成空为止
    schedule.run()
    while(True):
        Timer(0, do_mysql_bak, ()).start()
        time.sleep(24 * 60 * 60)

def main():
    if strategy==1:
        timming_mysql_bak(hour,minute,second)
    else:
        #定时执行一次
        timming_interval_task(inteval)


# 第一个参数确定任务的时间，返回从某个特定的时间到现在经历的秒数
# 第二个参数以某种人为的方式衡量时间
schedule = sched.scheduler(time.time, time.sleep)
main()
