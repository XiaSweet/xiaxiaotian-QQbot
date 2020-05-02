#加载基础组件
import subprocess
#注意：用户的输入Tag在这里的变量是'tag'

async def get_nextchest_of_tag(tag: str) -> str:

    # subprocess.getoutput是用于执行脚本并输出结果的
    users = subprocess.getoutput("python3 lib/clashroyale/chests.py -u %s"%(tag))
    # 向用户返回的信息（这里是脚本内容）
    return f'{users}'
