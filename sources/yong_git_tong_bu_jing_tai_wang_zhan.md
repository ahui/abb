title: 用git同步静态网站
date:  2014-02-06 07:30:17
file:  yong_git_tong_bu_jing_tai_wang_zhan.md
tags: 
- blog
- network
memo: 
- ":"号与"-"号紧接着至少一个空格
- tags英文大小写无关，可以用memo的无序列表方式，也可以删除 "- notag" 行，然后用同一行的方式，多tag用","号分隔，如"tags: tag1, tag2"
- 正文与文件参数用空行分隔
- memo不算字数...file与memo也不参与文章发布。这二项可以在模板文件init.md中删除。
- ahui at ahui.us,2014

ABB(Ahui Blog Build)生成的静态html文件，可以用git比较方便的同步到VPS Server上。

首先Server和Client二边都安装好git.

VPS Server上做如下设定后，就不用管了：

创建git仓库目录为www.git，要安全起见，可以换用个普通用户帐号，并修改相应目录及权限。

    cd /root/tmp
    mkdir www.git
    cd www.git
    git --bare init

建立www根目录，并配置nginx指向。

    mkdir /home/wwwstatic/public

建立git hook,在Client push文件后，自动checkout到指定的www根目录

    cat > hooks/post-receive
    #!/bin/bash
    GIT_WORK_TREE=/home/wwwstatic/public git checkout -f

加上可执行属性

    chmod +x post-receive

Server端设置完毕。

Client端如果还没有ssh key,则用

    ssh-keygen -t rsa -C "your_email@example.com"

生成key,然后将~/.ssh/id_rsa.pub中的内容复制到Server端的 /root/.ssh/authorized_keys中。

然后进入静态html生成目录，做一次初始化。

    cd public
    git init
    git remote add ahuius root@ahui.us:/root/tmp/www.git

设定完毕。

这样每次用abb bulid整个站点后，执行下sync.sh就可以将新生成的html文件同步到vps的www根目录了。
 
    cat sync.sh

    #!/bin/bash
    cd public
    git add .
    git commit -m "ok"
    git push -f ahuius master

这篇Blog是完成设定后第一篇被同步的文章.

    ./sync.sh
    [master 97bc2d2] ok
     84 files changed, 1000 insertions(+), 671 deletions(-)
     create mode 100644 post/yong_git_tong_bu_jing_tai_wang_zhan.html
    Counting objects: 174, done.
    Delta compression using up to 4 threads.
    Compressing objects: 100% (88/88), done.
    Writing objects: 100% (88/88), 21.61 KiB, done.
    Total 88 (delta 84), reused 0 (delta 0)
    To root@ahui.us:/root/tmp/www.git
       7167c21..97bc2d2  master -> master
