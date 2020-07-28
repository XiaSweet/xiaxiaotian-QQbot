from nonebot.default_config import *
from datetime import timedelta

#欢迎进入夏小甜De配置文件夹
#以下信息为设置小管家的专属文件，如果不清楚设置的内容则不建议精简本行注释代码
#NONEBOT基础设置
SUPERUSERS = {1172608638}
COMMAND_START = {'', '/', '!', '／', '！'}
#小管家昵称
NICKNAME = {'小管家', '夏小甜'}
SESSION_RUN_TIMEOUT = timedelta(seconds=10)
DEFAULT_VALIDATION_FAILURE_EXPRESSION = '你发送的内容格式不太对呢，请检查一下再发送哦～'
DEBUG = False
#腾讯AI-API段鉴权配置
TXAI_APP_ID = '2128916170'
TXAI_APP_KEY = 'mSTstLFLxSdO6SRp'
#配置文件结束

