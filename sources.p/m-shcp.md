Title: 修正Syntax Highlighter ComPress的自动换行问题
Date: 2010-07-16 22:12
Author: ahui
Category: Linux, 网络
Tags: blog, Linux
Slug: m-shcp

Syntax Highlighter
ComPress语法加亮插件在我用的模板中不能自动换行．改了下ＣＳＳ先用着．可惜这个插件在IE下有小部分不能正常显示，FF下大部分正常．

查找syntax-highlighter-compress/styles/shCoreEclipse.css中的

~~~~ {.brush:css}
.syntaxhighlighter .line {
  white-space: pre !important;
}
~~~~

改为

~~~~ {.brush:css}
.syntaxhighlighter .line {
 white-space: pre-wrap;       
 white-space: -moz-pre-wrap; 
 white-space: -pre-wrap;    
 white-space: -o-pre-wrap; 
 word-wrap: break-word;
}
~~~~

保存就ok了.
