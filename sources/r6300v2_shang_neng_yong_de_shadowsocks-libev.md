title: R6300V2上能用的SHADOWSOCKS-LIBEV
date:  2014-04-16 05:07:04
file:  R6300V2_shang_neng_yong_de_SHADOWSOCKS-LIBEV.md
tags: 
- linux
- network
memo: 
- ":"号与"-"号紧接着至少一个空格
- tags英文大小写无关，可以用memo的无序列表方式，也可以删除 "- notag" 行，然后用同一行的方式，多tag用","号分隔，如"tags: tag1, tag2"
- 正文与文件参数用空行分隔
- memo不算字数...file与memo也不参与文章发布。这二项可以在模板文件init.md中删除。
- ahui at ahui.us,2014

R6300v2上安装opkg，opkg再安装python，然后运行python版本的shadowsocks成功．不过加密方式只能用table，无法正常访问google的相关服务．

一时没搞定python的m2crypto，无法启用其他加密方式，于是直接编译shadowsocks-libev，　ss-local采用命令行方式指定参数运行成功，采用aes-256-cfb加密方式，google相关网站访问正常．

移步下载 [shadowsocks-libev on R6300v2](http://pan.baidu.com/s/1bncR2CB)

Arm7系cpu应该通用，但未测试．