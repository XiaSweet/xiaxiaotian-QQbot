# -*- coding: utf-8 -*-
import urllib.request
import urllib.error
import json
import ssl
import os
import argparse
#外部函数引入
parser = argparse.ArgumentParser(description='CR宝箱查询程序')
parser.add_argument('--usertag','-u',help='你的Tag')
args = parser.parse_args()
with open("lib/clashroyale/mykey.txt") as f:
    mykey=f.read().rstrip("\n")
    ssl._create_default_https_context = ssl._create_unverified_context
    base_url = "https://api.clashroyale.com/v1"
    endpoint = "/players/%23"
    #获取变量TAG  
    tag = (args.usertag)
    chests = "/upcomingchests"
    #请求调取官方数据库   
    request = urllib.request.Request(
                   base_url+endpoint+tag+chests,
                   None,
              {
                            "Authorization":"Bearer %s" % mykey
                   }
                )           
    #检查HTTP错误，并设置超时机制
    try:            
        response = urllib.request.urlopen(request,timeout=8).read().decode("utf-8")
    #如果出现HTTP错误
    except urllib.error.HTTPError as e:
        code = (e.code)
        if 404:
            print('ERROR-CR404')
        elif 400:
            print('ERROR-CR400')
        elif 403:
            print('ERROR-CR403')
    #超时反馈信息
    except Exception as e:
        print("ERROR-CRTimeOut")
    #如果出现中文
    except UnicodeEncodeError:
        print("ERROR-CRNotCallMe")
    #没有出现HTTP错误
    else:   
        data = json.loads(response)
        #查询相应的用户名称
        os.system("python3 lib/clashroyale/hello-user.py -t %s"%(args.usertag))
        #返回正确的用户信息
        print('以下是您未来可以获得的宝箱Ovo：')
        for item in data ["items"]:
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