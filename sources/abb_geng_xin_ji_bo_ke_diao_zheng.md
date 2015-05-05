title: ABB 更新及博客调整
date:  2015-05-05 12:02:26
file:  abb_geng_xin_ji_bo_ke_diao_zheng.md
tags: 
- python
- blog
memo: 
- ":"号与"-"号紧接着至少一个空格
- tags英文大小写无关，可以用memo的无序列表方式，也可以删除 "- notag" 行，然后用同一行的方式，多tag用","号分隔，如"tags: tag1, tag2"
- 正文与文件参数用空行分隔
- memo不算字数...file与memo也不参与文章发布。这二项可以在模板文件init.md中删除。
- ahui at ahui.us,2014

ABB(Ahui Blog Build)断断续续自己一个人在用着, 基本上没太大问题. 为方便生成另外的站点,做了些调整.

- config.py 中设置新站点参数,模板调整为通用,从 config中取得站点信息.
- 生成的 html 文件名,全部用小写.
- 模板加入 goto.html 文件,用于跳转以前的老旧页面到首页.
- 模板中加入网站统计变量,统计代码可在 config.py 中设置.
- 生成整站时,输出相关信息.
- github 地址为 https://github.com/ahui/abb

其中 goto.html 主要用于自己博客. 因为最早用 wordpress, 后来的 abb 又生成过大小写敏感的 html,导致搜索过来的页面地址有差异. 而生成整站静态 html 时,为了能本地查看,均使用了相对地址, 这样 nginx 的 try_file 重定向的首页,会导致 css,js 无法正常取得,最简便的方法是定向到 goto.html,然后用 JS 重定向到首页.

另外 duosuo 评论,偶尔会导致加载时间达10秒,暂时在模板中去除. 

ABB 程序与 [GITHUB](https://github.com/ahui/abb) 同步.

最近一次生成信息:
./abb.py build
总共生成 68 篇文章.
总共花费时间: 0.098921 秒.

生成性能大约为每秒700篇文章,硬件为 RMBP 15, CPU i7.