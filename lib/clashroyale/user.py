# -*- coding: utf-8 -*-
import urllib.request
import urllib.error
import json
import ssl
import os
import argparse
#外部函数引入
parser = argparse.ArgumentParser(description='CR查询程序 - 用户详细信息')
parser.add_argument('--usertag','-u',help='你要查询的Tag')
args = parser.parse_args()

with open("lib/clashroyale/mykey.txt") as f:
    mykey=f.read().rstrip("\n")
    ssl._create_default_https_context = ssl._create_unverified_context
    base_url = "https://api.clashroyale.com/v1"
    endpoint = "/players/%23"
    tag = (args.usertag) 
    request = urllib.request.Request(
                   base_url+endpoint+tag,
                   None,
              {
                            "Authorization":"Bearer %s" % mykey
                   }
                ) 
    try:            
        response = urllib.request.urlopen(request,timeout=2.2).read().decode("utf-8")
    except urllib.error.HTTPError as e:
        code = (e.code)
        if 404:
            print('ERROR-CR404')
            exit
        elif 400:
            print('ERROR-CR400')
            exit
        elif 403:
            print('ERROR-CR403')
            exit
    except Exception as e:
        print("ERROR-CRTimeOut")
        exit
    except UnicodeEncodeError:
        print("ERROR-CRNotCallMe")
        exit
    else:   
        data = json.loads(response)
        os.system("python3 lib/clashroyale/hello-user.py -t '%s'"%(args.usertag))
        print('以下是用户的详细信息：')
        user = ("个人信息:\n所在竞技场:%s ，国王塔等级:%s\n目前杯数:%s，最高杯数:%s")%(
                        data["arena"]["name"],
                        data["expLevel"],
                        data["trophies"],
                        data["bestTrophies"]
        )
        clan = ("所在部落信息:\n所在部落:%s，部落Tag:%s\n本周捐卡:%s，本周收卡:%s\n部落职位:%s") %(
                        data["clan"]["name"],
                        data["clan"]["tag"],
                        data["donations"],
                        data["donationsReceived"],
                        data["role"]
                        )
        #竞技场段翻译
        user = user.replace('Ultimate Champion','终极冠军联赛')
        user = user.replace('Royal Champion','皇室冠军联赛')
        user = user.replace('Grand Champion','超级冠军联赛')
        user = user.replace('Champion','冠军联赛')
        user = user.replace('Master','大师联赛')
        user = user.replace('Legendary','普通联赛')
        user = user.replace('Arena','普通竞技场')
        #部落职位翻译
        clan = clan.replace('coLeader','副首领')
        clan = clan.replace('leader','首领')
        clan = clan.replace('member','成员')
        clan = clan.replace('elder','长老')
        print(user)
        print(clan)
        print('想查询更加详细的用户信息吗？敬请浏览：')
        royapi = ("https://royaleapi.com/player/%s（英文）")%(args.usertag)
        print(royapi)
        print('小管家猜测您似乎需要:"宝箱查询"或"部落查询"可以发送指令查询(⊙o⊙)哦')
    


    

