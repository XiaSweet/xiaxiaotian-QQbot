from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand

help_text = "1.“宝箱查询”请发送[bxh]\n2.“部落战信息”请发送[blzh]\n3.“更新日志”请发送[updatenote] \n4.发送[xxtnote]获取夏小甜手记和其他夏小甜的有关信息\n特殊情况：发送[helpme]获取隐私保护与投诉指引\n"
banbenhao = " By 夏小甜超能力-CR部落辅助Ver:1.0-Python\n"
blog = "夏小甜的秘密基地（内网访问）：https://notes.xiasweet.com"
#宝箱查询帮助
bxcx = "宝箱查询是为了帮助大家了解后续出现的宝箱而制作的小程序 \n食用方法： \n向夏小甜发送[宝箱查询+空格+你的游戏Tag]等待回复即可\n"
bxcxq = "常见问题解答：\n"
bxcxq1 = "1.我发送了指令但是收到一群看不懂的英文？\nF：这种分为2种情况，首先是你的TAG输入有误（例如多加了一个字母或没填写Tag），如果确定Tag没有问题并看到HTTP 404字样那可能是首领端的验证出现的问题。请不要慌张，复制错误信息并私信首领吧OvO\n"
bxcxq2 = "2.为什么每次要输入Tag才能查询?\nF:Tag是皇室战争用于区分用户玩家的唯一识别信息，部落采用了官方的API调取接口，故必须要手动填写查询。\n作为帮助大家解忧的初衷，首领会在后期尝试添加账号绑定服务，这样您就不用一直搜Tag了\n"
hxcxq3 = "3.首领真厉害，能解释一下原理吗？我也想帮助夏小甜。\nF:（这条留言给自己，你们能问这问题才奇怪了）这个程序主要还是自用，基于自然语言Python编程。因为采用了开源框架制作而成，所以使得首领即使自身不是Python高手，也能轻松编译。为了感谢这些开源大佬，这个程序本身也会开源，不过帮助指引只会交给真心愿意帮助维护代码的大佬和部落里的好伙伴了\n详细信息请参阅[xxtnote]查看夏小甜手记吧(≧∇≦)ﾉ"
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
        await session.send("夏小甜的食用指南：\n请回复您想要查询的指令\n"+help_text+banbenhao+blog, ignore_failure=False,at_sender=True)
    except:
        print("send error!")

@on_command('宝箱帮助', aliases=('bxh'))
async def address(session: CommandSession):
    try:
        await session.send(bxcx+bxcxq+bxcxq1+bxcxq2+hxcxq3, ignore_failure=False,at_sender=True)
    except:
        print("bxh send error!")

@on_command('部落战信息', aliases=('bxh'))
async def address(session: CommandSession):
    try:
        await session.send(blzh1+blzh2+blzh3+blzh4+blzh5, ignore_failure=False,at_sender=True)
    except:
        print("blzh send error!")