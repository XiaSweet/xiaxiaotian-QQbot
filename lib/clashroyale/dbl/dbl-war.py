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
    try:
        response = urllib.request.urlopen(request).read().decode("utf-8")
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
        nowar = 'notInWar'
        if nowar in data["state"]:
            print('NotWar')
        else:
            for item in data["participants"]:
                usertag = '#'+args.usertag
                if usertag not in item["tag"]:
                    jieguo = ''
                if usertag in item["tag"]:         
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
                    jieguo = ("你的昵称:%s，你的Tag:%s\n战斗日打完次数：%s，集卡日打完次数：%s\n战斗日是否打完：%s，集卡日是否打完：%s" %
                             (
                                    item["name"],                                    
                                    item["tag"], 
                                    item["battlesPlayed"],
                                    item["collectionDayBattlesPlayed"],
                                    zhandou,
                                    jikas
                               )
                         )
                    print("感谢参加部落6月活动，以下是您在最近部落战的情况：")
                    print(jieguo)
                    print("数据来源：CR官方开发者接口，仅供参考。")
                    print('备注：查询信息仅限大部落！！')
                    api ="https://royaleapi.com/clan/JU8YQ28/war"
                    print("如果你想知道更多部落战信息请浏览以下网址:\n%s(英文)"%(api))
                    break
        if jieguo == '':
            print('NoUser')