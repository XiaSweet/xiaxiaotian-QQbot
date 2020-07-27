import subprocess
import logging
from nonebot.log import logger
async def get_nextchest_of_tag(tag: str) -> str:
    chest = subprocess.getoutput("python3 lib/clashroyale/chests.py -u '%s'"%(tag))
    if chest == 'ERROR-CR404':
        logger.info('[宝箱查询]查询完毕，官方无此TAG信息')
        logger.debug('[宝箱查询]查询脚本执行完毕并返回信息到Nonebot脚本')
        return f'出现意外了：\n你想查询的用户被抓到二次元了，请检查一下再重新发送指令查询吧(⊙﹏⊙)'
    elif chest == 'ERROR-CR400':
        logger.info('[宝箱查询]出现错误了:官方API查询400,提示详见Debug模式')
        logger.info('[宝箱查询]你可以前往CR开发者网站查询详情')
        logger.debug('[宝箱查询]详细信息:没有使用正确的查询地址或官方关闭API了，或许也倒闭了吧( •̀ ω •́ )')
        logger.debug('[宝箱查询]查询脚本执行完毕并返回信息到Nonebot脚本')
        return f'QAQ小管家迷路了，请联系管理员协助修复吧'
    elif chest == 'ERROR-CR403':
        logger.info('[宝箱查询]出现错误了:官方API查询403,提示详见Debug模式')
        logger.debug('[宝箱查询]详细信息：查询Key不正确，通常是公网IP地址变更导致的失效情况在家用宽带中较常见.详见小管家Wiki')
        logger.debug('[宝箱查询]查询脚本执行完毕并返回信息到Nonebot脚本')
        return f'登录失败，暂时无法查询宝箱，请联系管理员协助吧'    
    elif chest == 'ERROR-CRTimeOut':
        logger.info('[宝箱查询]出现错误了:官方API查询超时,提示详见Debug模式')
        logger.debug('[宝箱查询]详细信息：查询超时.详见小管家Wiki')
        logger.debug('[宝箱查询]查询脚本执行完毕并返回信息到Nonebot脚本')
        return f'出现意外了：\n因为连接速度太慢所以主动放弃查询了，请您重新使用指令再查询一下吧' 
    elif chest == 'ERROR-CRNotCallMe':
        logger.info('[宝箱查询]用户意外触发或未正常放弃，宝箱查询无效,提示详见Debug模式')
        logger.debug('[宝箱查询]详细信息：包含英文数字以外的其他语言，查询无效.详见小管家Wiki')
        logger.debug('[宝箱查询]查询脚本执行完毕并返回信息到Nonebot脚本')
        return f'对不起，你似乎不是来查询宝箱的(。﹏。)'         
    else:
        return f'{chest}'