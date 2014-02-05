Title: DIY家用NAS之软件篇
Date: 2011-10-24 16:24
Author: ahui
Category: Linux, 其他, 网络
Tags: blog, Linux, Network
Slug: diy-nas-softeare

NAS系统的选择,首先放弃了windows系统. 然后在DIY linux与现成开源的类linux
nas系统中,确定用现成的freenas,基于freebsd的nas.

freenas现在主版本有7.x 与8.x二个系列.
7.x的风格更类linux一点,配置时要先加硬盘,格式化,再mount到对应目录,最后再共享目录.

不过对于我配置的特定硬件,7.x 无法自动认出板上的网卡以及sata接口.
网卡驱动倒是可以换一个,不过认不出sata接口却无法解决,这样系统启动后一个硬盘都找不到.

8.x系列,封装得更好一点,配置也简单很多. 当然DIY的自由度也少了很多.
另外8.x对ZFS的支持要完善很多,用raid z相当方便.

1.首先去http://www.freenas.org/下载FreeNAS-8.0.2-RELEASE-amd64-Full\_Install.xz,因为用到了8G内存,必须用64位版本,而且zfs文件系统,要求内存越大越好,6G+是必要的.  

2.用7zip解开FreeNAS-8.0.2-RELEASE-amd64-Full\_Install.xz,是个2G左右的FreeNAS-8.0.2-RELEASE-amd64-Full\_Install文件  

3.用dd或physdiskwrite.exe写到一个2G以上的u盘上.用u盘做系统盘,一是能省下一个sata接口以后好扩充,二是8.x的freenas不能再使用系统盘上的空闲空间.  
4.启动nas并配置好ip地址后web登录,默认帐号为admin/freenas  
5.在Storage中,用Create Volume,选取三块硬盘,fs选择zfs,zaid
z模式.命名为public. 这时就创建好了一个总容易为3.8T的raid z卷.
并且以后所有的目录分配或iscsi都基于public卷.  
6.Create ZFS
Dataset用来创建不用的应用目录,用于分配给不同的用户或是用作不同的用途.  
7.Create ZFS Volume创建一个指定容量的大文件,用于iscsi的虚拟磁盘.  
8.配置好后,在System-\>Settings,-\>Save
Config里,保存好当前配置.这样万一系统损坏或u盘物理损坏后,通过前四步,然后导入现有配置就能恢复.  
9.最后在Services中,启用CIFS,FTP以及iSCSI三个主要共享功能.

这样能通过ftp,windows的网上邻居,linux的smb,以及iscsi访问nas上的空间.
1000Mbps网络环境中,上下传速度其中以iscsi速度最快,约70MB/s左右,然后是ftp,60MB/s左右,网上邻居要慢点,40\~50MB/s左右.
100Mbps网络环境三者都能比较稳定在10MB/s左右.
由此可见,使用nas,1000Mbps的网络环境是必要的.

最后从总功耗以及传输速度来看,基本上满足了自己的要求.
