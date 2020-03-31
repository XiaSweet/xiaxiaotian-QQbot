# -*- coding: utf-8 -*-
import urllib.request
import json
import ssl

with open("mykey.txt") as f:
    mykey=f.read().rstrip("\n")
    
    ssl._create_default_https_context = ssl._create_unverified_context
    
    base_url = "https://api.clashroyale.com/v1"
     
    endpoint = "/players/%23Y98V0RQR"
    
    request = urllib.request.Request(
                   base_url+endpoint,
                   None,
                   {
                            "Authorization":"Bearer %s" % mykey
                   }
                )
    response = urllib.request.urlopen(request).read().decode("utf-8")
       
    data = json.loads(response)
    
    user = (data["name"])
                                        
    print('欢迎您，敬爱的:',(user))
