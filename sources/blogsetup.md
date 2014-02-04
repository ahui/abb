title: "我的博客架设笔记"
id: 13
date: 2010-07-15 20:53:47
tags: 
- blog
- Linux
- Network
categories: 
- Linux
---

博客架设前，试用了很多相关程序，包括drupal,dedecms,wordpress等，甚至单文件的TiddlyWiki． 个人觉得TiddlyWiki在本地使用是很方便的，只是放在网上管理上会比较麻烦．drupal在定制一番后，也蛮好用，麻烦就麻烦在要定制不少东西．最后决定用wordpress，相对drupal来说，wordpress上手要容易得多，特别是新版本的wordpress 3的menu很好用.

WP3计划放在安装了centos５的ＶＰＳ上，使用源代码编译安装apache,mod_php以及mysql三大件．Nginx要下次再换了，因为现在最新版本的php5.3.2编译成fpm方式比较麻烦．好在fpm已经进入ＰＨＰ的ＳＶＮ了，不久就应该有官方的fpm出来．

安装过程写在下面，方便以后重个装，查个找什么的．

１．安装apache

从官方网站　http://httpd.apache.org/　下载　httpd-2.2.15.tar.gz
把所有扩展功能都编译成模块，用--enable-modules=all与--enable-mods-shared=all二个参数．把all替换成most，则只编译大部分模块，或者指定模块名．懒人用all吧，编译完成后再去配置文件里，去掉不要的功能．
<pre class="brush:shell">
tar vzxf httpd-2.2.15.tar.gz
cd httpd-2.2.15
./configure --prefix=/usr/local/apache2 \
--enable-modules=all \
--enable-mods-shared=all
</pre>
apache的配置文件在ＰＨＰ安装完成后再修改．
<!--more-->
２．安装mysql

从官方网站http://mysql.com下载mysql-5.1.35.tar.gz
其实mysql的安装，用yum最方便，我自己编译安装，是yum update时省点流量．虽然这个ＶＰＳ流量挺多...
<pre class="brush:shell">
tar -vzxf mysql-5.1.35.tar.gz
cd mysql-5.1.35
./configure --prefix=/usr/local/mysql \
--enable-assembler \
--with-charset=utf8 \
--enable-thread-safe-client \
--with-extra-charsets=all \
--with-big-tables \
--with-readline \
--with-ssl \
--with-embedded-server \
--enable-local-infile

make &amp;&amp; make install
groupadd mysql
useradd -g mysql mysql
cp /usr/local/mysql/share/mysql/my-medium.cnf /etc/my.cnf /usr/local/mysql/bin/mysql_install_db --user=mysql
chown -R mysql /usr/local/mysql/var
chgrp -R mysql /usr/local/mysql/.
cp /usr/local/mysql/share/mysql/mysql.server /etc/init.d/mysql
chmod 755 /etc/init.d/mysql
echo "/usr/local/mysql/lib/mysql" &gt;&gt; /etc/ld.so.conf
echo "/usr/local/lib" &gt;&gt;/etc/ld.so.conf
ln -s /usr/local/mysql/lib/mysql /usr/lib/mysql
ln -s /usr/local/mysql/include/mysql /usr/include/mysql
ldconfig
</pre>
安装完成后，修改/etc/my.cnf文件．用#注释掉skip-networking，开启ＴＣＰ监听．
#skip-networking
并在之后插入下面这行，只在本机监听：
bind-address=127.0.0.1

３．安装ＰＨＰ

centos没有现成的libiconv包，所以在编译PHP之前要手动编译下libiconv.
要用最新的1.13.1才行,1.13我这里编译后PHP死活找不到．
<pre class="brush:shell">
wget http://ftp.gnu.org/pub/gnu/libiconv/libiconv-1.13.1.tar.gz
tar -zxvf libiconv-1.13.1.tar.gz
cd libiconv-1.13.1
./configure --prefix=/usr/local/libiconv
make
make install
</pre>
从http://php.net上下载php-5.3.2.tar.gz
现在可以编译PHP子，有一个老长老长的编译参数:
<pre class="brush:shell">
tar vzxf php-5.3.2.tar.gz
cd php-5.3.2.tar.gz
./configure \
--with-apxs2=/usr/local/apache2/bin/apxs \
--with-mysql \
--with-mysqli=/usr/local/mysql/bin/mysql_config \
--with-iconv=/usr/local/libiconv \
--with-freetype-dir \
--with-jpeg-dir \
--with-png-dir \
--with-zlib \
--with-libxml-dir=/usr \
--enable-xml \
--disable-rpath  \
--enable-magic-quotes \
--enable-safe-mode \
--enable-bcmath \
--enable-shmop \
--enable-sysvsem \
--enable-inline-optimization \
--with-curl \
--with-curlwrappers \
--enable-mbregex \
--enable-mbstring \
--with-mcrypt \
--enable-ftp \
--with-gd \
--enable-gd-native-ttf \
--with-openssl \
--with-mhash \
--enable-pcntl \
--enable-sockets \
--with-xmlrpc \
--enable-zip \
--enable-soap \
--without-pear \
--with-gettext
make
make install
</pre>
安装后php说是会自动修改/usr/local/apache/conf/httpd.conf文件，检查了下，发现
<pre class="brush:plain">
LoadModule php5_module        modules/libphp5.so
</pre>
会被自动加入，但还是要手工添加
<pre class="brush:plain">
AddType application/x-httpd-php .php
</pre>
把这行放到任意一个AddType行之后就行.

再次修改apache的配置文件/usr/local/apache/conf/httpd.conf，去掉所有不必要模块（用#注释掉相应的LoadModule行），只保留下面几个：
<pre class="brush:plain">
LoadModule log_config_module modules/mod_log_config.so
LoadModule mime_module modules/mod_mime.so
LoadModule dir_module modules/mod_dir.so
LoadModule rewrite_module modules/mod_rewrite.so
LoadModule php5_module        modules/libphp5.so
</pre>
查找
<pre class="brush:plain">
<IfModule dir_module>
    DirectoryIndex index.php index.html index.htm
</IfModule>
</pre>
加入index.php作为默认页面．
用#注释所有以Order用Deny开头的行：
<pre class="brush:plain">
    #Order deny,allow
    #Deny from all
</pre>
查找
<pre class="brush:plain">
#Include conf/extra/httpd-mpm.conf
</pre>
去掉前面的#，并修改httpd-mpm.conf，考虑到现在来我这的客人会比较少，数字填写小点，省点内存．要想过好日子，能省点就省点吧...
<pre class="brush:plain">
<IfModule mpm_prefork_module>
    StartServers          3
    MinSpareServers       3
    MaxSpareServers       5
    MaxClients            50
    MaxRequestsPerChild   500
</IfModule>
</pre>
其中MaxRequestsPerChild默认值为0．最好改为非0值，500,1000都可．这样一个apache子进程在做完500个份内工作后，会光荣退休，换新鲜血液上来，防止他一直霸占工作岗位．

４．启动mysql及apache

麻烦的东西都安装好了，现在可以启动mysql和apache了．
<pre class="brush:shell">
/etc/init.d/mysql start
/usr/local/apache2/bin/apachectl start
</pre>

5．安装wordpress3
从http://wordpress.org下载最新版本的wordpress，我下载的是3.0
<pre class="brush:shell">
wget http://wordpress.org/latest.tar.gz
tar vzxf latest.tar.gz
mv wordpress/* /usr/local/apache2/htdocs
</pre>
这样就把wp3放到apache默认网站的根目录了

安装wp3前，要先安装phpmyadmin，用来操作mysql数据库．yum install phpmyadmin 或者直接官网下载解开就好．放在htdocs/db下.
默认mysql root口令为空，如果是新版本的phpmyadmin，要修改一下其配置文件config.inc.php，才能正常login.
<pre class="brush:plain">
$cfg['Servers'][$i]['AllowNoPassword'] = true;
</pre>
默认为false,改为true就好．没有这行就不用管．

先在firefox打开　http://站点ip或域名/db　，首先修改root口令，然后在mysql里单独建立一个新用户如wp及新库如wp，并将库wp的所有权限授予新用户wp．完成后刷新下权限表．

再打开　http://站点ip或域名　就可以正常安装wordpress了，数据库地址填写localhost 或127.0.0.1，最好mysql新用户wp对应的host字段也是localhost.　

6\. 可能存在的问题
安装程序如果提示配置文件wp-config.php无法创建，大部分原因是因为htdocs目录的权限问题．
先查找用户名
<pre class="brush:plain">
cat /usr/local/apache2/conf/httpd.conf | grep -1 Group
#
# User/Group: The name (or #number) of the user/group to run httpd as.
# It is usually good practice to create a dedicated user and group for
--
User daemon
Group daemon
</pre>
可见apache是以daemon的身份运行的，更改用户并查看结果
<pre class="brush:plain">
chown -R daemon.daemon /usr/local/apache2/htdocs
ls -ld /usr/local/apache2/htdocs/
drwxr-xr-x 6 daemon daemon 4096 Jul 15 22:33 /usr/local/apache2/htdocs/
</pre>
再运行wordpress安装程序就能自动建立配置文件了．以后也不会出现wordpress安装插件或升级时，要输入连接信息的错误．

到这里安装就差不多完成了．接下来就是配置插件等内容了．有空再慢慢写.