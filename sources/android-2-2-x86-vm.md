title: "Android 2.2 x86虚拟机版编译记录"
id: 198
date: 2010-08-06 20:50:59
tags: 
- Linux
- Network
categories: 
- Linux
- 网络
---

Android x86项目提供的还是1.6版本的iso,[这里](http://cwhuang.info/)做了很多的最新版本2.2的工作,可以由他上传的源码编译一个Virutal Box能使用的vm.iso文件.

编译主机用的Ubuntu 10.04,其他OS可能要安装的相关依赖文件有所不同.
10.04默认没有sun jdk,要加个新源 

    http://archive.canonical.com/ lucid partner.

1.安装相关依赖文件

    sudo add-apt-repository "deb http://archive.canonical.com/ lucid partner"
    sudo apt-get update
    sudo apt-get install git-core 
    sudo apt-get install sun-java6-jdk 
    sudo apt-get install flex 
    sudo apt-get install bison 
    sudo apt-get install gperf
    sudo apt-get install libsdl-dev
    sudo apt-get install libwxgtk2.6-dev 
    sudo apt-get install build-essential 
    sudo apt-get install curl 
    sudo apt-get install valgrind


2.安装repo

    cd
    mkdir bin
    cd bin
    curl http://android.git.kernel.org/repo > ~/bin/repo
    chmod a+x repo

3.下载同步源代码

    cd
    mkdir android2.2
    cd android2.2
     ../bin/repo init -u git://android-x86.git.sf.net/gitroot/android-x86/manifest.git -b froyo-x86
     ../bin/repo sync

同步要花n久时间.取决于网速,我这200+KB/s跑了四个多小时.

4.编译成vm.iso  其中编译参数-j4是我有四个cpu核心,所以设定同时运行4个进程.

     . build/envsetup.sh
    lunch vm-eng 
    m -j4 iso_img  ' cpu x 4

编译也要花n久时间,取决于CPU性能,我的Xeon 4核心花了近三个小时.
然后你就能在out下找到vm.iso了.文件大小约557,714KB.
新开一个Virtual Box虚拟机,挂载vm.iso,直接光盘运行或安装到硬盘都可.鼠标独占要去掉,否则不会显示鼠标.而且鼠标的速度慢了点,得等作者在新版本里进行修正了.

ISO文件已经上传到网盘,[点此查看](http://ahui.us/?p=234).

无图无真相,给几张在我的VB中运行的靓照.多图杀猫啊~ 点击查看清晰无码大图.

[gallery link="file" columns="2" orderby="title"]

-----END-----