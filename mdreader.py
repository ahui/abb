#!/usr/bin/python
# coding=utf-8
# 用于解析md文件
#Ahui at ahui.us, 2014

import sys

reload(sys)
sys.setdefaultencoding('utf-8')   

class md:
    title = ""
    date = ""
    tags = []
    body = ""
    def __init__(self,filename):
        with open(filename,'r') as fp:
            self.tags = []
            tdict = {}
            tlist = []
            last = ""
            while 1:
                line = fp.readline()
                #第一个空行之后为body,linux下只用判断\n，win下判断\n\r, mac os下判断\r
                #if line == "\r" or line[0:3] == "---" or line == "\n" or line == "\n\r":
                if line == "\n":
                    self.title = tdict['title']
                    self.date = tdict['date']
                    self.body = fp.read()
                    break
                else:
                    tlist = line.split(":",1)
                    if len(tlist) > 1:
                        tdict[tlist[0].lower()]=tlist[1].replace("\n","").replace('"','').strip()
                        #置标志
                        if tlist[0].lower() == "tags": 
                            last = "tags"
                            #tags在一行且存在时
                            if len(tlist[1]) > 2:
                                for v in tlist[1].split(","):
                                    self.tags.append(v.replace("\n","").strip())
                        #暂不考虑categories
                        if tlist[0].lower() == "categories": 
                             last = "categories"
                    else:
                        #tags为markdown列表形式时
                        tlist = line.split("-")
                        if len(tlist) < 3:
                            if last == "tags":
                                self.tags.append(tlist[1].replace("\n","").strip())
                            else:
                                pass
        #没有tag时放入notag类
        if len(self.tags) == 0:
            self.tags.append("notag")

if __name__ == "__main__":
    # from timeit import Timer
    # t1=Timer('md("adsl20.md")','from __main__ import md')
    # print t1.timeit(1000)
    pass

