import re
test = '测试信息 #sdsada566'
test1 = '帮我查村#dfsf434234的宝箱'
test2 = '不玩那个 #weqwe44 宝箱'
print('test')
print (re.search('[A-Za-z0-9]+',test).group())
print('test1')
print (re.search('[A-Za-z0-9]+',test1))
print('test2')
print (re.search('[A-Za-z0-9]+',test2))
