Title: Openvz VPS的IPV6地址添加
Date: 2010-11-05 12:54
Author: ahui
Category: Linux, 网络
Tags: ipv6, Linux, Network, VPS
Slug: openvz-vps-ipv6-add

burstnet的openvz vps提供了二个源生的ipv6地址,MASK是128位的.  

新的vps也是openvz,不过没有源生ipv6.但可以申请he.net的ipv6块,然后添加到vps上.  
首先要开通openvz的tun支持,确认  
cat /dev/net/tun  
返回值为:  
cat: /dev/net/tun: File descriptor in bad state  

访问https://www.tunnelbroker.net,申请地址块,会拿到一个MASK为64位的地址.还真是浪费啊,要都这么分下去,ipv6的理论地址一下就少了一半.  
记下Server IPv4 address,Client IPv4 address以及Client IPv6
address.前面的地址可选择离vps近的机房,中间地址是vps
ip.最后一个是分配给你的2的64次方的地址中的第一个地址.按he的分配规则,是类似x:x:x:x::1/64的地址块.前64位已经固定,后64位全部给你自己分配,但x:x:x:x::1/128分配给了服务器做中转,你能用到的第一个ipv6地址,应该是x:x:x:x::2/128.当然用64的mask也可以.  
openvz没有sit设备,用软件模拟  
mkdir tb  
cd tb  
wget http://tb-tun.googlecode.com/files/tb-tun\_r18.tar.gz  
tar zxf tb-tun\_r18.tar.gz  
gcc tb\_userspace.c -l pthread -o tb\_userspace  
setsid ./tb\_userspace tb [Server IPv4 address] [Client IPv4 address]
sit \> /dev/null  
成功创建tb设备后,启用ipv6  
ifconfig tb up  
ifconfig tb inet6 add x:x:x:x::2/64  
ifconfig tb mtu 1480  
ip -6 route add default dev tb  
看看设置:  
ifconfig tb  
tb Link encap:UNSPEC HWaddr
00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00  
inet6 addr: x:x:x:x::2/64 Scope:Global  
UP POINTOPOINT RUNNING NOARP MULTICAST MTU:1480 Metric:1  
RX packets:200 errors:0 dropped:0 overruns:0 frame:0  
TX packets:181 errors:0 dropped:0 overruns:0 carrier:0  
collisions:0 txqueuelen:500  
RX bytes:28387 (27.7 KiB) TX bytes:21990 (21.4 KiB)  
总的来说,这ipv6地址用得真的很浪费,虽然我已经申请了三块64位的地址....
