#!/usr/bin/python
# coding=utf-8

#将指定目录下的文件名改为小写字母

import os


s_dir	=	'../sources'

for fn	in os.listdir(s_dir):
	n_fn = fn.lower()
	os.rename(os.path.join(s_dir,fn), os.path.join(s_dir,n_fn))
	print "changed filename from '%s' to '%s'" % (fn,n_fn)

