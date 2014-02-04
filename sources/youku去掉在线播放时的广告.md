title: "Youku去掉在线播放时的广告"
id: 290
date: 2011-02-21 15:10:02
tags: 
- Network
categories: 
- 网络
---

最简单的,在hosts文件中,加入
127.0.0.1 valf.atm.youku.com
就能去掉播放前的广告.
要想去掉所有广告,则要在hosts文件中加入下列行:
127.0.0.1 atm.youku.com 
127.0.0.1 Fvid.atm.youku.com 
127.0.0.1 html.atm.youku.com 
127.0.0.1 valb.atm.youku.com 
127.0.0.1 valf.atm.youku.com 
127.0.0.1 valo.atm.youku.com 
127.0.0.1 valp.atm.youku.com 
127.0.0.1 lstat.youku.com 
127.0.0.1 speed.lstat.youku.com 
127.0.0.1 urchin.lstat.youku.com 
127.0.0.1 stat.youku.com 
127.0.0.1 static.lstat.youku.com 
127.0.0.1 valc.atm.youku.com 
127.0.0.1 vid.atm.youku.com 
127.0.0.1 walp.atm.youku.com

win7系统下
C:\Users\当前用户\AppData\Roaming\Macromedia\Flash Player\#SharedObjects\随机串
static.youku.com目录改名，并新建同名文件。

参考连接
http://www.itopdog.cn/software-tech/noad.html
http://www.jcboy.info/2011/02/pingbiyoukutudoudengshipinwangzhan15miaoguanggaodezuiquanzuijiandanfangfa.htm