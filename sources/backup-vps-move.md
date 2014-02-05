title: "整站备份&VPS转移"
id: 284
date: 2010-12-20 15:56:36
tags: 
- blog
- Linux
- Network
categories: 
- Linux
- 网络
---

刚搬的VPS因为硬件故障,不得已又新换了一家.
再一次重做好整个站点后,索性全部打个包,下次只要解压下就能快速恢复.

    tar vzcf vps.all.20101220.tar.gz /* --exclude /dev --exclude /home --exclude /lost+found --exclude /mnt --exclude /proc --exclude /tmp --exclude /var --exclude /boot --exclude /root --exclude /sys

如果网站数据没放在/usr/local/apache2/htdoc下,比如nginx常放在/home/www,则去掉--exclude /home或者单独再打个包

    tar vzcf ahuiblog.20101220.tar.gz /home/www/

恢复系统时,先备份下/etc/sysconfig/network文件,再解开包. 然后还原network文件后重启动.