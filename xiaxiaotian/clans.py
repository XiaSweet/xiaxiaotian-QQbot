from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
import logging
from nonebot.log import logger
import subprocess
@on_command('clans', aliases=('部落查询'),only_to_me=True)
async def clans(session: CommandSession):
    tag = session.get('tag', prompt='请回复您的游戏TAG哦。',at_sender=True,only_to_me=True)
    clans_report = await get_clans(tag)
    if clans == 'ERROR-CR404':
        logger.info('[部落查询]查询完毕，官方无此TAG信息')
        logger.debug('[部落查询]查询脚本执行完毕并返回信息到Nonebot脚本')
        await session.send('出现意外了：\n你想查询的用户被抓到二次元了，请检查一下再重新发送指令查询吧(⊙﹏⊙)',at_sender=True)
    elif clans == 'ERROR-CR400':
        logger.info('[部落查询]出现错误了:官方API查询400,提示详见Debug模式')
        logger.info('[部落查询]你可以前往CR开发者网站查询详情')
        logger.debug('[部落查询]详细信息:没有使用正确的查询地址或官方关闭API了，或许也倒闭了吧( •̀ ω •́ )')
        logger.debug('[部落查询]查询脚本执行完毕并返回信息到Nonebot脚本')
        await session.send('QAQ小管家迷路了，请联系管理员协助修复吧',at_sender=True)
    elif clans == 'ERROR-CRTimeOut':
        logger.info('[部落查询]出现错误了:官方API查询超时,提示详见Debug模式')
        logger.debug('[部落查询]详细信息：查询超时.详见小管家Wiki')
        logger.debug('[部落查询]查询脚本执行完毕并返回信息到Nonebot脚本')
        await session.send('出现意外了：\n因为连接速度太慢所以主动放弃查询了，请您重新使用指令再查询一下吧',at_sender=True)
    elif clans == 'ERROR-CRNotCallMe':
        logger.info('[宝箱查询]用户意外触发或未正常放弃，宝箱查询无效,提示详见Debug模式')
        logger.debug('[宝箱查询]详细信息：包含英文数字以外的其他语言，查询无效.详见小管家Wiki')
        logger.debug('[宝箱查询]查询脚本执行完毕并返回信息到Nonebot脚本')
        await session.send('对不起，你似乎不是来查询用户信息的(。﹏。)',at_sender=True)   
    else:
        await session.send(clans_report,at_sender=True)
        logger.info('[部落查询]结果无错误并已查询完毕并发送给用户,任务结束')
async def get_clans(tag: str) -> str:
    #clans = subprocess.getoutput("python3 lib/clashroyale/clans.py -u '%s'"%(tag))
    #return f'{clans}'
    return f'部落查询功能暂未启用，敬请期待→_→'
@clans.args_parser
async def _(session: CommandSession):
    logger.debug('[部落查询]开始过滤无效字符')
    stripped_arg = session.current_arg_text.replace(' ','')
    stripped_arg = session.current_arg_text.replace('#','')
    if session.is_first_run:
        logger.info('[部落查询]第一次进入程序，开始分析')
        if stripped_arg:
            session.state['tag'] = stripped_arg
            logger.info('[部落查询]用户第一次输入不为空，作为参数传入并执行查询脚本')
        return
    if not stripped_arg:
        logger.info('[部落查询]用户没有输入正确的TAG，重新询问')
        session.pause('您要查询的TAG似乎不对，再试试吧',at_sender=True)
        handle_cancellation(session)
    logger.info('[部落查询]收到了非空白的用户TAG，转接查询实用程序')
    session.state[session.current_key] = stripped_arg
@on_natural_language(keywords={'查用户','Tag查CR','用户'},only_to_me=True)
async def _(session: NLPSession):
    return IntentCommand(80.0, 'clans')