#!/usr/bin/python
# coding=utf-8
# Ahui at ahui.us,2014

from mdreader import *
import tenjin
from tenjin.helpers import *
import misaka as m
import os
from operator import itemgetter

engine = tenjin.Engine(path=['themes/default'], layout='')
tenjin.set_template_encoding('utf-8')

content={}                  #传送给模板的参数
posts = {}                  #保存post信息，以时间为key
inputdir = "sources"        #md文件目录
outputdir = "public"        #静态文件输出目录
inputfn = "adsl20.1.md"     #post的md格式文件名
theme = "default"           #主题
tags = {}                   #保存所有tag,格式为tag:tag内文章数目
files = {}                  #保存所有预处理后的文件信息


def sortdict(d,reverse=True):
    return sorted(d.iteritems(), key=itemgetter(0), reverse=reverse)

def render_post(newmd):
    content={}
    content["title"] = newmd.title
    content["date"] = newmd.date
    content["tags"] = newmd.tags
    content["body"] = m.html(newmd.body)

    for tag in newmd.tags:
        if tag in tags:
            tags[tag] = tags[tag] + 1
        else:
            tags[tag] = 1

    outputfile = "%s/post/%s.html" % (outputdir,inputfn[0:-3])
    posts[newmd.date] = {"title":newmd.title,"url":"%s.html" % inputfn[0:-3],"tags":newmd.tags}
    files[outputfile] = content

def write_post():
    #检查目录是否存在
    if not os.path.exists(outputdir):
        os.mkdir(outputdir)
    if not os.path.exists("%s/post" % outputdir):
        os.mkdir("%s/post" % outputdir)

    for post in files:
        with open(post,"w") as fp:
            fp.write(engine.render("post.html",files[post]))

def render_rightside():
    content = {}
    content["tags"] = tags
    #最近文章，取前5条. 排序后为list
    content["posts"] = sortdict(posts)[0:5]
    with open("themes/default/sidebar.html","w") as fp:
        fp.write(engine.render("rightbar.html",content))

def render_tags():
    tagdir = "%s/tag" % outputdir
    if not os.path.exists(tagdir):
        os.mkdir(tagdir)
    taglist = {}
    #存在的问题: 二次调用排序
    for post in sortdict(posts):
        for tag in post[1]["tags"]:
            if tag not in taglist:taglist[tag]=[]
            taglist[tag].append({"url":post[1]["url"],"title":post[1]["title"],"date":post[0]})
    for tag in taglist:
        content = {}
        content["posts"] = taglist[tag]
        content["title"] = "标签 %s 所有文章列表" % tag
        with open("%s/%s.html" % (tagdir,tag),"w") as fp:
            fp.write(engine.render("tag.html",content))

    
def write_tag(tag):
    pass

def render_index():
    pass

#预处理文章
for inputfn in os.listdir(inputdir):
    #print inputfn
    fullpath = "%s/%s" % (inputdir,inputfn)
    if os.path.isfile(fullpath):
        #print inputfn
        newmd = md(fullpath)
        render_post(newmd)

#生成右侧
render_rightside()
#生成并写入文章
write_post()

#生成tags列表
render_tags()

#生成index
render_index()

#print posts
#所在全局变量
pass