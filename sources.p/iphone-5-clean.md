Title: Iphone 5可用容量恢复
Date: 2013-08-04 14:24
Author: ahui
Category: Linux, 网络
Slug: iphone-5-clean

有台iphone 5莫名可用容量急剧减少，查看可用容易，估计有大约4\~7G容量不见。  
ssh到iphone,du -k查看并查找最占容间的前50个目录,发现明显  
mobile/Library/Caches/com.apple.passd/com.apple.Shoebox  
目录有问题，占用空量4G+,删除之，能释放近6G容量。  
另外照片流也会占用不少容量。

附前50条记录:

<!--more-->

"bytes";"dir";"id"  
10291118;"mobile";1458101  
5041749;"mobile/Library";1454199  
4542087;"mobile/Library/Caches";1450783  
4447000;"mobile/Library/Caches/com.apple.passd";1450713  

4442425;"mobile/Library/Caches/com.apple.passd/com.apple.Shoebox";1450711  
3070707;"mobile/Applications";664860  
2178545;"mobile/Media";1458099  
971237;"mobile/Media/DCIM";1454440  
970566;"mobile/Media/DCIM/100APPLE";1454439  
660713;"mobile/Media/PhotoStreamsData/1330973174";1458010  
660713;"mobile/Media/PhotoStreamsData";1458011  
638525;"mobile/Media/PhotoStreamsData/1330973174/100APPLE";1457952  
544488;"mobile/Media/PhotoData";1455066  
403330;"mobile/Media/PhotoData/Sync";1455058  
403251;"mobile/Media/PhotoData/Sync/100SYNCD";1455056  
351152;"stash";1468737  

313584;"mobile/Applications/68C74FC1-8A0C-4369-8E86-4E599335F7EC";589987  

254071;"mobile/Applications/68C74FC1-8A0C-4369-8E86-4E599335F7EC/Library";589955  

254069;"mobile/Applications/68C74FC1-8A0C-4369-8E86-4E599335F7EC/Library/Application
Support/No\_Backup";589947  

254069;"mobile/Applications/68C74FC1-8A0C-4369-8E86-4E599335F7EC/Library/Application
Support";589948  
204621;"mobile/Media/DCIM/100APPLE/IMG\_0199.mov";1454398  
181566;"mobile/Library/VoiceServices/Assets/zh-CN";1453650  
181566;"mobile/Library/VoiceServices/Assets";1453651  
181566;"mobile/Library/VoiceServices";1453652  
143007;"mobile/Library/Mail";1452332  
142401;"stash/share.VNy9as";1468736  
140309;"stash/Applications.50zavX";1466111  

139514;"mobile/Library/VoiceServices/Assets/zh-CN/synth\_ting-ting\_full\_155mrf22\_270\_06.dat";1453645  
134015;"mobile/Media/PhotoData/Thumbnails";1455062  

131209;"mobile/Applications/68C74FC1-8A0C-4369-8E86-4E599335F7EC/Library/Application
Support/No\_Backup/iphone";589920  

131208;"mobile/Applications/68C74FC1-8A0C-4369-8E86-4E599335F7EC/Library/Application
Support/No\_Backup/iphone/1.0.226789.rsb";589919  

129490;"mobile/Applications/06E1377D-3D25-4736-96B7-287255AC8DC3";556778  

129399;"mobile/Applications/06E1377D-3D25-4736-96B7-287255AC8DC3/VoiceGuideAll.app";556774  
128167;"mobile/Media/DCIM/100APPLE/IMG\_0223.MOV";1454419  

122421;"mobile/Applications/68C74FC1-8A0C-4369-8E86-4E599335F7EC/Library/Application
Support/No\_Backup/ipad2";589918  

122420;"mobile/Applications/68C74FC1-8A0C-4369-8E86-4E599335F7EC/Library/Application
Support/No\_Backup/ipad2/1.0.226789.rsb";589917  

116232;"mobile/Applications/F32D96FF-8020-4BFE-BF3A-C22B7F4E6EF6";660087  

116131;"mobile/Applications/F32D96FF-8020-4BFE-BF3A-C22B7F4E6EF6/PvZ-iPhone\_ZH.app";660084  

114695;"mobile/Applications/9ADE3F3B-D880-4918-A565-09B879094997";617869  

110752;"mobile/Applications/06E1377D-3D25-4736-96B7-287255AC8DC3/VoiceGuideAll.app/data";556488  

105033;"mobile/Applications/F8F8FE94-CA5A-4272-92C4-276948EE1706";663324  

105029;"mobile/Applications/F8F8FE94-CA5A-4272-92C4-276948EE1706/AR.Rescue.app";663310  

99381;"mobile/Applications/0CCB1B6C-9EE9-4F4B-852F-1ED0C26113C2";558084  

99379;"mobile/Applications/0CCB1B6C-9EE9-4F4B-852F-1ED0C26113C2/MerriamWebster.app";558081  
97250;"root";1458263  
94877;"root/Library";1458252  
94852;"root/Library/Caches";1458221  
94550;"mobile/Media/DCIM/100APPLE/IMG\_0172.mov";1454373  

89964;"mobile/Applications/0CCB1B6C-9EE9-4F4B-852F-1ED0C26113C2/MerriamWebster.app/definitions.db";557980  

89116;"mobile/Library/Mail/ExchangeActiveSync979797EC-C70C-4940-9076-2BA004C4C5DD";1451893
