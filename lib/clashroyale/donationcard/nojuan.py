# -*- coding: utf-8 -*-
import urllib.request
import json
import ssl
import argparse

#外部函数引入
parser = argparse.ArgumentParser(description='CR查询程序-0捐查询')
parser.add_argument('--clantag', '-c', help='填写部落代码')
args = parser.parse_args()

with open("lib/clashroyale/mykey.txt") as f:
    mykey=f.read().rstrip("\n")   
    ssl._create_default_https_context = ssl._create_unverified_context
    base_url = "https://api.clashroyale.com/v1"
    endpoint = "/clans/%23"
    if args.clantag == 'dbl0':
        clan = "88GUJ80"
        clanid = '大部落'
        nojuan = True
    elif args.clantag == 'xbl0':
        clan = "JY8YVC0"
        clanid = '小部落'
        nojuan = True
    elif args.clantag == 'dbl':
        clan = "88GUJ80"
        clanid = '大部落'
        nojuan = False
    elif args.clantag == 'xbl':
        clan = "JY8YVC0"
        clanid = '小部落'
        nojuan = False
    else:
        print ('ERROR-CRNotMyClans')
        exit()
    member = "/members"
    request = urllib.request.Request(
                   base_url+endpoint+clan+member,
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
            exit()
        elif 400:
            print('ERROR-CR400')
            exit()
        elif 403:
            print('ERROR-CR403')
            exit()
    except Exception as e:
        print("ERROR-CRTimeOut")
        exit()
    except UnicodeEncodeError:
        print("ERROR-CRNotCallMe")
        exit()
    if nojuan == True:
        response = urllib.request.urlopen(request).read().decode("utf-8")
        data = json.loads(response)
        stat = 0
        for item in data["items"]:
                if item["donations"] == 0 and item["donationsReceived"] > 0:
                    stat = 1
                    break
                else:
                    pass
        if stat == 0:
            print (('恭喜，%s现在没有0捐党，请各位伙伴保持住，Bye(⊙o⊙)！')%(clanid))
        elif stat == 1:
            print(("我最恨的就是0捐要卡的伸手党了〒▽〒\n以下是%s的0捐信息:")%(clanid))
            for item in data["items"]:        
                if item["donations"] == 0 and item["donationsReceived"] > 0:
                    mem = ("成员：%s，捐卡：%d，接卡:%s，Tag: %s " % (
                        item["name"], 
                        item["donations"],
                        item["donationsReceived"], 
                        item["tag"]
                            ))
                    print(mem)
                else:
                    pass
            print ('小提示：重新提醒我查询全部可看到完整信息，已去除0捐0收的好伙伴ovo')
        else:
            print('CRNotError')
    elif nojuan == False:
        response = urllib.request.urlopen(request).read().decode("utf-8")
        data = json.loads(response)
        stat = 0
        for item in data["items"]:
                if item["donationsReceived"]  - item["donations"]  >40:
                    stat = 1
                    break
                else:
                    pass
        if stat == 0:
            print (('%s目前没有发现伸手党，请继续努力哦，Bye(⊙o⊙)！')%(clanid))
        elif stat == 1:
            print(("以下是%s的全部伸手党信息:")%(clanid))
            for item in data["items"]:
                if item["donationsReceived"]  - item["donations"]  >40:
                    mem = ("成员：%s,捐卡：%d,接卡:%s,差距:%s,Tag: %s " % (
                        item["name"], 
                        item["donations"],
                        item["donationsReceived"], 
                        item["donationsReceived"] - item["donations"],                                    
                        item["tag"]
                            ))
                    print(mem)
                else:
                    continue
            print ('注：如果您想继续查询成员信息可使用"用户查询"服务')
        else:
             print('CRNotError')