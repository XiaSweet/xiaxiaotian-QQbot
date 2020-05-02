from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
#加载基础组件
import subprocess
#注意：用户的想说的话在这里的变量是'aword'


# on_command 装饰器将函数声明为一个命令处理器
# 这里 achat 为命令的名字（可为不冲突的任意值），同时允许使用别名「跟我聊天」
@on_command('achat',aliases=('一言'),only_to_me=True)
async def achat(session: CommandSession):
    # 获取信息
    aword = session.get('aword')
    # 向脚本发送API请求
    achat_report = await get_achat_of_chat(aword)
    # 向用户发送回复信息
    await session.send(achat_report,at_sender=True)


# achat.args_parser 装饰器将函数声明为 achat 命令的参数解析器
# 命令解析器用于将用户输入的参数解析成命令真正需要的数据
@achat.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符和混淆注释号’#’
    stripped_arg = session.current_arg_text.strip(' ')
    stripped_arg = session.current_arg_text.strip('#')
 
#开始运行命令
async def get_achat_of_chat(aword: str) -> str:

    # subprocess.getoutput是用于执行脚本并输出结果的
    onechat = subprocess.getoutput("python3 lib/yiyan/aword.py"
    # 向用户返回的信息（这里是脚本内容）
    return f'{onechat}'

    
# on_natural_language 装饰器将函数声明为一个自然语言处理器
# keywords 表示需要响应的关键词，类型为任意可迭代对象，元素类型为 str
# 如果不传入 keywords，则响应所有没有被当作命令处理的消息
@on_natural_language(keywords=｛'一言'｝,only_to_me=True)
async def _(session: NLPSession):
    # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
    return IntentCommand(70.0, 'achat')