title: ssh无法连接
date:  2015-05-04 06:15:48
file:  ssh_wu_fa_lian_jie.md
tags: 
- linux
- network
- vps
memo: 
- ":"号与"-"号紧接着至少一个空格
- tags英文大小写无关，可以用memo的无序列表方式，也可以删除 "- notag" 行，然后用同一行的方式，多tag用","号分隔，如"tags: tag1, tag2"
- 正文与文件参数用空行分隔
- memo不算字数...file与memo也不参与文章发布。这二项可以在模板文件init.md中删除。
- ahui at ahui.us,2014

ssh 登录阿里云远VPS,提示

	ssh_exchange_identification: read: Connection reset by peer

几月前出过一次同样问题, 表现在开发机无法登录阿里云 VPS,但可以正常登录HK VPS,而且 HK VPS 也可以正常登录阿里云VPS. 检查下来是阿里云机房误判攻击并阻断了我当前在用的移动IP(移动出网 ip 会被 nat 到一组特定 ip 上),提交工单后才解决.

这次再用 HK VPS 检查,发现也无法登录,应该不是原来的老问题.
本机详细登录日志:

	#ssh ahui$ ssh -vvv -l root serverip
	OpenSSH_6.2p2, OSSLShim 0.9.8r 8 Dec 2011
	debug1: Reading configuration data /etc/ssh_config
	debug1: /etc/ssh_config line 20: Applying options for *
	debug1: /etc/ssh_config line 102: Applying options for *
	debug2: ssh_connect: needpriv 0
	debug1: Connecting to serverip [serverip] port 22.
	debug1: Connection established.
	debug3: Incorrect RSA1 identifier
	debug3: Could not load "/Users/ahui/.ssh/id_rsa" as a RSA1 public key
	debug1: identity file /Users/ahui/.ssh/id_rsa type 1
	debug1: identity file /Users/ahui/.ssh/id_rsa-cert type -1
	debug1: identity file /Users/ahui/.ssh/id_dsa type -1
	debug1: identity file /Users/ahui/.ssh/id_dsa-cert type -1
	debug1: Enabling compatibility mode for protocol 2.0
	debug1: Local version string SSH-2.0-OpenSSH_6.2
	ssh_exchange_identification: read: Connection reset by peer

本机改过 hostname,rsa 没做更改, 同样的 rsa 能登录 HK VPS,应该和证书没关系.

阿里终端连接进去,发现 ssh localhost 居然也无法正常登录,问题应该在 sshd 服务本身.

想到服务器几周前做过一次 apt-get upgrade, 应该是更新导致 sshd 出了问题. 重启 sshd, 问题依旧.

google 结果大部分说是 hosts.allow 的问题,加入 sshd:ALL 后,问题依旧.

最后查看 sshd log:

	May  4 17:05:15 AY1407211542405399a6Z sshd[17586]: fatal: Missing privilege separation directory: /var/run/sshd

发现/var 下 run 目录不存在. 

	cd /var
	mkdir run
	cd run
	mkdir sshd

重启 sshd,问题解决.

问题可能出在 apt-get upgrade 后,服务器没重新启动导致问题出现. 或者本次 upgrade有 bug,重启也不能解决. 没证实. 记录下,系统为:

	uname -a
	Linux AY1407211542405399a6Z 3.13.0-32-generic #57-Ubuntu SMP Tue Jul 15 03:51:08 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux
	cat /etc/issue
	Ubuntu 14.04.2 LTS \n \l