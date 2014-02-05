Title: Chrome字体及缓存目录修改
Date: 2012-08-21 10:35
Author: ahui
Category: 其他, 网络
Tags: blog, Network
Slug: chrome-cache-dir

字体+阴影，打开  
C:\\Users\\[用户名]\\AppData\\Local\\Google\\Chrome\\User
Data\\Default\\User StyleSheets\\Custome.css  
添加  
\*{font-family:Arial,"Microsoft Yahei" !important;}  
\*{text-shadow: silver 0px 0px 1px !important;}

其中第一行将所有字体改为雅黑，第二行设置1px的字体阴影。1440以上高分屏，设置第二行效果很好。1366的只添加第一行。

缓存目录  
shift+右 点击Chrome图标，属性，目标后添加  
--disk-cache-dir=“Z:\\Users\\"

其中Z:为RAM盘，设置RAM盘并修改系统TEMP目录后，会自动建立类Users\\[用户名]的目录。否则如果指定的Users目录不存在，Chrome启动会报错。
