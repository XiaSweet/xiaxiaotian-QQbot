# -*- coding: utf-8 -*-
import urllib.request
import json
import ssl
import os

with open("mykey.txt") as f:
    mykey=f.read().rstrip("\n")
    
    ssl._create_default_https_context = ssl._create_unverified_context
    
    base_url = "https://api.clashroyale.com/v1"
     
    endpoint = "/clans/%2388GUJ80/currentwar"
    
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

    print('部落战情况如下所示（信息可能较长，敬请谅解QaQ）：')

    print(  )

    for item in data["participants"]:
                    print("成员名称:%s , 战斗日次数:%d次\n已打次数:%s次 , 胜利次数：%s次 , 已打集卡日：%s次" % (
                                    item["name"], 
                                    item["numberOfBattles"],
                                    item["battlesPlayed"],
                                    item["wins"],
                                    item["collectionDayBattlesPlayed"]
                            ))
