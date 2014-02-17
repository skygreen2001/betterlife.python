#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,sys

def bbWalker(queryDir,outputTxtFile):
    export = []
    for root,dirs,files in os.walk(queryDir):
        export.append("\n %s;%s;%s" % (root,dirs,files))    
    open(outputTxtFile,"w").write(''.join(export))
 
def bbGrep(filepath,keyword):
    filelist = os.listdir(filepath)
    for file in filelist:
        # 搜索目录中的文件
        # 循环文件列表
        # 过滤可能的其它文件,只关注.cdc
        if ".txt" in file:
            queryfile = open(filepath+file)
            for line in queryfile.readlines(): # 读取文件每一行,并循环
                # 拼合文件路径,并打开文件
                if keyword in line: # 判定是否有关键词在行中
                    print line # 打印输出

if __name__ == '__main__':     # this way the module can be
    #print os.listdir("/Users/pupu")
    print sys.argv
    queryDir=sys.argv[1];outputTxtFile=sys.argv[2]
    bbWalker(queryDir,outputTxtFile)
    #fileWalker("/Users/pupu/dev/eclipse","/Users/pupu/python/output2.txt")
    