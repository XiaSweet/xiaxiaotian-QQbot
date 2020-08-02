# -*- coding: utf-8 -*-
import argparse
#外部函数引入
from your import *
from apilib import *
parser = argparse.ArgumentParser(description='CR宝箱查询程序')
parser.add_argument('--usertag','-u',help='你的Tag')
args = parser.parse_args()
tag = (args.usertag)
request = crapi('players',tag,'upcomingchests')
if request == 404:
            print('ERROR-CR404')
elif request == 400:
            print('ERROR-CR400')
elif request == 403:
            print('ERROR-CR403')
elif request == "ERROR-CRTimeOut":
            print("ERROR-CRTimeOut")
elif request == "ERROR-CRNotCallMe":
            print("ERROR-CRNotCallMe")
else:
    print ('久等了,查询的用户 :'+cr_user(tag)+'\n您未来可获得的宝箱如下Ovo:')
    for item in request ["items"]:
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
                    chest = chest.replace('+0','下个宝箱')
                    print (chest)
