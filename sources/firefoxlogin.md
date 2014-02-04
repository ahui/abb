title: "Firefox有时候不能正常登录论坛"
id: 183
date: 2010-08-03 00:56:29
tags: 
- Network
categories: 
- 网络
---

新安装了个中文版的firefox,已经更新到3.6.8,发现有个常去的论坛死活登录不上去,IE没有问题,以前一直用的英文版ff也ok,于是怀疑是中文版的cookies的问题,找到

C:\Users\ahui\AppData\Roaming\Mozilla\Firefox\Profiles\XXXX.default\cookies.sqlite

用sqlite管理软件查看内容,发现没有保存刚登录的论坛的记录.
尝试将cookies.sqlite改名,重新登录,问题解决.
原因不明.特记之.