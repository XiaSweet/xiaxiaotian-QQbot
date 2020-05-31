# -*- coding: utf-8 -*-
import urllib.request
import json
import ssl
import os
import argparse

#外部函数引入
parser = argparse.ArgumentParser(description='CR查询程序-特殊活动查询')
parser.add_argument('--usertag','-u',help='你的Tag，必需')
args = parser.parse_args()

with open("lib/clashroyale/mykey.txt") as f:
    mykey=f.read().rstrip("\n")
    
    ssl._create_default_https_context = ssl._create_unverified_context
    
    base_url = "https://api.clashroyale.com/v1"
     
    task = "/clans/%23"

    clan = '88GUJ80'

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
    print('大部落本次部落战排名如下所示：')
    for item in data["participants"]:
                    battles = item["battlesPlayed"]
                    jika = item["collectionDayBattlesPlayed"]
                    if jika == 3:
                        jikas = '是'
                    else:
                        jikas = '否'
                    if battles == 1:
                        zhandou = '是'
                    else:
                        zhandou = '否'
                    war = ("伙伴昵称:%s，伙伴Tag:%s\n战斗日打完次数：%s，集卡日打完次数：%s\n战斗日是否打完：%s，集卡日是否打完：%s" %
                             (
                                    item["name"],                                    
                                    item["tag"], 
                                    item["battlesPlayed"],
                                    item["collectionDayBattlesPlayed"],
                                    zhandou,
                                    jikas
                               )
                         )
                    print (war)

