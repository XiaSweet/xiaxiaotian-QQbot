from nonebot.default_config import *
from datetime import timedelta

SUPERUSERS = {1172608638}
COMMAND_START = {'', '/', '!', '／', '！'}
NICKNAME = {'小管家', '夏小甜'}
SESSION_RUNNING_EXPRESSION = '别着急，过会喊我嘛，我的脑袋不好使QAQ'
SESSION_CANCEL_EXPRESSION = (
    '好的',
    '收到ovo',
    '好吧，那就不打扰啦╭(╯^╰)╮',
    '那夏小甜先不打扰你啦。',
)
SESSION_RUN_TIMEOUT = timedelta(seconds=10)
DEFAULT_VALIDATION_FAILURE_EXPRESSION = '你发送的内容格式不太对呢，请检查一下再发送哦～'
DEBUG = False