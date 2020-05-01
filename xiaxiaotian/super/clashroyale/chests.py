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

with open("xiaxiaotian/super/clashroyale/mykey.txt") as f:
    mykey=f.read().rstrip("\n")
    
    ssl._create_default_https_context = ssl._create_unverified_context
    
    base_url = "https://api.clashroyale.com/v1"
     
    endpoint = "/players/%23"

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
    #检查HTTP错误
    try:            
        response = urllib.request.urlopen(request).read().decode("utf-8")
    #如果出现HTTP错误
    except urllib.error.HTTPError as e:
        code = (e.code)
        if 404:
            print('\n你想查询的用户被抓到二次元了，请检查一下再重新发送指令查询吧(⊙﹏⊙)。\n错误提示:无法从官方查询您的TAG,请确保没有中文输入或遗漏再尝试查询吧\n错误代码:GF - %s' %(code) )
            exit
        elif 400:
            print('\n额。。。。QAQ听不懂官方说的话，请联系管理员提供错误提示协助修复吧\n错误提示:没有使用正确的查询地址或官方关闭API了，或许也倒闭了吧( •̀ ω •́ )y\n错误代码：代码GF - 1')
        elif 403:
            print('\nemmm( •̀ ω •́ )我好像打不开门，请联系管理员协助修复吧\n错误提示：钥匙不正确，通常是公网IP地址变更导致的失效情况在家用宽带中较常见.您无法独自修复这个错误，请联系管理员协助吧\n错误代码:GF - 2')
    #没有出现HTTP错误
    else:   
        data = json.loads(response)
        #查询相应的用户名称
        os.system("python3 xiaxiaotian/super/clashroyale/hello-user.py -t %s"%(args.usertag))
        #返回正确的用户信息
        print('以下是您未来可以获得的宝箱Ovo：')
    
        for item in data["items"]:
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
                    chest = chest.replace('+0','下个宝箱:')
                    print (chest)
        print('如需帮助请发送[help]指令哦')
    
    

    


    

