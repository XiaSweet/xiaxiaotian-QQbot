import optparse
import time
import chatlib#夏小甜自有调取库
import json
import ssl
def anso(chat,TXAI_APP_ID,TXAI_APP_KEY):
    str_question = chat
    session = 10000
    ai_obj = chatlib.AiPlat(TXAI_APP_ID,TXAI_APP_KEY)
    rsp = ai_obj.getNlpTextChat(session,str_question)
    if rsp['ret'] == 0:
        ask = (rsp['data'])['answer']
        chatre = (ask)
    else:
        if rsp['ret'] == 16394:
            chatre = ('ERROR4')
        elif rsp['ret'] == 16453:
            chatre = ('ERROR5')
        elif rsp['ret'] < 0:
            chatre = ('ERROR6' )
        elif rsp['ret'] == 16388:
            chatre = ('ERROR7')
        else:
            chatre = (json.dumps(rsp, ensure_ascii=False, sort_keys=False, indent=4))
    return chatre
if __name__ == '__main__':
    anso()