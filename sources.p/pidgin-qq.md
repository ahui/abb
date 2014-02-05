Title: Pidgin中QQ协议失效
Date: 2011-02-21 15:06
Author: ahui
Category: 其他, 网络
Tags: Network
Slug: pidgin-qq

大约一二周前,发现pidgin中的qq无法login,查看log显示

QQ: Server busy for 尊敬的用户，您的QQ版本已经停止使用，

请到http://im.qq.com

下载并安装最新的QQ版本。

给您带来不便，敬请谅解！

看来是2008协议已经失效.查找了一下,只发现  
http://code.google.com/p/libqq-pidgin/  
在准备开发2010版本的qq协议,不过还不能使用.只能等待了.

其实最佳方法,还是不要用QQ那玩意了.

update:  
http://code.google.com/p/libqq-pidgin/的插件已经能正常使用.
win下替换掉pidgin安装目录/plugins下的libqq.dll即可.
