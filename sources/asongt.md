title: "一首不错的歌以及你不得不掌握的一些的技术"
id: 115
date: 2010-07-19 15:34:31
tags: 
- blog
- ssh
categories: 
- 网络
---

以前曾偶然听到李家怡的原创歌曲：365，觉得很普通的同时又很动听．在网上查了下，youtube上保存的版本不错，有繁体中文字幕，包括歌词，特地记录在这里．

如果你也来到里，看到的却是一个大白框的话，那也是很正常的现象，因为youtube有时候是个不存在的网站，或者说是个看不见的网站．如果你有兴趣听这歌，或者是有兴趣围观下传说中的网站，那么，滚动鼠标到白框后面，做点技术层面上的事后，再刷新本页面吧．

<!--more-->

<object width="640" height="385"><param name="movie" value="http://www.youtube.com/v/Ncu43zOHT0o&amp;hl=zh_CN&amp;fs=1"></param><param name="allowFullScreen" value="true"></param><param name="allowscriptaccess" value="always"></param><embed src="http://www.youtube.com/v/Ncu43zOHT0o&amp;hl=zh_CN&amp;fs=1" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" width="640" height="385"></embed></object> 

歌词如下:
<pre class="brush:plain">
李家怡 - "365"  
词/曲/演唱 李家怡

闷热的夏天 平淡的秋天
突然间在我的眼里都变特别
烦躁的春天 懒惰的冬天
都没关系 只要有你在我的身边
我开始发现 所谓的永远
原来远在天近在眼前

No matter day or night
You are still my light
You make me feel that all the things will be alright
No matter how time flies
You are still by my side
I'll see the peace
You know I need you be my guy

难过的阴天 无聊的雨天
幸福的感觉满溢心里 没改变
失去的昨天 未知的明天
都没关系 因为我们有的是今天
你终於出现 我的生命线
从此甜蜜的继续蔓延

No matter day or night
You are still my light
You make me feel that all the things will be alright
No matter how time find
You are still by my side
I'll see the peace
You know I need you be my guy

Oh~
Da da, da da, da da, da da
Oh da da da da da

不管白天黑夜 离不开的视线
答应我一直到白头都不改变
</pre>

仍然强烈建议你用firefox访问本站，一是因为本站访问效果没有在IE下进行调整测试，二是有些活在firefox下方便得多．当然还有更多的理由，就不多说了．
首先你可以在这里获取一个免费的国外ssh帐号:

[美国免费SSH账户|美国免费SSH账号](http://www.freessh.us/)

或者你在twitter follow@freesshus也许能要到一个, BTW，那个twitter也是个看不到的网站，如果你能正常访问，下面的内容就可以跳过了．

然后从这里下载个小工具(windows类操作系统，如果你用linux,直接使用ssh命令，打开监听并指定端口即可)

[plink.exe](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html)

放桌面上，做一个快捷方式，将属性中的目标改为
<pre class="brush:plain">
～\plink.exe -pw 密码　用户名@主机名 -N -C -D 127.0.0.1:7070
</pre>
其中~为plink.exe所在目录，保持原样，假如从freessh.us取得的密码为 JuR3K2,主机为一号主机，那么plink.exe的参数如下面的样子
<pre class="brush:plain">
～\plink.exe -pw JuR3K2　freessh@a.freessh.us-N -C -D 127.0.0.1:7070
</pre>
第一次运行会提示保存证书，确认就行．连接成功会显示形如
<pre class="brush:plain">
Using username "freessh".
</pre>
这样就ok了．

Firefox推荐安装AotoProxy插件，代理服务器选择默认的SSH -D就行，然后刷新本页．
IE要在Internet选项里，把套接字代理服务器设置为127.0.0.1，端口7070，然后刷新本页．

可能有的问题：
最近freessh相当火爆，如果服务器状态显示繁忙，密码就拿不到了．如果你有耐心，评论里留下email，我会发送一个最长一个月有效的香港ssh帐号给你试用，限额前五名．
现在还能用的ssh国外帐号申请网站
[http://www.cjb.net/](http://www.cjb.net/)
add一个新的free ssh提供网站
[http://ssh.daili.vc/](http://ssh.daili.vc/)