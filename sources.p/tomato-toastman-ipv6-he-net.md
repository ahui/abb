Title: Tomato Toastman完美支持he.net的IPV6
Date: 2011-06-21 17:58
Author: ahui
Category: Linux, 网络
Tags: ipv6, Linux, Network
Slug: tomato-toastman-ipv6-he-net

he.net申请到的免费IPV6地址块只用到一台机器上太浪费了,
而Toastman的Tomato修改版, 对he.net的ipv6地址块支持得相当完美了.
这样可以把申请到的地址块放在路由器上,
并自动分配IPV6地址给所有接入路由器的机器.

首先去https://www.tunnelbroker.net/申请一个64位的IPV6地址块,并记下  
Server IPv4 Address  
Server IPv6 Address  
Client IPv4 Address  
Client IPv6 Address

然后你要有一个能刷tomato的路由器,并刷上相应的Tomato Toastman版.
我用的中兴h618b对应的版本是Tomato Firmware v1.28.7820 MIPSR1-Toastman
K26 USB VPN.

login到router,进入basic-\>ipv6菜单.  
[![][]][]  
IPv6 Service Type 选择 6in4 Static Tunnel  
Assigned / Routed Prefix
填写要分配给接入机器的ipv6前缀,比如你申请到的是类x.x.x.x::1的地址,这儿填写x.x.x.x::  
Prefix Length填64  
Router IPv6 Address选择Default,会自动填写成he.net分配的Server IPv6
Address,不然选择Manual手工填写成Server IPv6 Address.  
Enable Router Advertisements勾上,  
Tunnel Remote Endpoint (IPv4 Address)填写he.net分配的Server IPv4
Address,  
Tunnel Client IPv6 Address填写he.net分配的Client IPv6 Address,64位长.

如果你好运气路由器是固定的IPV4地址,那么设置这些就ok了.保存后radvd会自动启动用于分配ipv6地址.

如果是pppoe之类拿的动态IP地址,那么这时候he.net上显示的Client IPv4
Address则会和你现在路由器地址不符.
这个时候所说的"完美"支持就表示出来了.  
进入basic-\>ddns菜单,看,下拉列表里有个"HE.net IPv6 Tunnel
Broker",贴心吧.帐号填写完后保存,这样地址改动后,会自动update
he.net上的Client IPv4 Address数据.

之后路由器给接入的机器分配IPv4地址时,会自动也分配一个IPv6地址.
这样router后面带的所有机器,都能实现IPV6接入了.

  []: http://ahui.us/wp-content/uploads/2011/06/setipipv6.png
    "setipipv6"
  [![][]]: http://ahui.us/wp-content/uploads/2011/06/setipipv6.png
