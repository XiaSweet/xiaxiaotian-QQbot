# -*- coding: utf-8 -*-
import urllib.request
import urllib.error
import json
import ssl
def crapi(menu,tag,menu2):
    with open("lib/clashroyale/mykey.txt") as f:
        mykey=f.read().rstrip("\n")
        ssl._create_default_https_context = ssl._create_unverified_context
        base_url = "https://api.clashroyale.com/v1"
        fj = '/'
        endpoint = "/%23"
        #请求调取官方数据库   
        request = urllib.request.Request(
                    base_url+fj+menu+endpoint+tag+fj+menu2,
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
                data = 404
            elif 400:
                data = 400
            elif 403:
                data = 403
        #超时反馈信息
        except Exception as e:
            data = ("CRTimeOut")
        #如果出现中文
        except UnicodeEncodeError:
            data = ("CRNotCallMe")
        else:
            data = json.loads(response)
    return data