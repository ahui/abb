title: owncloud mac os 客户端乱码
date:  2015-01-17 05:17:59
file:  owncloudmacos_ke_hu_duan_luan_ma.md
tags: 
- mac
- network
memo: 
- ":"号与"-"号紧接着至少一个空格
- tags英文大小写无关，可以用memo的无序列表方式，也可以删除 "- notag" 行，然后用同一行的方式，多tag用","号分隔，如"tags: tag1, tag2"
- 正文与文件参数用空行分隔
- memo不算字数...file与memo也不参与文章发布。这二项可以在模板文件init.md中删除。
- ahui at ahui.us,2014

owncloud mac ox client 安装后,首次设置以及运行后的设置界面, 中文显示为方框. 最简单的解决方法删除自带的翻译文件,强制使用英文显示.

进入

/Volumes/Macintosh HD/Applications/owncloud.app/Contents/Resources/Translations

删除或改名这二个文件:

- mirall_zh_CN.qm
- qt_zh_CN.qm

然后退出owncloud,再运行就是英文界面了.

windows 下应该类似, 但没验证.