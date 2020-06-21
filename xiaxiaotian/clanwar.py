from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
import logging
from nonebot.log import logger
import subprocess
@on_command('dblwar', aliases=('部落3+1','活动查询'),only_to_me=True)
async def dblwar(session: CommandSession):
    tag = session.get('tag', prompt='欢迎使用特别功能!请回复你的游戏TAG查询你的部落战情况吧',at_sender=True,only_to_me=True)
    dblwar_report = await get_dblwar(tag)
    #logger.info('[部落3+1]发送打油诗')
    #await session.send('信息量较大查询可能较慢，敬请谅解\n请稍微休息一下吧：\n部落3 + 1，获胜笑嘻嘻。\n既能拿宝箱，还能拿奖品。\n倘若人数多，岂不悲哀乎？\n管家笑嘻嘻,首领惨兮兮。\n温馨提示：仅为小管家自动吐槽，逗君一笑，请勿当真！',at_sender=True) 
    if dblwar_report == 'ERROR-CRTimeOut':
        logger.info('[部落3+1]出现错误了:官方API查询超时,提示详见Debug模式')
        logger.debug('[部落3+1]详细信息：查询超时.详见小管家Wiki')
        logger.debug('[部落3+1]查询脚本执行完毕并返回信息到Nonebot脚本')
        await session.send('出现意外了：\n因为连接速度太慢所以主动放弃查询了，请您重新使用指令再查询一下吧',at_sender=True)
    elif dblwar_report == 'ERROR-CRNotCallMe':
        logger.info('[部落3+1]用户意外触发或未正常放弃，查询无效,提示详见Debug模式')
        logger.debug('[部落3+1]详细信息：包含英文数字以外的其他语言，查询无效.详见小管家Wiki')
        logger.debug('[部落3+1]查询脚本执行完毕并返回信息到Nonebot脚本')
        await session.send('对不起，你似乎不是来查询信息的(。﹏。)',at_sender=True)
    elif dblwar_report == 'NotWar':
        logger.info('[部落3+1]信息查询完成，部落未开部落战')
        logger.debug('[部落3+1]查询脚本执行完毕并返回信息到Nonebot脚本')
        await session.send('部落战还没有开始呢，着急不是一件好事情(⊙o⊙)哦',at_sender=True)
    elif dblwar_report == 'NoUser':
        logger.info('[部落3+1]信息查询完成，没有参战或不在查询部落')
        logger.debug('[部落3+1]查询脚本执行完毕并返回信息到Nonebot脚本')
        await session.send('没有参战的小坏蛋查什么部落战？一边喝可乐去(￣┰￣)',at_sender=True)   
    else:
        await session.send(dblwar_report,at_sender=True)
        logger.info('[部落3+1]结果无错误并已查询完毕并发送给用户,任务结束')
@dblwar.args_parser
async def _(session: CommandSession):
    logger.debug('[部落3+1]开始过滤无效字符')
    stripped_arg = session.current_arg_text.replace(' ','')
    stripped_arg = session.current_arg_text.replace('#','')
    if session.is_first_run:
        logger.info('[部落3+1]第一次进入程序，开始分析')
        if stripped_arg:
            session.state['tag'] = stripped_arg
            logger.info('[部落3+1]用户第一次输入不为空，作为参数传入并执行查询脚本')
        return
    if not stripped_arg:
        logger.info('[部落3+1]用户没有输入正确的TAG，重新询问')
        session.pause('您要查询的TAG似乎不对，再试试吧',at_sender=True)
        handle_cancellation(session)
    logger.info('[部落3+1]收到了非空白的用户TAG，转接查询实用程序')
    session.state[session.current_key] = stripped_arg
async def get_dblwar(tag: str) -> str:
    dblwar = subprocess.getoutput("python3 lib/clashroyale/dbl/dbl-war.py -u '%s'"%(tag))
    return f'{dblwar}'
@on_natural_language(keywords={'3+1','大部落部落战'},only_to_me=True)
async def _(session: NLPSession):
    return IntentCommand(81.0, 'dblwar')