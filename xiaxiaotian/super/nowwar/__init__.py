from nonebot import on_command, CommandSession
import os
import sys
import subprocess


#连接脚本目录
sys.path.append('xiaxiaotian/super/clashroyale')

# on_command 装饰器将函数声明为一个命令处理器
# 这里 blz 为命令的名字，同时允许使用别名「宝箱查询」
@on_command('blz', aliases=('部落战排名'))
async def blz(session: CommandSession):
    # 从会话状态（session.state）中获取游戏Tag（bltag），如果当前不存在，则询问用户
    bltag = session.get('bltag', prompt='请回复您的部落TAG。')
    # 获取城市的天气预报
    blz_report = await get_blz_of_bltag(bltag)
    # 向用户发送天气预报
    await session.send(blz_report)


# blz.args_parser 装饰器将函数声明为 blz 命令的参数解析器
# 命令解析器用于将用户输入的参数解析成命令真正需要的数据
@blz.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()
    stripped_arg = session.current_arg_text.strip('#')

    if session.is_first_run:
        # 该命令第一次运行（第一次进入命令会话）
        if stripped_arg:
            # 第一次运行参数不为空，意味着用户直接将城市名跟在命令名后面，作为参数传入
            # 例如用户可能发送了：天气 南京
            session.state['bltag'] = stripped_arg
        return

    if not stripped_arg:
        # 用户没有发送有效的城市名称（而是发送了空白字符），则提示重新输入
        # 这里 session.pause() 将会发送消息并暂停当前会话（该行后面的代码不会被运行）
        session.pause('TAG似乎不对哦，请重新输入吧')

    # 如果当前正在向用户询问更多信息（例如本例中的要查询的城市），且用户输入有效，则放入会话状态
    session.state[session.current_key] = stripped_arg

    
#开始查询宝箱
#chest = os.system("python3 chests.py -u %s"%(bltag))


async def get_blz_of_bltag(bltag: str) -> str:
    # 这里简单返回一个字符串
    # 实际应用中，这里应该调用返回真实数据的天气 API，并拼接成天气预报内容
    #chest = os.system("python3 chests.py -u %s"%(bltag))
    users = subprocess.getoutput("python3 xiaxiaotian/super/clashroyale/dbl-warRank.py -c %s"%(bltag))

    return f'{users}'
