title: "SIP服务器SER 0.9.6:SIP Express Router 安装记录"
id: 135
date: 2010-07-20 16:12:33
tags: 
- Linux
- Network
- sip
categories: 
- Linux
- 网络
---

小时候长话费尤其是国际长话费贵得惊人，几分钟就得１０多块几十块上百块的．由此也出现了不少守个公用电话做为小营生的小商人，倒是制造了或多或少的就业机会，当然那高额的利润究竟最后到了谁手上，就不知道了．

现在费用倒是明里暗里下降了不少，不过你要是有个必须每天打Ｎ通电话的重要人物在外地甚至在外国，话费的Ｎ倍还是吃不太消．就算不存乎，能省点也是几千年来的光荣传统不是？自己架个SIP Server，再用个phone 2 network类的设备，你想打Ｎ通就打Ｎ通，每通想打Ｎ久就打Ｎ久，如果你有那么多话说，不必再担心话费问题了．取而代之的，你可能要担心网费和电费的问题．

现在有不少几合一的家用路由交换一体的设备，都带有电话接口，设置好SIP帐号，接部普通电话就能用了．而最新的智能手机，带wifi功能的，也都基本支持SIP类软件，设置好帐号，直接用wifi通话，也要比走GSM,3G类的网络节省很多．

首先，官网下载源代码．BTW，只能在Linux下安装．Window下也有类似的程序，国产的就有不少，不过我没用过，不做评论．我个人仍然喜欢用开源的东西自己来编译．
<!--more-->
从　http://www.iptel.org/ser/　下载 ser-0.9.6_src.tar.gz
<pre class="brush:plain">
tar vzxf ser-0.9.6_src.tar.gz
cd ser-0.9.6
</pre>
修改Makefile,加入mysql支持
<pre class="brush:plain">
# if not set on the cmd. line or the env, exclude this modules:
exclude_modules?=                             cpl ext extcmd \
                                                        postgres snmp \
                                                        im \
                                                        jabber mysql \
                                                        cpl-c \
                                                        auth_radius group_radius uri_radius avp_radius \
                                                        pa
</pre>
删除其中的mysql字样．
<pre class="brush:plain">
make all
make install
</pre>
修改/usr/local/sbin/ser_mysql.sh，防止默认utf编码时．建立库失败．
查找
<pre class="brush:plain">
echo "creating database $1 ..."

sql_query <<EOF
create database $1;
use $1;
</pre>
create database $1;行后加入
<pre class="brush:plain">
alter database ser character set latin1;
</pre>
建立初始数据库,没有出错提示，会自动建立２４个表，而且其中大部分没用到．
<pre class="brush:plain">
make dbinstall or run /usr/local/sbin/ser_mysql.sh create
</pre>
建立新用户
<pre class="brush:plain">
serctl add username@domin password email
</pre>
安装语音代理rtpproxy,一样从http://www.iptel.org/ser/下载，make,make install就好

配置文件/usr/local/etc/ser/ser.cfg,配置mysql认证，以及NAT修正.
其他类型可在这查看

ftp://siprouter.teigre.com/pub/gettingstarted/configs/

<pre class="brush:plain">
# $Id: nat-rtpproxy.cfg 51 2006-01-31 13:28:04Z /CN=Paul Hazlett/emailAddress=paul@onsip.org $
debug=3
fork=yes
log_stderror=no

listen=192.0.2.13           # INSERT YOUR IP ADDRESS HERE
port=5060
children=4

dns=no
rev_dns=no
fifo="/tmp/ser_fifo"
fifo_db_url="mysql://ser:heslo@localhost/ser"

loadmodule "/usr/local/lib/ser/modules/mysql.so"
loadmodule "/usr/local/lib/ser/modules/sl.so"
loadmodule "/usr/local/lib/ser/modules/tm.so"
loadmodule "/usr/local/lib/ser/modules/rr.so"
loadmodule "/usr/local/lib/ser/modules/maxfwd.so"
loadmodule "/usr/local/lib/ser/modules/usrloc.so"
loadmodule "/usr/local/lib/ser/modules/registrar.so"
loadmodule "/usr/local/lib/ser/modules/auth.so"
loadmodule "/usr/local/lib/ser/modules/auth_db.so"
loadmodule "/usr/local/lib/ser/modules/uri.so"
loadmodule "/usr/local/lib/ser/modules/uri_db.so"
loadmodule "/usr/local/lib/ser/modules/nathelper.so"
loadmodule "/usr/local/lib/ser/modules/textops.so"

modparam("auth_db|uri_db|usrloc", "db_url", "mysql://ser:heslo@localhost/ser")
modparam("auth_db", "calculate_ha1", 1)
modparam("auth_db", "password_column", "password")

modparam("nathelper", "natping_interval", 30) 
modparam("nathelper", "ping_nated_only", 1)   
modparam("nathelper", "rtpproxy_sock", "unix:/var/run/rtpproxy.sock")

modparam("usrloc", "db_mode", 2)

modparam("registrar", "nat_flag", 6)

modparam("rr", "enable_full_lr", 1)

route {

	# -----------------------------------------------------------------
	# Sanity Check Section
	# -----------------------------------------------------------------
	if (!mf_process_maxfwd_header("10")) {
		sl_send_reply("483", "Too Many Hops");
		break;
	};

	if (msg:len > max_len) {
		sl_send_reply("513", "Message Overflow");
		break;
	};

	# -----------------------------------------------------------------
	# Record Route Section
	# -----------------------------------------------------------------
	if (method!="REGISTER") {
		record_route();
	};

	if (method=="BYE" || method=="CANCEL") {
		unforce_rtp_proxy();
	} 

	# -----------------------------------------------------------------
	# Loose Route Section
	# -----------------------------------------------------------------
	if (loose_route()) {

		if ((method=="INVITE" || method=="REFER") && !has_totag()) {
			sl_send_reply("403", "Forbidden");
			break;
		};

		if (method=="INVITE") {

			if (!proxy_authorize("","subscriber")) {
				proxy_challenge("","0");
				break;
			} else if (!check_from()) {
				sl_send_reply("403", "Use From=ID");
				break;
			};
			consume_credentials();

			if (nat_uac_test("19")) {
				setflag(6);
				force_rport();
				fix_nated_contact();
			};
			force_rtp_proxy("l");
		};
		route(1);
		break;
	};

	# -----------------------------------------------------------------
	# Call Type Processing Section
	# -----------------------------------------------------------------
	if (uri!=myself) {
		route(4);
		route(1);
		break;
	};

	if (method=="ACK") {
		route(1);
		break;
	} else if (method=="CANCEL") {
		route(1);
		break;
	} else if (method=="INVITE") {
		route(3);
		break;
	} else  if (method=="REGISTER") {
		route(2);
		break;
	};

	lookup("aliases");
	if (uri!=myself) {
		route(4);
		route(1);
		break;
	};

	if (!lookup("location")) {
		sl_send_reply("404", "User Not Found");
		break;
	};

	route(1);
}

route[1] {

	# -----------------------------------------------------------------
	# Default Message Handler
	# -----------------------------------------------------------------

	t_on_reply("1");

	if (!t_relay()) {
		if (method=="INVITE" && isflagset(6)) {
			unforce_rtp_proxy();
		};
		sl_reply_error();
	};
}

route[2] {

	# -----------------------------------------------------------------
	# REGISTER Message Handler
	# ----------------------------------------------------------------

	if (!search("^Contact:[ ]*\*") && nat_uac_test("19")) {
		setflag(6);
		fix_nated_register();
		force_rport();
	};

	sl_send_reply("100", "Trying");

	if (!www_authorize("","subscriber")) {
		www_challenge("","0");
		break;
	};

	if (!check_to()) {
		sl_send_reply("401", "Unauthorized");
		break;
	};

	consume_credentials();

	if (!save("location")) {
		sl_reply_error();
	};
}

route[3] {

	# -----------------------------------------------------------------
	# INVITE Message Handler
	# -----------------------------------------------------------------

	if (!proxy_authorize("","subscriber")) {
		proxy_challenge("","0");
		break;
	} else if (!check_from()) {
		sl_send_reply("403", "Use From=ID");
		break;
	};

	consume_credentials();

	if (nat_uac_test("19")) {
		setflag(6);
	}

	lookup("aliases");
	if (uri!=myself) {
		route(4);
		route(1);
		break;
	};

	if (!lookup("location")) {
		sl_send_reply("404", "User Not Found");
		break;
	};

	route(4);
	route(1);
}

route[4] {

	# -----------------------------------------------------------------
	# NAT Traversal Section
	# -----------------------------------------------------------------

	if (isflagset(6)) {
		force_rport();
		fix_nated_contact();
		force_rtp_proxy();
	}
}

onreply_route[1] {

	if (isflagset(6) && status=~"(180)|(183)|2[0-9][0-9]") {
		if (!search("^Content-Length:[ ]*0")) {
			force_rtp_proxy();
		};
	};

	if (nat_uac_test("1")) {
		fix_nated_contact();
	};
}
</pre>
先启动rtpproxy,用ftp的用户权限
<pre class="brush:plain">
 /usr/local/bin/rtpproxy -u ftp
</pre>
启动ser
<pre class="brush:plain">
serctl start
</pre>
停止ser
<pre class="brush:plain">
serctl start
</pre>
查看注册用户
<pre class="brush:plain">
serctl ul show
</pre>