title: "freeNAS 8.0.1 上 iSCSI存在的几个问题"
id: 380
date: 2012-09-22 16:14:32
tags: 
- Linux
- Network
categories: 
- Linux
- 网络
---

1.二台win 7机器A,B同时连接上iSCSI,分别在iSCSI盘上新建立的文件，互相不可见，需要删除当前的iSCSI连接，再重设。
2.同上A，B二机短时间内写同一目录，大部分情况下会导致些目录损坏，不能再访问。
3.在iSCSI上COPY大文件后，马上重启NAS,文件大部分情况下会丢失。
4.iSCSI盘采用NTFS时，COPY文件速度会降低一些。

可见freeNAS 8.0.1版本上的iSCSI存在比较大的问题，只有在长期开着NAS并且长期只有一个写入用户的情况下，才能放心使用。其他大多数情况，应该采用其他文件共享协议。