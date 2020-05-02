# -*- coding: utf-8 -*-
import urllib.request
import json
import ssl
import argparse

#外部函数引入
parser = argparse.ArgumentParser(description='CR登陆用户查询程序')
parser.add_argument('--tag', '-t', help='输入你的CR游戏Tag属性，必要参数')
args = parser.parse_args()


with open("lib/clashroyale/mykey.txt") as f:
    mykey=f.read().rstrip("\n")
    
    ssl._create_default_https_context = ssl._create_unverified_context
    
    base_url = "https://api.clashroyale.com/v1"
     
    endpoint = "/players/%23"

    userstag = (args.tag)
    
    request = urllib.request.Request(
                   base_url+endpoint+userstag,
                   None,
                   {
                            "Authorization":"Bearer %s" % mykey
                   }
                )
    response = urllib.request.urlopen(request).read().decode("utf-8")
       
    data = json.loads(response)
    
    user = (data["name"])
                                        
    print('\n欢迎您，敬爱的:',(user))
