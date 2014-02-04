title: "[转贴]Linux Kernel Econet漏洞权限提升脚本"
id: 273
date: 2010-12-10 11:16:43
tags: 
- Linux
- Network
- ssh
categories: 
- Linux
- 网络
---

原贴出处
http://www.vpsee.com/2010/12/linux-kernel-root-level-exploit-leveraging-multiple-previous-vulnerabilities/
脚本出处
http://marc.info/?l=full-disclosure&m=129175358621826&w=2

受影响系统：
Debian Linux 5.0 x
Linux kernel 2.6.0 - 2.6.36
Linux kernel 2.6.0 - 2.6.26
Ubuntu Linux 9.10 - 10.04

已测试系统
Ubuntu 10.4 提升成功
Centos 5.5 提升失败

脚本下载
http://ahui.us/get/public/ahui/root.c.txt
已编译脚本
http://ahui.us/get/public/ahui/root.txt

Acorn Econet/AUN 协议
Econet 是一个相当老的和慢的网络协议，它主要用在Acorn电脑上，用于访问文件和打印机服务器。它使用本地的Econet 网络卡。AUN 是高层的 Econet 协议，运行于通常的以太网连接，它运行在 UDP 包协议之上，这两个协议轮流运行于IP协议上。
参考:http://en.wikipedia.org/wiki/Econet