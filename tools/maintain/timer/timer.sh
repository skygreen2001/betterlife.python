#!/bin/bash
# 查询脚本所在的进程是否在后台运行: ps -aux|grep timer.py
# nohup和&后台运行，进程查看及终止: https://www.cnblogs.com/cfas/p/9348880.html
nohup /root/app/timer/timer.py > timer.log 2>&1 & echo $! > run.pid
sync; echo 1 > /proc/sys/vm/drop_caches;
