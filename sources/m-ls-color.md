title: "修改ls --color的颜色"
id: 281
date: 2010-12-20 12:55:44
tags: 
- Linux
- Network
categories: 
- Linux
- 网络
---

ls --color默认目录颜色是深蓝，在黑色背景下，看得很纠结．换成浅蓝就好多了．
centos下， vi /etc/DIR_COLORS
将
DIR 01;34       # directory
这行修改为
DIR 00;36       # directory
然后vi .bashrc
加上
export LS_OPTIONS='-aCF --color=auto'
eval "`dircolors -b /etc/DIR_COLORS`"
alias ls='ls $LS_OPTIONS'
顺便加上PS1
PS1="\[\033[37m\]\t\[\033[m\] \[\033[36m\]\u\[\033[m\]@\[\033[32m\]\h:\[\033[33;1m\]\w\[\033[m\]>"
执行. .bashrc生效