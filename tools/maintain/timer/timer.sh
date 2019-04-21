#!/bin/bash
nohup /root/app/timer/timer.py > timer.log 2>&1 & echo $! > run.pid
sync; echo 1 > /proc/sys/vm/drop_caches;
