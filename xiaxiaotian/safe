from nonebot import on_command, CommandSession
#夏小甜安全卫士组件
#自动拒绝好友申请
@bot.on_request('friend', 'group.invite')
async def _(session: RequestSession):
    # 判断验证信息是否符合要求
    if session.event.comment == '夏小甜卡哇伊(⊙o⊙)哦':
        # 验证信息正确，同意入群
        await session.approve()
        return
    # 验证信息错误，拒绝添加
    await session.reject('自动拒绝好友申请')