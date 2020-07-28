from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from .data_source import get_nextchest_of_tag
import logging
from nonebot.log import logger
import re
from nonebot.helpers import render_expression as expr
import sys
sys.path.append("lib/smartxxt")
import systemre as e
@on_command('nextchest', aliases=('宝箱查询'),only_to_me=False)
async def nextchest(session: CommandSession):
    tag = session.get('tag', prompt='收到，请回复您的游戏TAG哦。',at_sender=True,only_to_me=True)
    await session.send(expr(e.SYSTEM_WAITING))
    nextchest_report = await get_nextchest_of_tag(tag)
    await session.send(nextchest_report,at_sender=True)
    logger.info('[宝箱查询]结果已反馈用户,任务结束')
@nextchest.args_parser
async def _(session: CommandSession):
    logger.info('[宝箱查询]正则匹配')
    logger.info('[宝箱查询]开始提取字符')
    stripped_arg = re.search('[A-Za-z0-9]+',session.current_arg_text).group()
    if session.is_first_run:
        logger.info('[宝箱查询]用户触发了程序，开始尝试理解')
        if stripped_arg: 
            logger.info('[宝箱查询]用户第一次输入不为空，作为参数传入并执行查询脚本')
            session.state['tag'] = stripped_arg
        return
    if not stripped_arg:
        logger.debug('[宝箱查询]用户没有输入正确的TAG，重新询问')
        session.pause('您的TAG似乎不对，再试试吧',at_sender=True)
        handle_cancellation(session)
    logger.info('[宝箱查询]收到了非空白的用户TAG，转接查询实用程序')
    session.state[session.current_key] = stripped_arg
@on_natural_language(keywords={'宝箱','下一个宝箱','箱子'},only_to_me=True)
async def _(session: NLPSession): 
    return IntentCommand(87.0, 'nextchest',current_arg=session.msg_text)