import re

str = 'movej([-3.45182449022402, -3.137806240712301, -1.3714802900897425, -0.5598643461810511, 1.689890742301941, 1.1276788711547852], a=1.0, v=1.0)'

pattern_type = r'(\s)*(movej|movep|movej){1}'
m1 = re.match(pattern_type, str)
print(m1.group())
print(m1.start())
print(m1.end())
print(m1.span())
motion_type = m1.group()
print('motion type: %s' % motion_type)

pattern_pos = r'\[[-+.,\d\s]*\]'
m2 = re.search(pattern_pos, str)
pos = eval(m2.group())
print('pos:%s' % pos)

'''
(?:exp) -- 匹配exp但是不捕获匹配的文本
(?P<name>exp) -- 匹配exp并捕获到名为name的组中
(exp) -- 匹配exp并捕获到自动命名的组中
'''
acc_pattern = r'a(?:\s)*\=(?:\s)*(?P<acc>[\d.]*),'
m3 = re.search(acc_pattern, str)
acc = eval(m3.group('acc'))
print('acc:%s' % acc)

vel_pattern = r'v(?:\s)*\=(?:\s)*(?P<vel>[\d.]*)'
m4 = re.search(vel_pattern, str)
vel = eval(m4.group('vel'))
print('vel:%s' % vel)
