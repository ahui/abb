Title: UliPad自动输入括号和引号
Date: 2011-04-12 23:05
Author: ahui
Category: Linux, 网络
Tags: Linux, sofeware
Slug: ulipadautoinput

打开 ulipad/conf/python.acp文件,在  
[autostring\_append]  
行之后加入

~~~~ {.brush:html}
' = "!^'"
" = '!^"'
< = "!^>"
( = "!^)"
{ = "!^}"
<square> = "!^]"
~~~~
