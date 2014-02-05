Title: Tomato Toastman 之 SIP Server : siproxd 安装与使用
Date: 2011-06-21 16:23
Author: ahui
Category: Linux, 网络
Tags: Linux, Network, sip
Slug: tomato-firmware-v1-28-7820-mipsr1-toastman-k26-usb-vpn

原本使用的SIP Server是sip ser,后来改用kamailio.
二者的配置和使用都基本一样.
kamailio放在VPS上,程序本身相当稳定,但随着通话时间的增长,随机在5到10分钟后,会因为一些已知或未知的原因,通话质量迅速下降.
挂掉重拨后能且只正常一小会儿,然后又必须重拨, 很是烦人.

后来把sip流量放在vpn里,情况好了很多.
至少不会因为莫名的干扰导致通话质量下降.
不过这样一来,sip流量必须通过vps进行中转,
而出国线路每天会不定期的抽风随机的一段时间......全国LAN网时代大概不远了吧?

暂时方案,把sip
server放在家里的router上,然后再挂上vpn,这样二方通话就能直接走国内线路vpn里.
虽然我也曾发现国内有时候也丢包15%\~30%,但总比去VPS丢50%+要好.
而且国内线路抽风的时候要少些, 因为大多数G点都不在国内.

翻出落了不少灰尘的中兴h618,吹吹. 其实我蛮看好开源的Netgear WNR
3500L,5个1000M端口有木有?480M的CPU有木有?64M内存有木有?到手的3500L被人抢走了有木有?
可惜只有8M FLASH,抢就抢吧, 我也主要用无线,1000M的有线端口暂时用处不大.
我还是再吹吹h618吧,干净了.

firmware换成Tomato Firmware v1.28.7820 MIPSR1-Toastman K26 USB
VPN了,为了它的IPV6功能.

中兴h618有16M FLASH,安装完firmware后,还能空8M+,用来安装ipkg及sip server.
如果其他开源router没有足够的FLASH空间,则要有usb接口,mount一个小u盘到/opt,8M以上容量就可以了,实际安装完占用约3.5M的空间.

ipkg包里,选择极其轻巧的siproxd做为sip
server,功能自然没有ser及kamailio多,但足够满足简单的通话要求.

ssh到路由器里,Enable
jffs并且mount到/opt,然后安装ipkg基本包,也可参考[Tomato
Pandora之Optware软件安装][].

cat opt.sh 或下载
http://www.3iii.dk/linux/optware/optware-install-ddwrt.sh.txt  
<!--more-->

~~~~ {.brush: .bash}
#!/bin/sh
# Optware pre-installation script, Leon Kos 2006, 2008
# added -verbose_wget to some lines, MrAlvin 2009

REPOSITORY=http://ipkg.nslu2-linux.org/feeds/optware/ddwrt/cross/stable
TMP=/tmp

PATH=/bin:/sbin:/usr/bin:/usr/sbin:/opt/bin:/opt/sbin
unset LD_PRELOAD
unset LD_LIBRARY_PATH

_check_config()
{
    echo "Checking system config ..."
    GATEWAY=$(netstat -rn |
    sed -n 's/^0.0.0.0[ \t]\{1,\}\([0-9.]\{8,\}\).*/\1/p' )
    if [ -n "${GATEWAY}" ]; then
    echo "Using ${GATEWAY} as default gateway."
    else
    echo "Error: No default gateway set!"
    exit 2
    fi
    if [ -s /etc/resolv.conf ]; then
    echo "Using the following nameserver(s):"
    if grep nameserver /etc/resolv.conf ; then
            GATEWAY_SUBNET=$(echo "${GATEWAY}" |
        sed 's/\.[0-9]\{1,3\}\.[0-9]\{1,3\}$//')
        if [ "${GATEWAY_SUBNET}" = "192.168" ]; then
        if grep -q ${GATEWAY} /etc/resolv.conf ; then
            echo "Gateway ${GATEWAY} is also nameserver."
        else
            echo "Warning: local nameserver is different than gateway!"
            echo "Check config or enter:"
            if test -L /etc/resolv.conf ; then 
              echo "  sed -i s/192.168.*/${GATEWAY}/ /tmp/resolv.conf"
            else
              echo "  sed -i s/192.168.*/${GATEWAY}/ /etc/resolv.conf"
            fi
            echo "and try again - or wait to see if your download continues anyway."
        fi
        fi
    else
        echo "Error: No nameserver specified in /etc/resolv.conf"
        exit 5
    fi
    else
    echo "Error: Empty or nonexistent /etc/resolv.conf"
    exit 3
    fi

    if mount | grep -q /opt ; then
    [ -d /opt/etc ] && echo "Warning: /opt partition not empty!"
    else
    echo "Error: /opt partition not mounted."
    echo "for running Optware on JFFS (not recommended), Enter"
    echo "    mkdir /jffs/opt"
    echo "    mount -o bind /jffs/opt /opt"
    echo "to correct this."
    exit 4
    fi
}


_install_package()
{
    PACKAGE=$1
    echo "Installing package ${PACKAGE} ..."
    echo "   Some newer versions of DD-WRT does not show download progress bar,"
    echo "   so just be patient - or check STATUS -> BANDWIDTH tab for download"
    echo "   activity in your routers Web-GUI"
    wget -O ${TMP}/${PACKAGE} ${REPOSITORY}/${PACKAGE}
    cd  ${TMP} 
    tar xzf ${TMP}/${PACKAGE} 
    tar xzf ${TMP}/control.tar.gz
    cd /
    if [ -f ${TMP}/preinst ] ; then
    sh ${TMP}/preinst
    rm -f ${TMP}/preints
    fi
    tar xzf ${TMP}/data.tar.gz
    if [ -f ${TMP}/postinst ] ; then
    sh ${TMP}/postinst
    rm -f ${TMP}/postinst
    fi
    rm -f ${TMP}/data.tar.gz
    rm -f ${TMP}/control.tar.gz
    rm -f ${TMP}/control
    rm -f ${TMP}/${PACKAGE}
}

_check_config
_install_package uclibc-opt_0.9.28-13_mipsel.ipk
_install_package ipkg-opt_0.99.163-10_mipsel.ipk
/opt/sbin/ldconfig
/opt/bin/ipkg -verbose_wget update 
/opt/bin/ipkg -force-reinstall -verbose_wget install uclibc-opt
/opt/bin/ipkg -force-reinstall -verbose_wget install ipkg-opt
~~~~

安装

~~~~ {.brush:bash}
cd /opt
sh ./opt.sh
ipkg update
~~~~

先安装libtool库,打包sipproxd时人没把这个依赖加进去

~~~~ {.brush:bash}
ipkg install libtool
~~~~

安装好用的ngrep工具,这个没有依赖,不安装也可以省点空量.

~~~~ {.brush:bash}
ipkg install ngrep
~~~~

安装sipproxd

~~~~ {.brush:bash}
ipkg install siproxd
~~~~

此时会提示  
To complete the installation, you must edit
/opt/etc/siproxd.conf-example and rename it to /opt/etc/siproxd.conf,  
and then run /opt/etc/init.d/S90siproxd to start siproxd.

其实应该先改/opt/etc/siproxd\_passwd.cfg文件,把sip帐号增加进去,格式很简单.  
然后 cp /opt/etc/siproxd.conf-example /opt/etc/siproxd.conf  
修改if\_inbound及if\_outbound为br0就可以了.
我这里因为用vpn连接了远程的路由器,
可视为全走内网,所以把rtp\_proxy\_enable也设为0了.  
最后启动

~~~~ {.brush:bash}
/opt/etc/init.d/S98siproxd
~~~~

siproxd会在TCP以及UDP的 0.0.0.0:5060上监听.  

这样我把自己路由器里的sip电话以及远端vpn连接的路由器里的sip电话都设置为自己路由器内网ip就可以了.  
简单示意图:  
sip phone1 ----\> GW1,siproxd server & openvpn server----\> internet
\<-----\>GW2,openvpn client \<-----sip phone2  
好了,你就真变成国内大LAN网,也影响不了我打电话了.

siproxd比较可惜的是不支持ipv6,没有查看注册及通话情况等管理功能.如果有啥问题,直接动用ngrep监听数据吧.

  [Tomato Pandora之Optware软件安装]: http://ahui.us/index.php/2010/08/tomato-pandora-optware/
