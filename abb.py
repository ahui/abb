#!/usr/bin/python
# coding=utf-8
# 静态博客生成器 by ahui
# Ahui at ahui.us,2014
# 修改或发布时请保留以上声明

__version__ = '0.2'

from tools.mdreader import *
import tenjin
from tenjin.helpers import *
import misaka as m
import os
from operator import itemgetter
import config
import time
import shutil

inputdir = config.path["input"]         #md文件目录
outputdir = config.path["output"]       #静态文件输出目录
theme = config.theme["name"]            #主题

content={}                              #传送给模板的参数
posts = {}                              #保存post信息，以时间为key
tags = {}                               #保存所有tag,格式为tag:tag内文章数目
files = {}                              #保存所有预处理后的文件信息



engine = tenjin.Engine(path=['themes/%s' % theme], layout='base.html')
tenjin.set_template_encoding('utf-8')

def sortdict(d,reverse=True):
    return sorted(d.iteritems(), key=itemgetter(0), reverse=reverse)

def render_post(mdfile):
    newmd = md("%s/%s" % (inputdir,mdfile))
    outputfile = "%s.html" % (mdfile[0:-3])

    content={}
    content["title"] = newmd.title
    content["date"] = newmd.date
    content["tags"] = newmd.tags
    content["dir"] = "../"
    content["sidebar"] = "_sidebar.html"
    content["mode"] = "post"
    content["url"] = outputfile
    content["blog"] = config.blog
    content["body"] = m.html(newmd.body)

    for tag in newmd.tags:
        if tag in tags:
            tags[tag] = tags[tag] + 1
        else:
            tags[tag] = 1

    
    posts[newmd.date] = {"title":newmd.title,"url":outputfile,"tags":newmd.tags}
    files[outputfile] = content

def write_post(postdir="default"):
    if postdir == "default":
        #检查目录是否存在
        if not os.path.exists(outputdir):
            os.mkdir(outputdir)
        if not os.path.exists("%s/post" % outputdir):
            os.mkdir("%s/post" % outputdir)
        postdir = "%s/post" % outputdir
    else:
        postdir = "."
    i = 0
    for post in files:
        i = i + 1
        with open("%s/%s" % (postdir,post),"w") as fp:
            fp.write(engine.render("post.html",files[post]))
    print "总共生成 %s 篇文章." % i

def render_rightside(dirprefix="../"):
    content = {}
    content["tags"] = tags
    content["dir"] = dirprefix
    content["blog"] = config.blog
    if dirprefix == "":
        sidebar = "_sidebar_index.html"
    else:
        sidebar = "_sidebar.html"
    #最近文章，取前5条. 排序后为list
    content["posts"] = sortdict(posts)[0:10]
    with open("themes/%s/%s" % (theme,sidebar),"w") as fp:
        fp.write(engine.render("rightbar.html",content,layout=""))

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
        content["dir"] = "../"
        content["sidebar"] = "_sidebar.html"
        content["posts"] = taglist[tag]
        content["blog"] = config.blog
        content["title"] = "标签 %s 所有文章列表" % tag
        with open("%s/%s.html" % (tagdir,tag),"w") as fp:
            fp.write(engine.render("tag.html",content))

    
def render_index():
    sortpost = sortdict(posts)
    postcount = 8                           #每页文章数
    pages = len(sortpost) / postcount       #总页数
    if (len(sortpost) % postcount)  > 0 :   #修正
        pages = pages + 1
    for p in xrange(pages):
        #最后一页取余数
        if p == pages -1 :
            if (len(sortpost) % postcount)  > 0 :
                postcount = (len(sortpost) % postcount)
        tmpbody = ""
        for i in xrange(postcount):
            content = {}
            #当前post指针
            postid = p * 8 + i
            content["title"] = sortpost[postid][1]["title"]
            content["tags"] = sortpost[postid][1]["tags"]
            content["url"] = sortpost[postid][1]["url"]
            content["dir"] = ""
            content["mode"] = "index"
            content["date"] = sortpost[postid][0]
            content["body"] = files[content["url"]]["body"]
            tmpbody = tmpbody + engine.render("post.html",content,layout="")
        #生成一页
        content ={}
        content["dir"] = ""
        content["sidebar"] = "_sidebar_index.html"
        content["title"] = "Ahui的个人博客"
        content["page"] = p
        content["pages"] = pages
        content["body"] = tmpbody
        content["blog"] = config.blog
        if p == 0:
            outputfile = "index.html"
        else:
            outputfile = "index.%s.html" % p
        with open("%s/%s" % (outputdir,outputfile),"w") as fp:
            fp.write(engine.render("index.html",content))

def getallhtml():
    #预处理文章
    for inputfn in os.listdir(inputdir):
        fullpath = "%s/%s" % (inputdir,inputfn)
        if os.path.isfile(fullpath):
            render_post(inputfn)

    #生成右侧
    render_rightside()
    #生成并写入文章
    write_post()

    #生成tags列表
    render_tags()

    #生成index要用的rightside
    render_rightside("")

    #生成index
    render_index()

    #copy theme 下的静态文件目录,如 css,img,js 等
    for static in config.theme["static"]:
        if not os.path.exists("%s/%s" % (outputdir, static)):
            shutil.copytree("themes/%s/%s" % (theme, static),"%s/%s" % (outputdir, static))


def gethtml(mdfile):
    render_post(mdfile)
    write_post()


def addpost(title):
    import tools.pinyin
    py = tools.pinyin.PinYin()
    mdfilename = " ".join(title)
    content["title"] = mdfilename
    mdfilename = "%s.md" % py.hanzi2pinyin_split(mdfilename,"_")
    #检查重复文件名,存在则添加数字后缀
    i = 0
    tmpfilename = mdfilename
    while 1:
        i = i + 1
        if os.path.exists("%s/%s" % (inputdir,tmpfilename)):
            tmpfilename = "%s_%s" % (i,mdfilename)
        else:
            break
    #文件名全部用小写字母
    mdfilename = tmpfilename.lower()
    engine = tenjin.Engine(path=[''], layout='')
    from datetime import datetime
    dt = datetime.now()
    content["date"] = dt.strftime('%Y-%m-%d %I:%M:%S')
    content["filename"] = mdfilename
    with open("%s/%s" % (inputdir,mdfilename),"w") as fp:
        fp.write(engine.render("init.md",content))

    print "文章%s模板已经生成，是否进入编辑? ([y]es or [n]o)" % mdfilename
    answer = raw_input()
    if answer.lower() in ("y","yes"):

        cmd = "%s %s/%s" % (config.editor,inputdir,mdfilename)
        os.system(cmd)

    sys.exit()

def printhelp():
    helpmsg = """
    可接受的参数列表:

        init            :初始化当前目录
        help            :显示帮助
        addpost 标题    :添加新文章(标题可以有空格)
        build           :生成整个站点
        html            :生成单个页面
        version         :查看版本
    """
    print helpmsg


if __name__ == "__main__":
    if len(sys.argv) == 1:
        #inputdir不存在时退出
        if not os.path.exists(inputdir):
            print "目录不正确。请输入init参数初始化。"
            sys.exit()
        printhelp()
        sys.exit()
    else:
        case = sys.argv[1]
    if case == "init":
        #生成source及public目录并copy theme文件
        pass
    elif case == "build":
        time_s = time.time()
        getallhtml()
        time_e = time.time()
        print "总共花费时间: %f 秒." % (time_e - time_s)
        sys.exit()
    elif case == "help":
        printhelp()
        sys.exit()
    elif case == "version":
        print "当前版本:%s,By Ahui at ahui.us" % __version__
        sys.exit()
    elif case == "html":
        if len(sys.argv) == 2:
            print "请输入md文件名."
            sys.exit()
        mdfile = sys.argv[2]
        if not os.path.exists("%s/%s" % (inputdir,mdfile)):
            print "md文件 %s 不存在。请输入正确的文件名。" % sys.argv[2]
            sys.exit()
        gethtml(mdfile)
    elif case == "addpost":
        if len(sys.argv) == 2:
            print "请输入文章标题."
            sys.exit()
        addpost(sys.argv[2:])
    else:
        printhelp()