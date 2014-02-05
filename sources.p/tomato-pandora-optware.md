Title: Tomato Pandora之Optware软件安装
Date: 2010-08-04 22:21
Author: ahui
Category: Linux, 网络
Tags: Linux, Network
Slug: tomato-pandora-optware

现在用的路由器安装的是Tomato Pandora Version
1.27.0475,有时候要在路由器上抓包,发现这个系统没有配置ngrep或者tcpdump,也没有ipkg,没法直接安装现成的opt包.  
不过发现作者有写接口程序,只是没直接公布.  
1.login到路由器,下载ipkg包的接口程序,用于安装ipkg

~~~~ {.brush:bash}
wget http://pandoric.googlecode.com/svn/Pandora%20%e8%84%b1%e6%9c%ba%e8%bd%af%e4%bb%b6/optware-install.sh
~~~~

不过发现直接下载的文件换行符有问题,要处理一下,或者copy下面的内容,存成optware-install.sh后再上传到路由器里面.

<!--more-->

~~~~ {.brush:bash}
#!/bin/sh
# Optware pre-installation script, Leon Kos 2006

REPOSITORY=http://pandoric.googlecode.com/svn/optware/stable
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
            echo "to correct this."
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
    echo "Enter"
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
/opt/bin/ipkg update
/opt/bin/ipkg install -force-reinstall uclibc-opt
/opt/bin/ipkg install -force-reinstall ipkg-opt
~~~~

2.进入路由器web界面.启用JFFS  

如果启用后,空间不够3M,也就没戏了.我用的一共16M空间,系统占了8M,还空8M.但opt的初始安装,要近3M左右空间.

3.运行下面的命令安装ipkg

~~~~ {.brush:bash}
mkdir /jffs/opt
mount -o bind /jffs/opt /opt
sh optware-install.sh
~~~~

4.修改下/opt/etc/ipkg.conf,源设置为

~~~~ {.brush:bash}
src/gz optware http://pandoric.googlecode.com/svn/optware/stable
~~~~

如果能正常下载,这步不改,用默认源也可

5.ok.能安装想要的软件了

~~~~ {.brush:bash}
ipkg install ngerp
~~~~

如果路由系统升级,这些要重做一次.
