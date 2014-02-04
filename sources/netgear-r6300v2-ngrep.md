title: "Netgear R6300v2上编译ngrep"
id: 432
date: 2013-10-09 13:33:44
tags: 
- Linux
- Network
categories: 
- Linux
- 开发
- 游戏
---

R6300v2的dd-wrt已经[有一个版本可用](http://www.myopenrouter.com/download/50404/DD-WRT-for-R6300v2)，但可惜wifi接入还是有问题，只好换回原厂固件。打算稍修改一下原厂固件，让它能自动运行usb设备上指定目录下的脚本，这样暂时没有好用的dd-wrt的时候，可以满足现有的大部分情况。

第一步，则是要先完成能用的编译环境，并能成功编译出能在R6300v2上运行的程序。因为常用ngrep，所以第一步则以编译能用的ngrep为目标.

[R6300v2硬件参数](http://wikidevi.com/wiki/Netgear_R6300_v2)

工具链是hndtools-arm-linux-2.6.36-uclibc-4.5.3,和R6250的一样，可以下载[R6250的原代码](ftp://downloads.netgear.com/files/GPL/R6250-V1.0.0.62_with_toolchain_source.zip)，取得工具链。并顺便下载[R6300的源代码](ftp://downloads.netgear.com/files/GPL/R6300v2-V1.0.1.72_1.0.21-src.tar.zip)备用.

主系统为ubuntu 12.04 32位，创建/projects/hnd/tools/linux目录，并解压R6250源码包中的hndtools-arm-linux-2.6.36-uclibc-4.5.3.tar到此目录。

将新编译工具目录放到PATH环境的最前面:
```bash
export PATH=/projects/hnd/tools/linux/hndtools-arm-linux-2.6.36-uclibc-4.5.3/bin:$PATH
```

下载libpcap-1.4.0.tar.gz及ngrep-1.45.tar并解压。

编译libpcap: 
```bash
./configure CC=arm-uclibc-linux-2.6.36-gcc --host=arm-linux --with-pcap=linux && make
```
编译ngrep: 
```bash
./configure CC=arm-uclibc-linux-2.6.36-gcc CXX=arm-uclibc-linux-2.6.36-g++ AR=arm-uclibc-linux-2.6.36-ar RANLIB=arm-uclibc-linux-2.6.36-ranlib LD=arm-uclibc-linux-2.6.36-ld  --prefix=/usr/local/arm/ngrep --host=arm-linux --build=arm --with-pcap-includes=../libpcap-1.4.0 && make
```

检查编译出来的文件:
```bash
file ngrep
ngrep: ELF 32-bit LSB executable, ARM, version 1 (SYSV), dynamically linked (uses shared libs), stripped
```

开启R6300v2的telnet(R6300v2 ip为192.168.1.1)
下载[telnetenable.py](https://code.google.com/p/netgear-telnetenable/)
```bash
python telnetenable.py 192.168.1.1 $(arp -n | awk "/192.168.1.1/"'  { gsub(/:/, "", $3); print toupper($3)}') Gearguy Geardog
```
出现"Sent telnet enable payload to '192.168.1.1:23'"则成功，否则多运行几次.

将ngrep copy到u盘，并在R6300上挂载，然后telnet到R6300v2,到/tmp/mnt/usb0/part1下找到ngrep并运行之。
```bash
./ngrep -V
ngrep: V1.45, $Revision: 1.93 $
```