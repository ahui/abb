Title: Ubuntu on Virtual Box VDI 复制后丢失网卡
Date: 2013-05-11 11:46
Author: ahui
Category: Linux, 网络
Tags: Linux, Network
Slug: vdi-file-lost-network

A机，VB安装Ubuntu 12.10
Server,网卡模式为桥接。此时Ubuntu中网卡为eth0，DHCP,
连接正常。复制硬盘VDI文件至B机。  

B机，VB安装完成后，新建立linux类虚拟机，并使用复制过来的Ａ机VDI文件启动，此时DHP无法取得ＩＰ，并且不能手工ifconfig
eth0 up，查看发现eth0不存在，网卡设备转为eth1.估计网卡mac有变动.  
解决：修改/etc/network/interface,将其中二行eth0相关配置，修改成eth1
