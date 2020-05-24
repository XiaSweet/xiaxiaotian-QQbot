from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
import time
#填写版本号，算是我微小的请求啦\(^o^)/~
ver = "1.4.3-alpha"
year = time.strftime("%Y", time.localtime()) 

help_text = "1.“帮助信息”请发送[bxh]\n2.“部落战信息”请发送[blzh]\n3.发送[helpme]获取隐私保护与投诉指引\n"
banbenhao = "\n版本信息:\n夏小甜 - CR辅助机器人\n版本号:%s\n"%(ver)
blog = "友情感谢:\n秘密基地(仅限内网)：https://notes.xiasweet.com \n夏小甜的Github:https://github.com/XiaSweet/xiaxiaotian-searchCRlog \n以及所有皇室战争“皇家.部落”里的所有提出建议的伙伴（*＾-＾*）\n"
gpl = "温馨提示：夏小甜使用AGPL3.0协议，您可以在无偿开放修改的源代码并注明作者的情况下自由的修改源码。\n2019-%s By XiaSweet Lab  纪念每一位部落的小伙伴OvO"%(year)
#宝箱查询帮助
bxcx = "宝箱查询是为了帮助大家了解后续出现的宝箱而制作的小程序 \n食用方法： \n向夏小甜发送[宝箱查询+空格+你的游戏Tag]等待回复即可\n"
bxcxq = "常见问题解答：\n"
bxcxq1 = "1.我发送了指令但是收到一群看不懂的英文？\nF：这种分为2种情况，首先是你的TAG输入有误（例如多加了一个字母或没填写Tag），如果确定Tag没有问题并看到HTTP 404字样那可能是首领端的验证出现的问题。请不要慌张，复制错误信息并私信首领吧OvO\n"
bxcxq2 = "2.为什么每次要输入Tag才能查询?\nF:Tag是皇室战争用于区分用户玩家的唯一识别信息，部落采用了官方的API调取接口，故必须要手动填写查询。\n作为帮助大家解忧的初衷，首领会在后期尝试添加账号绑定服务，这样您就不用一直搜Tag了\n"
hxcxq3 = "3.如果您"
#部落战信息”
blzh1 = "这个小程序目前使用非常简单，需要输入部落TAG\n"
blzh2 = "食用方法：\n"
blzh3 = "发送部落战排名+空格+你的要查询部落TAG"
blzh4 = "常见问题解答：\n"
blzh5 = "我可以直接发送部落战查询来查询部落的信息吗？Tag太麻烦了\nF:这项功能只是测试功能，在进行账号绑定操作后才能使用，敬请谅解（还没有上线呢qaq）"

@on_natural_language(keywords={'帮助'})
async def _(session: NLPSession):
    stripped_msg = session.msg_text.strip()
    return IntentCommand(90.0, '帮助', current_arg='')

@on_command('帮助', aliases=('帮助','help','指令帮助' ))
async def address(session: CommandSession):
    try:
        await session.send("夏小甜的食用指南：\n请回复您想要查询的指令\n"+help_text+banbenhao+blog+gpl, ignore_failure=False,at_sender=True)
    except:
        print("send error!")

@on_command('宝箱帮助', aliases=('bxh'))
async def address(session: CommandSession):
    try:
        await session.send(bxcx, ignore_failure=False,at_sender=True)
    except:
        print("bxh send error!")

@on_command('部落战信息', aliases=('blzh'))
async def address(session: CommandSession):
    try:
        await session.send(blzh1+blzh2+blzh3+blzh4+blzh5, ignore_failure=False,at_sender=True)
    except:
        print("blzh send error!")