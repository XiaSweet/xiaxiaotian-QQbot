from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
import subprocess
import logging
from nonebot.log import logger
@on_command('achat',aliases=('一言'),only_to_me=True)
async def achat(session: CommandSession):
    logger.info('[一言]用户激活指令开始运行')
    logger.debug('[一言]向编译库发送请求获取信息')
    achat_report = await get_achat_of_chat()
    logger.info('[一言]向用户发送运行结果，任务结束')
    await session.send(achat_report,at_sender=True)
async def get_achat_of_chat() -> str:
    onechat = subprocess.getoutput("python3 lib/yiyan/aword.py")
    return f'{onechat}'
@on_natural_language(keywords={'一言','每日一言'})
async def _(session: NLPSession):
    return IntentCommand(70.0, 'achat')