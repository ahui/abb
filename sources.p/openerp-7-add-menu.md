Title: OPENERP 7:菜单添加
Date: 2014-01-20 11:39
Author: ahui
Category: Linux, 开发, 网络
Tags: Linux, Network, openerp
Slug: openerp-7-add-menu

菜单大体上分三层:顶层，侧边，子菜单  

添加子菜单分为二种情况，一是添加全新的菜单，此时必须先添加顶层和侧边菜单，只用指定name及id，然后挂上子菜单.  
其中顶层菜单不用指定parent,子菜单是必须指定action.

\<menuitem id="top\_menu" name="Top"/\>  
\<menuitem id="section\_top\_menu" parent="top\_menu" /\>  
\<menuitem id="sub\_menu" parent="section\_top\_menu"
action="your\_action"/\>

二是挂上已经存在的侧边菜单，此时parent的取值为:对象.菜单id  
\<menuitem id="real\_menu"
parent="name\_of\_module\_of\_parent.section\_top\_menu"
action="your\_action"/\>

不指定对象则会重复建立同名菜单(三层均如此)，哪怕id值也相同。
