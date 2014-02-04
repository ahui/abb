title: "UliPad自动输入括号和引号"
id: 305
date: 2011-04-12 23:05:09
tags: 
- Linux
- sofeware
categories: 
- Linux
- 网络
---

打开 ulipad/conf/python.acp文件,在
[autostring_append]
行之后加入

<pre class="brush:html">
' = "!^'"
" = '!^"'
< = "!^>"
( = "!^)"
{ = "!^}"
&lt;square> = "!^]"

</pre>