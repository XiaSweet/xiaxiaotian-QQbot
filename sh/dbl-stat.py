# -*- coding: utf-8 -*-
import urllib.request
import json
import ssl
import os
import argparse

#外部函数引入
parser = argparse.ArgumentParser(description='CR部落战查询程序-详细信息')
parser.add_argument('--clantag', '-c', help='填写你的部落Tag，必需')
parser.add_argument('--usertag','-u',help='你的Tag')
args = parser.parse_args()

with open("mykey.txt") as f:
    mykey=f.read().rstrip("\n")
    
    ssl._create_default_https_context = ssl._create_unverified_context
    
    base_url = "https://api.clashroyale.com/v1"
     
    endpoint = "/clans/%23"

    clan = (args.clantag)

    member = "/members"
    
    request = urllib.request.Request(
                   base_url+endpoint+clan+member,
                   None,
                   {
                            "Authorization":"Bearer %s" % mykey
                   }
                )
    response = urllib.request.urlopen(request).read().decode("utf-8")
       
    data = json.loads(response)

    os.system('python3 hello-user.py -t %s ' %(args.usertag))

    print("以下是您想查询部落的成员详细信息:")

    print( )
    
    for item in data["items"]:
                    mem = ("成员名称：%s,奖杯：%d,竞技场:%s,Tag: %s " % (
                                    item["name"], 
                                    item["trophies"],
                                    item["arena"]["name"], 
                                    item["tag"]
                            ))
                    mem = mem.replace('Master II','大师联赛二')
                    mem = mem.replace('Master I','大师联赛一')
                    mem = mem.replace('Challenger III','黄金联赛三')
                    mem = mem.replace('Challenger II','白银联赛二')
                    mem = mem.replace('Legendary Arena','青铜联赛一')
                    mem = mem.replace('Arena 12','12阶')
                    mem = mem.replace('Arena 11','11阶')
                    mem = mem.replace('Arena 10','10阶')
                    mem = mem.replace('Arena 9','9阶')
                    mem = mem.replace('Arena 8','8阶')                    
                    print(mem)
    print ('如果您想继续查询成员信息请使用xxxx.py')
                    
