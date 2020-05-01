from nonebot import on_command, CommandSession
import os
import subprocess

#Powered by XiaSweet Labs
#宝箱查询实用程序 -CR皇室战争
#本源码来自NoneBot，感谢作者的辛苦付出
#Nonebot https://nonebot.cqp.moe/

# on_command 装饰器将函数声明为一个命令处理器
# 这里 nextchest 为命令的名字（可为不冲突的任意值），同时允许使用别名「宝箱查询」
@on_command('nextchest', aliases=('宝箱查询','查宝箱'))
async def nextchest(session: CommandSession):
    # 从会话状态（session.state）中获取游戏Tag（city），如果当前不存在，则询问用户
    city = session.get('city', prompt='请回复您的游戏TAG。',at_sender=True)
    # 向脚本发送API请求
    nextchest_report = await get_nextchest_of_city(city)
    # 向用户发送宝箱信息
    await session.send(nextchest_report,at_sender=True)


# nextchest.args_parser 装饰器将函数声明为 nextchest 命令的参数解析器
# 命令解析器用于将用户输入的参数解析成命令真正需要的数据
@nextchest.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符和混淆注释号’#’
    stripped_arg = session.current_arg_text.strip()
    stripped_arg = session.current_arg_text.strip('#')

    if session.is_first_run:
        # 该命令第一次运行（第一次进入命令会话）
        if stripped_arg:
            # 第一次运行参数不为空，意味着用户直接将游戏Tag跟在命令名后面，作为参数传入
            # 例如用户可能发送了：宝箱查询 '查询Tag'
            session.state['city'] = stripped_arg
        return

    if not stripped_arg:
        # 用户没有发送有效的城市名称（而是发送了空白字符），则提示重新输入
        # 这里 session.pause() 将会发送消息并暂停当前会话（该行后面的代码不会被运行）
        session.pause('您的TAG似乎不对，再试试吧（请在用户界面中点击即可复制）',at_sender=True)

    # 如果当前正在向用户询问更多信息（例如本例中的要查询的城市），且用户输入有效，则放入会话状态
    session.state[session.current_key] = stripped_arg

#注意：用户的输入Tag在这里的变量是'City'

async def get_nextchest_of_city(city: str) -> str:

    # subprocess.getoutput是用于执行脚本并输出结果的
    users = subprocess.getoutput("python3 xiaxiaotian/super/clashroyale/chests.py -u %s"%(city))
    # 向用户返回的信息（这里是脚本内容）
    return f'{users}'
