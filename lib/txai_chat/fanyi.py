#-*- coding: UTF-8 -*-
import optparse
import time
import chatlib#夏小甜自有调取库
import json
import ssl
import argparse

app_key = 'mSTstLFLxSdO6SRp'
app_id = '2128916170'

fanyisore = '今天的天气'
if __name__ == '__main__':
    str_text = fanyisore
    type = 0
    ai_obj = chatlib.AiPlat(app_id, app_key)

    rsp = ai_obj.getNlpTextTrans(str_text, type)
    if rsp['ret'] == 0:
        deta = json.dumps(rsp, ensure_ascii=False, sort_keys=False, indent=4)
        datas = json.loads(deta)
        result = ("您想翻译的结果如下：%s \n" %(datas["data"]["trans_text"]))    
        print(result)
    else:
        print(json.dumps(rsp, ensure_ascii=False, sort_keys=False, indent=4))
        #print rsp

