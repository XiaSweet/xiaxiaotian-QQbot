# 夏小甜 -CR宝箱查询插件

一个使用Python简单查询游戏“皇室战争”的宝箱QQ机器人。以“夏小甜”为核心已经部署在CR部落"皇家.部落"的QQ群内。基于CoolQ机器人Nonebot组件制作 

## 配置要求

您的设备只需满足一下要求即可运行这个插件：
操作系统: 
Linux（Debian 8/CentOS 7 均可，必须能够运行最新版Docker） 或 Windows  7 Service Pack 1 以上
内存：
作者在CentOS 7 的环境中实际测试在1 GB内存中已经可以达到很好的效果，推荐最少2 GB内存或更高。
基础依赖及目的：
CoolQ：最新版(QQ机器人基础软件,Linux下可以使用其官方提供的脚本）
CoolQ-HTTP-API：v4.15.0+(用于CoolQ与下面的程序交互)
NoneBot框架: v1.6.0+（用于与夏小甜查询插件交互）
Python: V3.7+ （用于保证Nonebot可以运行以及查询插件的使用）
根据您的操作系统可能还需要一下组件:
Docker(**仅LINUX**): 最新版  （用于兼容CoolQ软件的运行）


## 使用方法

1. 在CoolQ中启用 CoolQ-HTTP-API 插件。
2. 使用PiP3安装 NoneBot 最新版。
 Linux:`pip3 install nonebot`
3. Git Clone查询插件最新版到你的电脑，然后配置你的 CoolQ-HTTP-API 插件与夏小甜机器人连接并使用`echo`指令测试是否连接成功。
4. 进入"皇室战争"游戏的官方[开发者](https://developer.clashroyale.com/ "开发者")页面申请一个查询API。
5. 将你申请的API填入到"夏小甜的插件目录/xiaxiaotian/super/clashroyale/mykey.txt"中
6. 向你的机器人发送“宝箱查询+空格+你要查询宝箱的用户名TAG”，如果运行正常的话稍后你便会收到机器人发送给你的宝箱查询信息啦(。・∀・)ノ

## 最后的话
这个小插件的诞生离不开其他开源的开发者，正是因为它们才会有夏小甜查询小插件的今天。虽然不知道以后什么时候会弃坑，但是作为对开源社区的回报，这个插件会一直处于开源状态，如果您有什么好的想法可以直接上传分支(⊙o⊙)哦

## 小广告
玩皇室战争的小伙伴可以来我们的部落“皇家.部落”来玩玩哦，这里是一个可以聊天的好地方\(^o^)/~
