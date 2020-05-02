import optparse
import time
import chatlib#这里我上端代码独立生成一个文件“chatlib.py"，所以要导入一下
import json
import ssl
import argparse

#外部函数引入
parser = argparse.ArgumentParser(description='智能AI - 腾讯AI提供支持')
parser.add_argument('--chat','-c',help='你想跟机器人说的话')
parser.add_argument('--null','-n',help='无效的指令')
args = parser.parse_args()

app_key = 'mSTstLFLxSdO6SRp'
app_id = '2128916170'
questionS= (args.chat)
def anso(questionS):
    str_question = questionS
    session = 10000
    ai_obj = chatlib.AiPlat(app_id, app_key)
 
    rsp = ai_obj.getNlpTextChat(session,str_question)
    if rsp['ret'] == 0:
        ask = (rsp['data'])['answer']
        print(ask)
    else:
        if rsp['ret'] == 16394:
            print('我还小，不知道怎么回答你呢。请换个话题聊聊吧QAQ\n错误代码:4 - TXAI16394')
        else:
            print(json.dumps(rsp, ensure_ascii=False, sort_keys=False, indent=4))
if __name__ == '__main__':
    anso(questionS)