# -*- coding: utf-8 -*-
import urllib.request
import json
import ssl
import os
import argparse

#外部函数引入
parser = argparse.ArgumentParser(description='CR部落战查询程序')
parser.add_argument('--clantag', '-c', help='填写你的部落Tag，必需')
parser.add_argument('--usertag','-u',help='你的Tag')
args = parser.parse_args()

with open("mykey.txt") as f:
    mykey=f.read().rstrip("\n")
    
    ssl._create_default_https_context = ssl._create_unverified_context
    
    base_url = "https://api.clashroyale.com/v1"
     
    task = "/clans/%23"

    clan = (args.clantag)

    search = "/currentwar"
    
    request = urllib.request.Request(
                   base_url+task+clan+search,
                   None,
                   {
                            "Authorization":"Bearer %s " % mykey
                   }
                )
    response = urllib.request.urlopen(request).read().decode("utf-8")
       
    data = json.loads(response)

    os.system('python3 hello-user.py -t %s ' %(args.usertag))
 
    print('部落战信息如下所示：')

    print( )

    for item in data["clans"]:
                    war = ("部落名称：%s,部落杯数：%d\n胜利次数：%s,参战人数：%s,战斗日未打次数：%s" %
                             (
                                    item["name"], 
                                    item["clanScore"],
                                    item["wins"],
                                    item["participants"],
                                    item["battlesPlayed"]
                                              )
                         )
                    lists = "battlesPlayed"
#                    a=sorted(lists.items(),key=lambda e:e[1],reverse=True)  //j技术还是不到家，有空还算继续恶补恶补Python吧QaQ
                    print (war)

