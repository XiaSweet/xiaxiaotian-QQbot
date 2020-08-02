from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
import logging
from nonebot.log import logger
import subprocess
from nonebot.helpers import render_expression as expr
import sys
sys.path.append("lib/smartxxt")
import systemre as e
@on_command('nojuan', aliases=('伸手党查询'),only_to_me=True)
async def nojuan(session: CommandSession):
    tag = session.get('tag')
    await session.send(expr(e.SYSTEM_WAITING))
    nojuan_report = await get_nojuan(tag)
    if nojuan == 'ERROR-CR404':
        logger.info('[伸手党查询]查询完毕，官方无此TAG信息')
        logger.debug('[伸手党查询]查询脚本执行完毕并返回信息到Nonebot脚本')
        logger.info('[伸手党查询]任务处理完成')
        await session.send('出现意外了：\n你想查询的用户被抓到二次元了，请检查一下再重新发送指令查询吧(⊙﹏⊙)',at_sender=True)
    elif nojuan == 'ERROR-CR400':
        logger.info('[伸手党查询]出现错误了:官方API查询400,提示详见Debug模式')
        logger.info('[伸手党查询]你可以前往CR开发者网站查询详情')
        logger.debug('[伸手党查询]详细信息:没有使用正确的查询地址或官方关闭API了，或许也倒闭了吧( •̀ ω •́ )')
        logger.debug('[伸手党查询]查询脚本执行完毕并返回信息到Nonebot脚本')
        logger.info('[伸手党查询]任务处理完成')
        await session.send('QAQ小管家迷路了，请联系管理员协助修复吧',at_sender=True)
    elif nojuan == 'ERROR-CRTimeOut':
        logger.info('[伸手党查询]出现错误了:官方API查询超时,提示详见Debug模式')
        logger.debug('[伸手党查询]详细信息：查询超时.详见小管家Wiki')
        logger.debug('[伸手党查询]查询脚本执行完毕并返回信息到Nonebot脚本')
        logger.info('[伸手党查询]任务处理完成')
        await session.send('出现意外了：\n因为连接速度太慢所以主动放弃查询了，请您重新使用指令再查询一下吧',at_sender=True)
    elif nojuan == 'ERROR-CRNotCallMe':
        logger.info('[伸手党查询]用户意外触发或未正常放弃，查询无效,提示详见Debug模式')
        logger.debug('[伸手党查询]详细信息：包含英文数字以外的其他语言，查询无效.详见小管家Wiki')
        logger.debug('[伸手党查询]查询脚本执行完毕并返回信息到Nonebot脚本')
        logger.info('[伸手党查询]任务处理完成')
        await session.send('对不起，你似乎不是来查询信息的(。﹏。)',at_sender=True) 
    elif nojuan == 'ERROR-CRNotMyClans':
        logger.info('[伸手党查询]用户并不在皇家部落内，拒绝查询并回复用户，提示详见Debug模式')
        logger.debug('[伸手党查询]详细信息：用户并不在皇家部落内，主动放弃查询.详见小管家Wiki')
        logger.debug('[伸手党查询]查询脚本执行完毕并返回信息到Nonebot脚本')
        logger.info('[伸手党查询]任务处理完成')
        await session.send('本服务仅对部落内的小伙伴所开放哦，Sorry。QAQ',at_sender=True) 
    else:
        await session.send(nojuan_report,at_sender=True)
        logger.info('[伸手党查询]结果无错误并已查询完毕并发送给用户,任务结束')
async def get_nojuan(tag: str) -> str:
    nojuan = subprocess.getoutput("python3 lib/clashroyale/donationcard/nojuan.py -c '%s'"%(tag))
    return f'{nojuan}'
    #return f'0捐测试功能触发完毕'
@nojuan.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text
    logger.debug('[伸手党查询]开始辨别部落代码') 
    if stripped_arg.find('大部落' and '全部') > -1:
            logger.info('[伸手党查询]用户查询大部落全部的伸手党成员，作为参数传入并执行查询脚本')
            session.state['tag'] = 'dbl'
    elif stripped_arg.find('小部落' and '全部') > -1:
            logger.info('[伸手党查询]用户查询小部落全部的伸手党成员，作为参数传入并执行查询脚本') 
            session.state['tag'] = 'xbl'
    elif f'大部落' in  stripped_arg:
            logger.info('[伸手党查询]用户查询大部落0捐成员，作为参数传入并执行查询脚本')
            session.state['tag'] = 'dbl0'
    elif f'小部落' in  stripped_arg:
            logger.info('[伸手党查询]用户查询小部落0捐成员，作为参数传入并执行查询脚本') 
            session.state['tag'] = 'xbl0'
    elif f'同好会' in  stripped_arg:
            logger.info('[伸手党查询]用户查询同好会信息，取消指令')
            session.finish('很抱歉，同好会暂未开放，无法查询，敬请谅解(ノへ￣、)')
    elif not session.is_first_run:
                logger.debug('[伸手党查询]用户二次查询无结果，征求用户意见')
                if stripped_arg.find(f'嗯' or f'是' or f'继续' or f'还不' or '可以' or f'需要' or f'好') > -1 :
                    logger.debug('[伸手党查询]用户希望继续查询，重置指令')
                    session.pause('请告诉我你想查询的部落等我消息吧')                    
                else:
                    logger.info('[伸手党查询]用户放弃查询，取消指令')
                    session.finish('你还是想好再来找我查询伸手党吧(⊙ω⊙)') 
    else:
            logger.debug('[伸手党查询]一次查找无结果，重新查询中')
            session.pause('您想要查询什么部落的伸手党？\n可用参数：大部落、小部落、同好会')


@on_natural_language(keywords={'伸手党','0捐','闲鱼榜'},only_to_me=True)
async def _(session: NLPSession):
    # 去掉消息首尾的空白符
    stripped_msg = session.msg_text.replace(' ','')
    stripped_msg = session.msg_text.replace('#','')
    return IntentCommand(81, 'nojuan',current_arg=stripped_msg)