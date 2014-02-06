title: 网站静态化
date:  2014-02-04 20:41:24
file:  wang_zhan_jing_tai_hua.md
tags: 
- Network
- python
memo: 
- ":"号与"-"号紧接着至少一个空格
- tags可以用memo的无序列表方式，也可以删除 "- notag" 行，然后用同一行的方式，多tag用","号分隔，如"tags: tag1, tag2"
- 正文与文件参数用空行分隔
- memo不算字数...file与memo也不参与文章发布。这二项目都可以在模板文件init.md中删除。
- ahui at ahui.us,2014

连续碰到几次BLOG打开卡住的情形，在VPS上重启一下nginx及php就好了。原因不详，但有可能是因为wordpress连续升级导致？

最好的解决方案就是将博客网站静态化。

试用了一下现成的解决方案，比较好用的有[hexo](http://zespia.tw/hexo/)以及[Pelican](http://docs.getpelican.com/en/3.3.0/)。
这二个都有工具能将wordpress导出的xml转化为md格式的文件。

其中hexo转化并生成静态网站后，效果相当不错。但问题是在使用时发现50+ md文件，生成时间在20s左右，这个速度太慢了一点。比较奇怪的是其他使用者都反应hexo是相当快的，所以也有可能是我这有个什么地方设置有问题。
同样的环境下Pelican的速度相当理想，同样多的md文件，生成时间3s左右。问题是他自己生成的md文件格式有点奇怪，和hexo的相比有差别，且感觉hexo的md文件格式更好点。

如果再考虑长远点，比如有海量的md文件要生成，那么就要求生成工具要么有极快的速度，要么有增量生成功能(已经生成的文件不用再生成)。这样hexo一者因为速度原因不能不放弃，二者可惜是node写的，我更偏好python一点。而pelican刚可能要修改一下格式问题，以及增加其他功能。

本着轮子不怕多的精神，干脆再做个相关工具好了。

初期目标

博客类小型网站，静态页面生成

生成方式

1. 全静态生成，所有文件需要更新。可用目录控制生成层次。
2. shtml包含，只更新必要文件
3. ajax包含，只更新必要文件

工作方式

1. cli
2. web gui

文章分类(初期只考虑tag)

1. 分类，一对一或一对多
2. tag标记，一对多

页面分类

1. index.html
2. tags.html
3. tag.html
4. comment.html
5. side_right.html
6. side_left.html
7. head.html
8. body.html ->要生成的主体文件
9. foot.html
