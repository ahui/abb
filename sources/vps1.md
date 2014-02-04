title: "PS1值保存待用"
id: 156
date: 2010-07-26 23:45:53
tags: 
- Linux
- Network
categories: 
- Linux
- 网络
---

常用的bash PS1值
<pre class="brush:plain">
PS1="\[\033[35m\]\t\[\033[m\] \[\033[36m\]\u\[\033[m\]@\[\033[32m\]\h:\[\033[33;1m\]\w\[\033[m\] ->"
</pre>
效果如下
[![](http://ahui.us/wp-content/uploads/2010/07/ps1.bmp "ps1")](http://ahui.us/wp-content/uploads/2010/07/ps1.bmp)

or
<pre class="brush:plain">
PS1="\[\033[37m\]\t\[\033[m\] \[\033[36m\]\u\[\033[m\]@\[\033[32m\]\h:\[\033[33;1m\]\w\[\033[m\]>"
</pre>