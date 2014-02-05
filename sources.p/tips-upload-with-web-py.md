Title: Tips : upload with web.py
Date: 2014-01-12 11:37
Author: ahui
Category: Linux, 开发, 网络
Tags: blog, Linux, Network
Slug: tips-upload-with-web-py

1.不同的jquery
upload插件，发送的字段有很大差别，可以通过打印wsgi\_input来查看。

2.文件在比较小时，直接用web.input()取得上传的文件内容及其他相关值。官网例子在这种情况下能正常工作。

3.文件在很大时，web.input无法一次读写，此时可以用rawinput，一次读入一部分数据再写入.
原理上rawinput的数据应该是已经放在磁盘上，这样会有二次写入操作。但能够写入超过内存容量的数据。  

此时有二种方法取得文件大小:一是客户端传入一个filesize字段，html5能取得上传文件的大小，IE不支持;
二是服务端用file.seek方法，取得rawinput.file的长度.

4.文件特别大且，不想二次写入时，可用wsgi\_input,一边读取传入的数据，一边进行写入。但此时读到的是原始数据，会包含一些文件相关的信息，写入后要进行数据整形。可以客户端传入时，简化传入数据以方便整形。

大多数情况下， 可以采用方式３。  

方式4最安全，服务端能根据情况随时中断传输。但没测试是否会阻塞后续页面请求。当然阻塞可以用其他方式解决(eg,协程等)。
