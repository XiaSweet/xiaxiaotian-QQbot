from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
#加载AI组件
import optparse
import time
import json
import ssl
import subprocess
#日志记录模块
import logging
from nonebot.log import logger
#注意：用户的想说的话在这里的变量是'chat'


# on_command 装饰器将函数声明为一个命令处理器
# 这里 aichat 为命令的名字（可为不冲突的任意值），同时允许使用别名「跟我聊天」   
@on_command('aichat',only_to_me=True)
async def aichat(session: CommandSession):
    # 获取可选参数，这里如果没有 message 参数，命令不会被中断，message 变量会是 None
    chat = session.state.get('chat')

    # 通过封装的函数获取图灵机器人的回复
    aichat_re = await call_txai_api(chat)
       
    await session.send(aichat_re,at_sender=True)

# aichat.args_parser 装饰器将函数声明为 aichat 命令的参数解析器
# 命令解析器用于将用户输入的参数解析成命令真正需要的数据
@aichat.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符和混淆注释号’#’
    stripped_arg = session.current_arg_text.strip(' ')
    stripped_arg = session.current_arg_text.strip('#')
 
#开始运行命令
async def call_txai_api(chat: str) -> str:
    logger.info('[腾讯闲聊]开始像脚本发送变量并尝试获取回复')
    # subprocess.getoutput是用于执行脚本并输出结果的
    hfchat = subprocess.getoutput("python3 lib/txai_chat/chat.py -c %s"%(chat))
    if hfchat == 'ERROR4':
        logger.info('[腾讯闲聊]出现错误了，代码:4 - TXAI16394')
        logger.info('[腾讯闲聊]指令出现错误并结束')
        return f'你的问题好像有些为难我哦。请换个话题聊聊吧◑﹏◐'
    elif hfchat == 'ERROR6':
        logger.info('[腾讯闲聊]出现错误了，代码:6 - TXAI-YourNetworkBad')
        logger.info('[腾讯闲聊]指令出现错误并结束')
        return f'通往次元的轮船堵船啦，请稍后再找我吧-_-|||'
    elif hfchat == 'ERROR5':
        logger.info('[腾讯闲聊]出现错误了，代码:5 - TXAI16394')
        logger.info('[腾讯闲聊]小提醒：您无法独自解决本问题，请联系管理员协助您处理吧')
        logger.info('[腾讯闲聊]指令出现错误并结束')
        
        return f'因为小管家意外受伤了，请呼唤管理员来拯救吧'
    else: 
        # 向用户返回的信息（这里是脚本内容）
        logger.info('[腾讯闲聊]没有出现错误，正常向用户发送结果')
        logger.info('[腾讯闲聊]指令成功完成并结束')
        return f'{hfchat}'

    
# on_natural_language 装饰器将函数声明为一个自然语言处理器
# keywords 表示需要响应的关键词，类型为任意可迭代对象，元素类型为 str
# 如果不传入 keywords，则响应所有没有被当作命令处理的消息
@on_natural_language(keywords=None,only_to_me=True)
async def _(session: NLPSession):
    # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
    # 确保任何消息都在且仅在其它自然语言处理器无法理解的时候使用 aichat 命令
    return IntentCommand(60.0, 'aichat', args={'chat': session.msg_text.replace(' ','')})