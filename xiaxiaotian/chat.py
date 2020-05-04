from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
#加载基础组件
import subprocess
#注意：用户的想说的话在这里的变量是'chat'


# on_command 装饰器将函数声明为一个命令处理器
# 这里 aichat 为命令的名字（可为不冲突的任意值），同时允许使用别名「跟我聊天」
@on_command('aichat',only_to_me=True)
async def aichat(session: CommandSession):
    # 获取信息
    chat = session.get('chat')
    # 向脚本发送API请求
    aichat_report = await get_aichat_of_chat(chat)
    # 向用户发送回复信息
    await session.send(aichat_report,at_sender=True)


# aichat.args_parser 装饰器将函数声明为 aichat 命令的参数解析器
# 命令解析器用于将用户输入的参数解析成命令真正需要的数据
@aichat.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符和混淆注释号’#’
    stripped_arg = session.current_arg_text.strip(' ')
    stripped_arg = session.current_arg_text.strip('#')
 
#开始运行命令
async def get_aichat_of_chat(chat: str) -> str:

    # subprocess.getoutput是用于执行脚本并输出结果的
    hfchat = subprocess.getoutput("python3 lib/txai_chat/chat.py -c %s"%(chat))
    # 向用户返回的信息（这里是脚本内容）
    return f'{hfchat}'

    
# on_natural_language 装饰器将函数声明为一个自然语言处理器
# keywords 表示需要响应的关键词，类型为任意可迭代对象，元素类型为 str
# 如果不传入 keywords，则响应所有没有被当作命令处理的消息
@on_natural_language(keywords=None,only_to_me=True)
async def _(session: NLPSession):
    # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
    # 确保任何消息都在且仅在其它自然语言处理器无法理解的时候使用 aichat 命令
    return IntentCommand(60.0, 'aichat', args={'chat': session.msg_text})