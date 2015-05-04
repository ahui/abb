title: p2p vpn 之 n2n 安装使用
date:  2015-01-20 04:59:05
file:  p2pvpn_zhi_n2n_an_zhuang_shi_yong.md
tags: 
- linux
- vpn
- network
memo: 
- ":"号与"-"号紧接着至少一个空格
- tags英文大小写无关，可以用memo的无序列表方式，也可以删除 "- notag" 行，然后用同一行的方式，多tag用","号分隔，如"tags: tag1, tag2"
- 正文与文件参数用空行分隔
- memo不算字数...file与memo也不参与文章发布。这二项可以在模板文件init.md中删除。
- ahui at ahui.us,2014

n2n 是点对点类型的 vpn, 轻量级,容易安装与配置. 

[官方网站在这里](http://www.ntop.org/products/n2n/)

在安装使用中,还是碰到几个小坑,记录下来. 另外其版本有 v1,v2二个,这里都使用 v2版本. 其用法二个版本都一样,但不同版本通信协议不兼容, 所以所有节点都要使用相同的版本.

#使用场景

边缘节点有三个

- zte h610b 路由器,安装 tomato, 无公网 ip
- RMBP 工作用电脑,安装 mac os, 内部 ip
- hk vps 一台,安装 ubuntu,有 固定公网 ip,地址为 a.b.c.d

超级节点一个,也就是上面有 ip 的 vps.

#安装记录

##hk vps
ubuntu 上安装最简单. 但 apt-get install n2n 是 v1的版本.我这里要用 v2,自己编译下.


    sudo apt-get install subversion build-essential libssl-dev
    svn co https://svn.ntop.org/svn/ntop/trunk/n2n
    cd n2n/n2n_v2
    make

然后就能生成需要的二个文件,超级节点守护程序`supernode`及边缘节点通信程序`edge`.
安装libssl-dev 有时候会进坑,报错说已经安装的 ssl 版本太新. 修复方式是在/etc/apt 源里,添加对应的 updates 源,更新后再安装.
如:

	deb http://mirrors.aliyun.com/ubuntu/ trusty-updates main restricted
	deb-src http://mirrors.aliyun.com/ubuntu/ trusty-updates main restricted

首先启动超级节点,监听端口999

	sudo ./supernode -l 999

然后本机也做为边缘节点启动

	sudo ./edge -d n2n0 -a 10.1.1.10 -c ahuin2nvpn -u nobody -g nobody -k ahuin2nvpn -l a.b.c.d:999 -m ae:e0:4f:e7:47:1a

其中一个小坑就是 -m 参数. 如果不指定,会产生一个随机 mac 地址,这样至少调试的时候多次运行,会出现 mac 混乱. 但指定的 mac  地址,有些不会识别,比如随便写个 ab:ab:ab:ab:ab:ab, 程序不会识别并自动产生一个新的随机 mac. 跳坑方法是找个真实的 mac 地址,然后改动最后二位.

##zte h610b 路由器

这个真的没有真 ip,用的移动光纤,给了个看上去象真的,其实是假的 ip.

tomato 有人做好了现成的版本, 打开 jffs 并挂载,然后把编译好的 n2n 放在/jffs/n2n 中. 备注:我用的地址1上的版本.

[下载地址1](http://right.com.cn/forum/thread-72025-1-1.html) 以及 [下载地址2](http://tomato.groov.pl/repo/n2n_r5895-1_mipsel.ipk)

加载一下 tun 设备
	
	modprobe tun
	
运行很简单

	./edge -d n2n0 -a 10.1.1.20 -c ahuin2nvpn -u nobody -g nobody -k ahuin2nvpn -l a.b.c.d:999 -m ae:e0:4f:e7:47:2a

运行后,ping 10.1.1.10能通,反之不行.

设置 iptables

	iptables -I OUTPUT -o n2n0 -j ACCEPT
	iptables -I INPUT -i n2n0 -j ACCEPT
	iptables -I FORWARD -o n2n0 -j ACCEPT
	iptables -I FORWARD -i n2n0 -j ACCEPT

ok,现在能与10.1.1.10互相 ping 通. 此时二台机器可以认为在同一个局域网.

##RMBP 工作用电脑

mac 上坑最多. 前提之一开发环境已经就绪,git svn 都 ok. 我这里用 git

首先安装 tuntap, [在这里下载](http://tuntaposx.sourceforge.net/)

下载源代码并编译:

	git clone git://github.com/certik/n2n.git
	cd n2n/n2n_v1
	make

出错啦,编译失败. 有好人做了[补丁](https://gist.github.com/tevino/9798566), 打完后再 make, 通过. 

或者手动修改, 删除void tun_close(tuntap_dev *device); 这行,并将tun_close(device);替换为tuntap_close(device);,改动这二处就 ok.

mac 下会自动生成 tun 设备 tap0, 所以运行时不用指定-d 参数:

	./edge -a 10.1.1.30 -c ahuin2nvpn -u nobody -g nobody -k ahuin2nvpn -l a.b.c.d:999 -m ae:e0:4f:e7:47:3a

大功告成,现在10.1.1.10, 10.1.1.20, 10.1.1.30三个节点都能互相 ping 通, 并互相访问所有端口,就象在同一个局域网里面.

#问题

理论上超级节点并不参与数据转发, 不过我测试的时候,ping 包至少是转发了的, 估计是与边缘结点没有公共 ip 有关. 其他流量没测试.

n2n 是点对点的, 如果想要把边缘结点后面的局域网也连起来, 应该能 通过在节点上通过手动指定路由并做 nat来实现, 当然这样配置起来就麻烦多了.

n2n 的最佳应用,应该是通过外网访问内网,特别是内网没有公共 ip 的时候,比如移动光纤...

要通过 n2n 访问一些不存在的网站,要做额外工作,可能 openvpn 更适合. 



