# -*- coding: utf-8 -*-
import argparse
#外部函数引入
from your import *
from apilib import *
#外部函数引入
parser = argparse.ArgumentParser(description='CR查询程序 - 用户详细信息')
parser.add_argument('--usertag','-u',help='你要查询的Tag')
args = parser.parse_args()

tag = (args.usertag)
data = crapi('players',tag,'')
if data == 404:
        print('ERROR-CR404')
elif data == 400:
        print('ERROR-CR400')
elif data == 403:
        print('ERROR-CR403')
elif data == "CRTimeOut":
    print("ERROR-CRTimeOut")
elif data == "CRNotCallMe":
    print("ERROR-CRNotCallMe")
else:   
    print('久等了，以下是用户"'+cr_user(tag)+'"的详细信息：')
    user = ("个人信息:\n所在竞技场:%s ，国王塔等级:%s\n目前杯数:%s，最高杯数:%s")%(
                    data["arena"]["name"],
                    data["expLevel"],
                    data["trophies"],
                    data["bestTrophies"]
    )
    clan = ("部落信息:\n所在部落:%s，部落Tag:%s\n本周捐卡:%s，本周收卡:%s\n部落职位:%s") %(
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
    #罗马数字翻译
    user = user.replace('I','1级')
    print(user)
    print(clan)
    print('想查询更加详细的用户信息吗？敬请浏览：')
    royapi = ("https://royaleapi.com/player/%s（英文）")%(args.usertag)
    print(royapi)
    print('小管家猜测您似乎需要:"宝箱查询"或"部落查询"可以发送指令查询(⊙o⊙)哦')