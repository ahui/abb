title: 用addpost生成的第一篇静态Blog
date:  2014-02-06 03:58:17
file:  yong_addpost_sheng_cheng_de_di_yi_pian_jing_tai_Blog.md
tags: 
- blog
- python
memo: 
- ":"号与"-"号紧接着至少一个空格
- tags可以用memo的无序列表方式，也可以删除 "- notag" 行，然后用同一行的方式，多tag用","号分隔，如"tags: tag1, tag2"
- 正文与文件参数用空行分隔
- memo不算字数...file与memo也不参与文章发布。这二项目都可以在模板文件init.md中删除。
- ahui at ahui.us,2014

静态网站生成程序上站测试。
ohoh,还没取名字...

已完成功能:

-  cli生成post模板
- 根据md文件生成对应的html文件
- 根据目录生成整站html文件
- 生成首页面index.html
- 首页下部生成页码导航
- 生成tag目录
- 生成最新文章列表
- 包含多说的ajax评论
- 除多说的ajax评论不支持file://,其他页面均能用file://方式浏览.
- 用Contango Theme做了一个默认模板。

wordpress转移方式

1.  在wordpress中导入所有post到xml文件中
2. hexo Pelican 二者都有对应工具，从xml中提取所有post为对应的.md格式文件。建议用hexo的工具，转换得更好一点。本程序支持这二者转换后的格式。
3. md格式修正。主要是换行，代码块等，多加点空行。
5. 生成全站静态html。

运行环境(Ubuntu on Virtualbox)

uname -a

    Linux openerp7 3.5.0-17-generic #28-Ubuntu SMP Tue Oct 9 19:32:08 UTC 2012 i686 i686 i686 GNU/Linux

cat /proc/cpuinfo

    ...
    processor       : 3
    vendor_id       : GenuineIntel
    cpu family      : 6
    model           : 58
    model name      : Intel(R) Core(TM) i5-3210M CPU @ 2.50GHz
    stepping        : 9
    cpu MHz         : 2394.400
    bogomips        : 4788.80


生成速度

     ls ./sources | wc
         59      59    1206

     time ./main.py build

    real    0m0.390s
    user    0m0.092s
    sys     0m0.120s

如果按照这个速度不变，生成一万篇文章需时一分钟多点。
