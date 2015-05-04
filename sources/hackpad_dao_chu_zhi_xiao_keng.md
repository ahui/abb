title: HACKPAD导出之小坑
date:  2014-09-23 05:07:35
file:  HACKPAD_dao_chu_zhi_xiao_keng.md
tags: 
- blog
- network
memo: 
- ":"号与"-"号紧接着至少一个空格
- tags英文大小写无关，可以用memo的无序列表方式，也可以删除 "- notag" 行，然后用同一行的方式，多tag用","号分隔，如"tags: tag1, tag2"
- 正文与文件参数用空行分隔
- memo不算字数...file与memo也不参与文章发布。这二项可以在模板文件init.md中删除。
- ahui at ahui.us,2014

hackpad.com编辑时，基本可以看做是在写md,而且是即时生成html效果(非分屏)，手感相当好，特别是表格和代码块。

不过在导出md格式时，文章标题不能有中文，否则这篇文章无法导出。

根据导出的md文件来着，文章标题实际上是第一级标题#，这也是一个小坑，这样hackpad里只能有一个#并且被文章标题占用，文章内容最高级标题只能是第二级标题##.