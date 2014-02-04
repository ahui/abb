title: "ArchLinux在Eeepc 701上的安装"
id: 253
date: 2010-09-09 14:54:14
tags: 
- Linux
- Network
categories: 
- Linux
- 网络
---

1.下载archlinux-2010.05-core-i686.iso
2.安装grub4dos到u盘
3.copy archlinux-2010.05-core-i686.iso到u盘.编辑menu.lst,加入
title Arch CD ISO
map --heads=0 --sectors-per-track=0 (hd0,0)/archlinux-2010.05-core-i686.iso (hd32)
map --hook
chainloader (hd32)
boot
4.epc设置u盘启动
5.没有找到安装源,自动跳出shell时运行
mkdir /iso
mount –r –t vfat /dev/sdb1 /iso
modprobe loop
losetup /dev/loop6 /iso/archlinux-2010.05-core-i686.iso
ln –s /dev/loop6 /dev/disk/by-label/ARCH_201005
exit
6.继续安装,分区时,ssd 4g为ext2格式,全部mount到/,无swap
7.编辑配置文件,fstab中,mount /时加入noatiome参数
8.编辑配置文件,hosts.deny修改为ALL: ALL EXCEPT 192.168.2.*: DENY
9.编辑配置文件,rc.local,禁用syslog-ng及netfs
10.编辑配置文件,pacman.conf加入
[eee]
Server = http://code.toofishes.net/packages/eee
11.安装完成后.重启
12.编辑配置文件/etc/pacman.d/mirrorlist,加入
Server = http://mirrors.163.com/archlinux/$repo/os/i686
13.pacman 安装openssh
14.编辑rc.local,启动sshd,编辑hosts.allow,加入
sshd:192.168.2.*:ALLOW
15.wget http://www.ihku.biz/eee/acpi-eee/acpi-eee-10.0-1-i686.pkg.tar.gz
pacman -U acpi-eee-10.0-1-i686.pkg.tar.gz
根据提示修改二处配置
16\. pacman -S kernel-eee
17.编辑/boot/grub/menu.lst,加入后重启动
# (2) Arch Linux
title  Arch Linux Eee kernel
root   (hd0,0)
kernel /boot/vmlinuzeee root=/dev/sda1 ro