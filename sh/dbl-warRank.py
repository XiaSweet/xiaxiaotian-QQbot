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

    print('部落战信息如下所示：')

    print( )

    for item in data["clans"]:
                    war = ("部落名称：%s\n战斗日未打次数：%d\n胜利次数：%s\n部落杯数：%s\n参战人数：%s\n " %
                             (
                                    item["name"], 
                                    item["battlesPlayed"],
                                    item["wins"],
                                    item["clanScore"],
                                    item["participants"]
                                              )
                         )
                    lists = "battlesPlayed"
#                    a=sorted(lists.items(),key=lambda e:e[1],reverse=True)  //j技术还是不到家，有空还算继续恶补恶补Python吧QaQ
                    print (war)
