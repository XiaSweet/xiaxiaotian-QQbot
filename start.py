import nonebot
import config
from os import path

if __name__ == '__main__':
    nonebot.init(config)
    nonebot.load_builtin_plugins()
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'xiaxiaotian'),
        'xiaxiaotian'
    )
    nonebot.run(host='0.0.0.0', port=8080)
