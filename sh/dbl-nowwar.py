# -*- coding: utf-8 -*-
import urllib.request
import json
import ssl

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
    
    for item in data["participants"]:
                    print("成员名称：%s\n战斗日次数：%d\n已打次数：%s\n胜利次数：%s\n集卡日次数：%s\n " % (
                                    item["name"], 
                                    item["numberOfBattles"],
                                    item["battlesPlayed"],
                                    item["wins"],
                                    item["collectionDayBattlesPlayed"]
                            ))
