#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, cmd
from bbtools import *

work_dir = '/Users/skygreen/'
output_dir = '/Users/skygreen/Workspace/betterlife.python/'

class PyBB(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self) # initialize the base class
        self.QUERYDIR = work_dir
        self.OUTPUTDIR = output_dir
        
        self.prompt="(PyBB)>"
        self.intro = '''PyBB1.0 使用说明:
    dir 目录名 #指定保存和搜索目录,搜索目录默认是 "/Users/skygreen/",保存目录默认是 "/Users/skygreen/Workspace/betterlife.python/"
    walk 文件名 #指定输出目录文件名,使用 "*.txt" 
    find 关键词 #使用在保存和搜索目录中遍历所有.txt 文件,输出含有关键词的行
    ? #查询
    EOF # 退出系统,也可以使用 Crtl+D(Unix)|Ctrl+Z(Dos/Windows)
        '''
    def help_EOF(self):
        print "退出程序 Quits the program"
    def do_EOF(self, line):
        sys.exit()
    def help_exit(self):
        print "退出"
    def do_exit(self,line):
        sys.exit()
    def help_walk(self):
        print "扫描指定查询目录并将所有文件明细 导出到 *.txt"
    def do_walk(self,filename):
        if filename == "":filename = raw_input("输入输出文件名: ")
        print "扫描指定目录内容保存到:'%s%s'" % (self.OUTPUTDIR,filename)
        bbWalker(self.QUERYDIR,self.OUTPUTDIR+filename)
    def help_dir(self):
        print "指定保存/搜索目录"
    def do_dir(self, pathname):
        if pathname == "":pathname = raw_input("输入指定保存/搜索目录: ")
        print "指定保存/搜索目录:'%s';默认是:'%s'" % (pathname,self.QUERYDIR)
        self.QUERYDIR = pathname
    def help_find(self):
        print "搜索关键词"
    def do_find(self, keyword):
        if keyword == "":keyword = raw_input("输入搜索关键字: ")
        print "搜索关键词:'%s'" % keyword
        bbGrep(self.OUTPUTDIR,keyword)

if __name__ == '__main__': # this way the module can be
    bb = PyBB()
    bb.cmdloop()
