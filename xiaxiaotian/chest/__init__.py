from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from .data_source import get_nextchest_of_tag
import logging
from nonebot.log import logger
@on_command('nextchest', aliases=('宝箱查询'),only_to_me=False)
async def nextchest(session: CommandSession):
    
    tag = session.get('tag', prompt='请回复您的游戏TAG哦。',at_sender=True,only_to_me=True)
    
    nextchest_report = await get_nextchest_of_tag(tag)
    
    await session.send(nextchest_report,at_sender=True)
    logger.info('[宝箱查询]结果已反馈用户,任务结束')
@nextchest.args_parser
async def _(session: CommandSession):
    logger.debug('[宝箱查询]开始过滤无效字符')
    stripped_arg = session.current_arg_text.replace(' ','')
    stripped_arg = session.current_arg_text.replace('#','')
    if session.is_first_run:
        logger.info('[宝箱查询]第一次进入程序，开始分析')      
        if stripped_arg:
            session.state['tag'] = stripped_arg
            logger.info('[宝箱查询]用户第一次输入不为空，作为参数传入并执行查询脚本')
        return
    if not stripped_arg:
        logger.info('[宝箱查询]用户没有输入正确的TAG，重新询问')
        session.pause('您的TAG似乎不对，再试试吧',at_sender=True)
        handle_cancellation(session)  
    logger.info('[宝箱查询]收到了非空白的用户TAG，转接查询实用程序')
    session.state[session.current_key] = stripped_arg
@on_natural_language(keywords={'查宝箱','下一个宝箱','箱子'},only_to_me=True)
async def _(session: NLPSession): 
    return IntentCommand(87.0, 'nextchest')