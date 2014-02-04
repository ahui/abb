title: "OPENERP 7:菜单添加"
id: 1342
date: 2014-01-20 11:39:30
tags: 
- Linux
- Network
- openerp
categories: 
- Linux
- 开发
- 网络
---

菜单大体上分三层:顶层，侧边，子菜单
添加子菜单分为二种情况，一是添加全新的菜单，此时必须先添加顶层和侧边菜单，只用指定name及id，然后挂上子菜单.
其中顶层菜单不用指定parent,子菜单是必须指定action.
```html
<menuitem id="top_menu" name="Top"/>
<menuitem id="section_top_menu" parent="top_menu" />
<menuitem id="sub_menu" parent="section_top_menu" action="your_action"/>
```

二是挂上已经存在的侧边菜单，此时parent的取值为:对象.菜单id
```html
<menuitem id="real_menu" parent="name_of_module_of_parent.section_top_menu" action="your_action">;
```

不指定对象则会重复建立同名菜单(三层均如此)，哪怕id值也相同。