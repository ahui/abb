Title: 魔塔世界自动打挂按键精灵脚本verycd版本
Date: 2010-07-18 18:30
Author: ahui
Category: 游戏, 网络
Tags: game, Network
Slug: scriptverycdmt

很闲的时候，找东西找发时间，无聊就玩了会verycd上的魔塔世界．有时候杀１０来只怪更无聊，何况更要爬１００多层的塔，全是重复劳动．不由想起很久以前用过的按键精灵，做这事最合适了．于是顺手写了个简单的前台脚本，放虚拟机里用蛮方便．后台那块还没看，以后看看会不会加进去．

记得最早用按键精灵好象还是2.x还是3.x来着，现在已经到了8.0，用起来是更方便了，广告也更多了......

脚本不长，100多行，就直接贴在下面，懒人也可以下载能直接运行的小精灵版本．下载压缩文件，全部放在c:\\mt下就好．放别的目录则在代码或小精灵里修改下picPath参数.

[小精灵版本下载][]  
[只下载脚本用到的图片][]

脚本:

<!--more-->

~~~~ {.brush:vb}
//todo
//1.加入修理
//2.加入统计显示
//3.智能判断所处场景

Dim findFlag    //是否找到的标志
Dim stepX       //X偏移量
Dim stepY       //Y偏移量
Dim picPath     //图片所在目录
Dim varGWWZ     //怪物位置
Dim varScreen   //场景,取值为 副本,冲塔,野外杀怪
Dim varLoopNum  //脚本运行次数
Dim varPicsim   //图片相似度
Dim adjX        //x adjust
Dim adjY        //y adjust



//初始设置
UserVar varPicsim=0.8 "图片相似度，0,5~1"
UserVar stepX=20 "查找图片时的偏移量x"
UserVar stepY=20 "查找图片时的偏移量y"
UserVar picPath="c:\mt\" "图片所在目录,以结束" 
UserVar varGWWZ=1 "设置怪物位置,取值为1,2,3"
UserVar varLoopNum=100 "脚本运行次数"
UserVar varScreen=DropList{"副本":"副本"|"冲塔":"冲塔"|"野外杀怪":"野外杀怪"}=2 "场景,取值为 副本,冲塔,野外杀怪"
UserVar adjX=208 "x adjust"
UserVar adjY=84 "Y adjust"


varGWWZ=varGWWZ*60-60

findFlag=false

Delay 500

For varLoopNum
    if varScreen="野外杀怪" then
        Call 野外杀怪
    ElseIf varScreen="冲塔" then
        Call 冲塔
    ElseIf varScreen="副本" then
        Call 副本
    End If
Next
 
//冲塔主程序
Sub 冲塔
    Call 继续探险()
    Delay 1000
    Call 确定打怪()
    Delay 500
    Call 关闭战斗()
    Delay 1000  
End Sub
//野外杀怪主程序 
Sub 野外杀怪
    Call 找到怪物()
    Delay 1000
    Call 确定打怪()
    Delay 500
    Call 关闭战斗()
    Delay 1000
End Sub

//副本主程序
Sub 副本
    Call 副本攻击()
    Delay 1000
    Call 确定打怪()
    Delay 500
    Call 关闭战斗()
    Delay 1000
End Sub

Sub 副本攻击
    If 试图查找点击图片(801,407,870,432,"攻击.bmp",35,14)=false then
        //没有找到则退出
        MessageBox "没有找到哦,我先休息会儿~~"
        EndScript
    End If
End Sub

Sub 继续探险
    If 试图查找点击图片(566,484,643,513,"继续探险.bmp",40,15)=false then
        //没有找到则退出
        MessageBox "没有找到哦,我先休息会儿~~"
        EndScript
    End If
End Sub

Sub 找到怪物
    //光标移动到第一个怪位置
    If 试图查找点击图片(1106,365+varGWWZ,1136,383+varGWWZ,"怪物.bmp",15,9)=false then
        //没有找到则退出
        MessageBox "没有找到怪物哦,我先休息会儿~~"
        EndScript
    End If
End Sub


//查找指定的图片并点击,返回true
//如果没查找,返回false
//参数分别为
//左上x,左上y,右下x,右下y,图片名,点击时偏移x,偏移y
//偏移用于尽量将鼠标移动到图片中间
//查找图片的范围偏移由全局变量决定
Function 试图查找点击图片(sX,sY,eX,eY,picName,mX,mY)
    FindPic sX-stepX-adjX,sY-stepY-adjY,eX+stepX-adjX,eY+stepY-adjY,picPath+picName,varPicsim,intX,intY
    If intX>0 and intY>0 then
        MoveTo intX+mX,intY+mY        
        LeftClick 1
        Delay 500
        //确认点击成功,检查三次
        FindPic sX-stepX-adjX,sY-stepY-adjY,eX+stepX-adjX,eY+stepY-adjY,picPath+picName,varPicsim,intX,intY
        For 3
            if intX>0 and intY>0 then
                //MoveTo intX+mX,intY+mY
                LeftClick 1
                Delay 500
            Else
                Exit For
            End If
        Next
        试图查找点击图片=true
    Else
        试图查找点击图片=false    
    End If
End Function


//查找指定的图片并点击
//如果没查找,延迟一秒后继续查找,找到为止
//参数分别为
//左上x,左上y,右下x,右下y,图片名,点击时偏移x,偏移y
//偏移用于尽量将鼠标移动到图片中间
//查找图片的范围偏移由全局变量决定
Sub 查找点击图片(sX,sY,eX,eY,picName,mX,mY)
    findFlag=false
    While findFlag=false
        FindPic sX-stepX-adjX,sY-stepY-adjY,eX+stepX-adjX,eY+stepY-adjY,picPath+picName,varPicsim,intX,intY
        If intX>0 and intY>0 then
            MoveTo intX+mX,intY+mY
            LeftClick 1
            Delay 500
            //确认点击成功,检查三次
            FindPic sX-stepX-adjX,sY-stepY-adjY,eX+stepX-adjX,eY+stepY-adjY,picPath+picName,varPicsim,intX,intY
            For 3
                if intX>0 and intY>0 then
                    //MoveTo intX+mX,intY+mY
                    LeftClick 1
                    Delay 500
                Else
                    Exit For
                End If
            Next
            findFlag=true
        End If
    Wend
End Sub

Sub 确定打怪
    Call 查找点击图片(626,558,713,596,"确定.bmp",41,17)
End Sub
Sub 关闭战斗
    Call 查找点击图片(712,604,794,636,"关闭.bmp",41,15)
End Sub
Sub 关闭战场
    Call 查找点击图片(720,560,804,593,"关闭战场.bmp",42,16)
End Sub
~~~~

备注一：不做任何改动，能在1024x768下运行，ie or
ff最大化，只显示一行地址栏及一行标签栏．  
备注二：UserVar adjX=208 "x adjust"及UserVar adjY=84 "Y
adjust"设置为0．能在1440x900的本本上运行．其他则要修改下这二个的值．原始图是在1440x900下取的，以攻击第一个野外怪位置为例，"攻击"二个字的图片位置是1104,363．其他分辨率下取这处图边左上角坐标与原始坐标的差值．1024x768下，这二字的左上角坐标为896,279,差值就是现在在用的208,84．以后有空再改为简单点的标识．

可能存在的问题：  

我在按键精灵8时进行调试，发现有时候Uservar定义的变量取值会不正常，后来发现是保存代码后，脚本里所有定义的Uservar值都会被保存下来，放在按键精灵8的安装目录根下，名为uservar.txt文件中．这时候如果只改动脚本里的值，调试运行里仍会读取这个文件里保存的值．理论上按键精灵8在调试里，应该先读取脚本里的值，并更新到uservar.txt中，或者调试里不使用这个文件．  

临里办法是每次调试都删除这个文件，或者直接先在编辑器里的ＧＵＩ中选择确定新值，并先保存，再调试．

  [小精灵版本下载]: http://ahui.us/wp-content/uploads/2010/07/mt.zip
  [只下载脚本用到的图片]: http://ahui.us/wp-content/uploads/2010/07/mtpic.zip
