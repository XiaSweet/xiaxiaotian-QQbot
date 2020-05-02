import optparse
import time
import chatlib#夏小甜自有调取库
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
        elif rsp['ret'] == 16453:
            print('啊哦，远方的伙伴似乎叫不醒了(┬＿┬)\n小提醒：您无法独占解决问题，请联系管理员协助您处理吧\n错误代码：5 - TXAI16394')
        elif rsp['ret'] < 0:
            print('通往次元的轮船堵船啦，请稍后再找我吧\n错误代码:6 - TXAI-YourNetworkBad')
        else:
            print(json.dumps(rsp, ensure_ascii=False, sort_keys=False, indent=4))
if __name__ == '__main__':
    anso(questionS)