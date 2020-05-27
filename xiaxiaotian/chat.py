from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from nonebot.helpers import context_id, render_expression as expr
from nonebot import get_bot
import optparse
import time
import json
import ssl
import subprocess
import logging
from nonebot.log import logger
TXCHAT_BAD = get_bot().config.TXCHAT_BAD
@on_command('aichat',only_to_me=True)
async def aichat(session: CommandSession):
    chat = session.state.get('chat')
    logger.info('[腾讯闲聊]指令被触发了，开始运行')
    aichat_re = await call_txai_api(chat)
    if aichat_re == 'ERROR4':
        logger.info('[腾讯闲聊]出现意外了，腾讯端还不会回答用户的问题，代码:4 - TXAI16394')
        logger.info('[腾讯闲聊]向用户告知不会回答并结束')
        await session.send(expr(TXCHAT_BAD))
    elif aichat_re == 'ERROR6':
        logger.info('[腾讯闲聊]出现错误了，代码:6 - TXAI-YourNetworkBad')
        logger.debug('[腾讯闲聊]小提醒：网络堵塞，请重新触发即可')
        logger.info('[腾讯闲聊]指令出现错误并结束')
        await session.send('通往次元的轮船堵船啦，请稍后再找我吧-_-|||')
    elif aichat_re == 'ERROR5':
        logger.info('[腾讯闲聊]出现错误了，代码:5 - TXAI16394')
        logger.info('[腾讯闲聊]小提醒：您无法独自解决本问题，请联系管理员协助您处理吧')
        logger.info('[腾讯闲聊]指令出现错误并结束')    
        await session.send('因为小管家意外受伤了，请呼唤管理员来拯救吧')
    else:
        logger.info('[腾讯闲聊]没有出现错误，正常向用户发送结果')
        logger.info('[腾讯闲聊]指令成功完成并结束')
        await session.send(aichat_re,at_sender=True)
async def call_txai_api(chat: str) -> str:
    logger.info('[腾讯闲聊]开始向脚本发送变量并尝试获取回复')
    hfchat = subprocess.getoutput("python3 lib/txai_chat/chat.py -c '%s'"%(chat))
    return f'{hfchat}'
@on_natural_language(keywords=None,only_to_me=True)
async def _(session: NLPSession):
    return IntentCommand(60.0, 'aichat', args={'chat': session.msg_text.replace(' ','+')})