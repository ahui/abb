title: "linux下youku去广告+黑屏"
id: 365
date: 2012-05-03 16:41:25
tags: 
- Linux
- Network
categories: 
- Linux
- 网络
---

去广告
hosts加入

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

去黑屏
cd ~/.macromedia/Flash_Player/#SharedObjects/xxx/
xxx为随机串

rm -tf static.youku.com
touch static.youku.com
sudo chown root.root static.youku.com

重启浏览器。