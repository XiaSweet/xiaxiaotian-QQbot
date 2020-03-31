# -*- coding: utf-8 -*-
import urllib.request
import json
import ssl
import os

with open("mykey.txt") as f:
    mykey=f.read().rstrip("\n")
    
    ssl._create_default_https_context = ssl._create_unverified_context
    
    base_url = "https://api.clashroyale.com/v1"
     
    endpoint = "/players/%23Y98V0RQR/upcomingchests"
    
    request = urllib.request.Request(
                   base_url+endpoint,
                   None,
                   {
                            "Authorization":"Bearer %s" % mykey
                   }
                )
    response = urllib.request.urlopen(request).read().decode("utf-8")
       
    data = json.loads(response)

    os.system("python3 hello-user.py")

    print('以下是您的未来可以获得的宝箱哦Ovo：')

    print( )
    
    for item in data["items"]:
                    chest = ("宝箱位置:+%s,宝箱名称:%s" % (
                                    item["index"], 
                                    item["name"]
                            ))  
                    chest = chest.replace('Silver Chest','普通银箱')
                    chest = chest.replace('Magical Chest','魔法紫箱')
                    chest = chest.replace('Golden Chest','黄金宝箱')
                    chest = chest.replace('Giant Chest','巨型宝箱')
                    chest = chest.replace('Mega Lightning Chest','国王闪电宝箱（提前恭喜啦Ovo）')
                    chest = chest.replace('Legendary Chest','传奇宝箱')
                    chest = chest.replace('Epic Chest','史诗宝箱')
                    chest = chest.replace('+0','下一场胜利')
                    print (chest)
