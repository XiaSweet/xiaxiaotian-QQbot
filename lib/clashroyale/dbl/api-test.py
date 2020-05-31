# -*- coding: utf-8 -*-
import urllib.request
import urllib.error
import json
import ssl
import os
import argparse

#外部函数引入
parser = argparse.ArgumentParser(description='CR查询程序')
parser.add_argument('--usertag','-u',help='你的Tag')
args = parser.parse_args()

with open("../mykey.txt") as f:
    mykey=f.read().rstrip("\n")  
    ssl._create_default_https_context = ssl._create_unverified_context   
    base_url = "https://api.clashroyale.com/v1"     
    endpoint = "/clans/%23"
    tag = 'JU8YQ28'
    war = '/currentwar'
    #请求调取官方数据库   
    request = urllib.request.Request(
                   base_url+endpoint+tag+war,
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
            print('\n你想查询的用户被抓到二次元了，请检查一下再查询吧(⊙﹏⊙)。\n错误提示:无法从官方查询您的TAG,请确保没有中文输入或遗漏再尝试查询吧\n错误代码:GF - %s' %(code) )
            exit
        elif 400:
            print('\n额。。。。QAQ听不懂官方说的话，请联系管理员提供错误提示协助修复吧\n错误提示:没有使用正确的查询地址或官方关闭API了，或许也倒闭了吧( •̀ ω •́ )y\n错误代码：代码GF - 1')
        elif 403:
            print('\nemmm( •̀ ω •́ )我好像打不开门，请联系管理员协助修复吧\n错误提示：钥匙不正确，通常是公网IP地址变更导致的失效情况在家用宽带中较常见.您无法独自修复这个错误，请联系管理员协助吧\n错误代码:GF - 2')
    #没有出现HTTP错误
    else:   
        print(response)

    
    

    


    

