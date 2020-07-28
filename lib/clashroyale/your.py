# -*- coding: utf-8 -*-
import urllib.request
import json
import ssl
import argparse
#外部函数引入
def cr_user(tag):
    with open("lib/clashroyale/mykey.txt") as f:
        mykey=f.read().rstrip("\n")
        ssl._create_default_https_context = ssl._create_unverified_context
        base_url = "https://api.clashroyale.com/v1"
        endpoint = "/players/%23"
        userstag = (tag)
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
        return user