title: "OPENERP 7 : 报表之sxw格式问题"
id: 396
date: 2013-07-23 13:07:02
tags: 
- Linux
- openerp
categories: 
- Linux
- 开发
---

openerp 7的报表生成方式之一是用openoffice的sxw格式，转换成rml后，再生成pdf.
但直接用openoffice新建文件，并保存为sxw格式时，openerp无法识别。在输出rml时，openoffice的报表插件也经常会出现无法响应的问题。开始以为是openoffice版本过高，换libreoffice 3,4都试了一下，问题依旧。
解决方法一：直接编辑openerp直带sxw文件，再另存。此格式可识别。
解决方法二：查询sxw并没有找到版本相关的问题，直接用openerp模块内的sxw2rm转换，有报uncode类错误。于是在ubuntu 12,utf-8语言环境下，用libreoffice 3,4生成新文件，发现无论sxw或odt格式，均能正确识别。可见python开发，还是linux下问题少点。