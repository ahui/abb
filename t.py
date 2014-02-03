#!/usr/bin/python
# coding=utf-8

import sys
import markdown
import codecs
import misaka as m

reload(sys)
sys.setdefaultencoding('utf-8')   
#print sys.getdefaultencoding()
with open('adsl20.md','r') as fp:
    var = fp.read()
    #print var

html = markdown.markdown(var)
#html = m.html(var)
print html

