Title: 修正WP-DBManager不能发送邮件与标题乱码的问题
Date: 2010-07-16 18:13
Author: ahui
Category: Linux, 网络
Tags: blog, Linux, Network
Slug: m-wp-dbmanager-mail

WP-DBManager是个不错的数据库管理插件，功能之一是把备份好的数据库打包发送到指定的邮箱．

ＶＰＳ因为没有配置smtp服务，这样php的mail函数不能正常工作，更加考虑到用Gmail信箱用来备份是个很好的选择，于是下载了WP-Mail-SMTP插件，设置ＷＰ用SMTP发信．安装设置好后，测试邮件能发送成功，但WP-DBManager的邮件发送显示ＯＫ，Gmail里面却收不到东西．

换了Configure
SMTP再试，这个插件更智能点，配置Gmail的信箱很容易．一样安装设置好后，测试邮件能发送成功，但WP-DBManager的邮件发送显示ＯＫ，Gmail里面却收不到东西．

于是估计大概可能也许是WP-DBManager的问题．查看了一下，与wp-dbmanager/wp-dbmanager.php及wp-dbmanager/database-manage.php二个文件有关．前者用于配置参数，其中有自动备份并发送邮件功能；后者用于管理备份文件，其中有将备份文件发送到指定信箱功能．果然这二个文件里都将邮件发送部分写成死死的php的mail函数，这样无论WP-Mail-SMTP还是Configure
SMTP有多强大，它都不知道啊～～

修改很简单，查找wp-dbmanager/wp-dbmanager.php中的  
<!--more-->

~~~~ {.brush:php}
mail($backup_email, $mail_subject, $mail_message, $mail_header);
~~~~

改为

~~~~ {.brush:php}
wp_mail($backup_email, $mail_subject, $mail_message, $mail_header);
~~~~

查找wp-dbmanager/database-manage.php中的

~~~~ {.brush:php}
mail($mail_to, $mail_subject, $mail_message, $mail_header）;
~~~~

改为

~~~~ {.brush:php}
wp_mail($mail_to, $mail_subject, $mail_message, $mail_header）;
~~~~

啊，没错，前面加wp\_就好，wp\_mail的相关信息可以参考  

http://phpdoc.wordpress.org/trunk/WordPress/\_wp-includes---pluggable.php.html\#functionwp\_mail  
这样修改后，wp\_mail会使用WP-Mail-SMTP或Configure
SMTP的配置SMTP发送邮件．这二个插件在wp3中都正常工作．

WP-DBManage现在能成功发送打包后的数据库备份文件到指定的Gmail信箱了，8过标题是乱码，好在正文是全Ｅ文的，能看清．  
修正标题乱码，在前面所说的二个php文件中，查找

~~~~ {.brush:php}
$mail_subject = sprintf(__('%s Database Backup File For %s', 'wp-dbmanager'), get_bloginfo('name'), $file_date);
~~~~

均在后面加入下面这一行进行base64编码

~~~~ {.brush:php}
$mail_subject = '=?UTF-8?B?'.base64_encode($mail_subject).'?=';
~~~~

再试一次发送邮件，万事大吉了\~

可能的问题：  
WP-DBManager的设置页面，Path To mysqldump:以及Path To
mysql:在自动检测失败时，要手动填入包含程序名的绝对路径，比如

~~~~ {.brush:plain}
Path To mysqldump:/usr/local/mysql/bin/mysqldump
Path To mysql:/usr/local/mysql/bin/mysql
~~~~

或者在大多数机器上，是在/usr/bin下的．

wp-content/backup-db放有备份文件，确保使用.htaccess进行保护，或者修改这个目录名.

WP-Mail-SMTP或Configure
SMTP配置时，都最好使用ssl加密连接，端口为465．使用Gmail时，也最好用https方式，这样你的网站数据，基本上都在加密通道跑来跑去，还算是比较安全的．
