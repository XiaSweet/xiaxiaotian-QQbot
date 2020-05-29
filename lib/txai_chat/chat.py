import optparse
import time
import chatlib#夏小甜自有调取库
import json
import ssl
import argparse

#外部函数引入
parser = argparse.ArgumentParser(description='智能AI - 腾讯AI提供支持')
parser.add_argument('--chat','-c',help='你想跟机器人说的话',type=str)
parser.add_argument('--appid','-id',help='腾讯AI应用ID')
parser.add_argument('--appkey','-key',help='腾讯AI鉴权Key')
args = parser.parse_args()

app_key = 'mSTstLFLxSdO6SRp'
app_id = '2128916170'
questionS= (args.chat)
def anso(questionS):
    str_question = questionS
    session = 10000
    ai_obj = chatlib.AiPlat(args.appid,args.appkey)
 
    rsp = ai_obj.getNlpTextChat(session,str_question)
    if rsp['ret'] == 0:
        ask = (rsp['data'])['answer']
        print(ask)
    else:
        if rsp['ret'] == 16394:
            print('ERROR4')
        elif rsp['ret'] == 16453:
            print('ERROR5')
        elif rsp['ret'] < 0:
            print('ERROR6')
        elif rsp['ret'] == 16388:
            print('ERROR7')
        else:
            print(json.dumps(rsp, ensure_ascii=False, sort_keys=False, indent=4))
if __name__ == '__main__':
    anso(questionS)