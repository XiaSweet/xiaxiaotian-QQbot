from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
#回复相应信息
from .data_source import get_nextchest_of_tag

#Powered by XiaSweet Labs
#宝箱查询实用程序 -CR皇室战争
#本源码来自NoneBot，感谢作者的辛苦付出
#Nonebot https://nonebot.cqp.moe/

# on_command 装饰器将函数声明为一个命令处理器
# 这里 nextchest 为命令的名字（可为不冲突的任意值），同时允许使用别名「宝箱查询」
@on_command('nextchest', aliases=('宝箱查询','查宝箱'),only_to_me=False)
async def nextchest(session: CommandSession):
    # 从会话状态（session.state）中获取游戏Tag（tag），如果当前不存在，则询问用户
    tag = session.get('tag', prompt='请回复您的游戏TAG并@我(⊙o⊙)哦。',at_sender=True,only_to_me=True)
    # 向脚本发送API请求
    nextchest_report = await get_nextchest_of_tag(tag)
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
            session.state['tag'] = stripped_arg
        return

    if not stripped_arg:
        # 用户没有发送有效的名称（而是发送了空白字符），则提示重新输入
        # 这里 session.pause() 将会发送消息并暂停当前会话（该行后面的代码不会被运行）
        session.pause('您的TAG似乎不对，再试试吧',at_sender=True)

    # 如果当前正在向用户询问更多信息（例如本例中的要查询的TAG），且用户输入有效，则放入会话状态
    session.state[session.current_key] = stripped_arg

# on_natural_language 装饰器将函数声明为一个自然语言处理器
# keywords 表示需要响应的关键词，类型为任意可迭代对象，元素类型为 str
# 如果不传入 keywords，则响应所有没有被当作命令处理的消息
@on_natural_language(keywords={'查宝箱'},only_to_me=True)
async def _(session: NLPSession):
    # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
    return IntentCommand(87.0, 'nextchest')