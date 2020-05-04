#- * -coding: utf - 8 - * -
import urllib.request
import urllib.error
import json
import ssl
import os

ssl._create_default_https_context = ssl._create_unverified_context
#api接口地址
base_url = "https://v1.hitokoto.cn/"
#请求的句子
#详细请求请参阅：https://developer.hitokoto.cn/sentence/#%E8%AF%B7%E6%B1%82%E5%8F%82%E6%95%B0
juzi = "?c=a&c=b&c=d&c=i&c=c&"

geshi = "json"

#获取句子
request = urllib.request.Request(
    base_url + juzi + geshi
    )
# 检查HTTP错误
try:
    response = urllib.request.urlopen(request).read().decode("utf-8")# 如果出现HTTP错误
except urllib.error.HTTPError as e:
    code = (e.code)
    if 404:
        print('\n远方的信封被抓到二次元了，请稍后再试吧(⊙﹏⊙)\n错误代码:He - YY%s' % (code))
else:
    #读取json
    data = json.loads(response)
    onechat =('来自远方的留言：\n%s\n出自%s '%(
                                data['hitokoto'],
                                data['from']
                                )
                               )
    print (onechat)