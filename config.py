from nonebot.default_config import *
from datetime import timedelta
#欢迎进入夏小甜De配置文件夹
#以下信息为设置小管家的专属文件，如果不清楚设置的内容则不建议精简本行注释代码
#NONEBOT基础设置
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
#小管家自有模块配置
#腾讯闲聊不知道如何回答的情况安排智库，将会在以下内容内随机挑选一个
TXCHAT_NOANSWER = (
    '你的问题好像有些为难我哦。请换个话题聊聊吧◑﹏◐',
    '问这么深奥的问题你是故意的吧？',
    '我还小，你不能问这么深奥的问题在欺负我╭(╯^╰)╮',
    '啦啦啦，我是无情的小管家。我听不见你说话啦啦啦(ˉ﹃ˉ)',
    '我还不太明白你在说什么呢，没关系，以后的我会变得更强呢！',
    '？？？，我想跟你聊些简单的话题',
    '其实我不太明白你的意思……',
    '抱歉哦，我现在的能力还不能明白你在说什么，但我会加油的～',
    '本管家现在不想理你，不接受质疑(︶︿︶)╭∩╮',
)
#腾讯AI-API段鉴权配置
TXAI_APP_ID = '2128916170'
TXAI_APP_KEY = 'mSTstLFLxSdO6SRp'

#配置文件结束