abb
===

abb=ahui blog builder  
abb是个静态博客生成工具，类似hexo

##主程序

    abb.py

##可接受的参数列表:

    init            :初始化当前目录
    help            :显示帮助
    addpost 标题    :添加新文章(标题可以有空格)
    build           :生成整个站点
    version         :查看版本

##依赖的外部模块
    misaka
    tenjin

同步静态文件[参见此处](http://ahui.us/post/yong_git_tong_bu_jing_tai_wang_zhan.html)。

##示例站点
    [http://ahui.us](http://ahui.us)

##使用方法:

1. 使用 ./abb iniit 初始化当前目录，这会删除示例文件.
2. 使用 ./abb addpost 标题 产生新的文章.
3. 产生更多的文章.
4. 编辑产生的md文件，加入内容及格式(markdown).
5. 使用 ./build 生成站点.
6. 使用 ./sync 同步站点.