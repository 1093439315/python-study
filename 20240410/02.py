# 序列的通用方法
# Expression: 变量 字面量 计算式 合法语句
'''
.index(el)
.rindex(el) # reverse 相反
.count(el)
[]
'''

#    01234567890
a = 'Hello world'

# 测试（判断）序列中是否存在元素
# el in str
print('o →', a.index('o'))
print('o ←', a.rindex('o'))

if 'a' in a:
    print('a', a.index('a'))
else:
    print('Not found char a')

print('...')

print('∑(o)', a.count('o'))
print('∑(a)', a.count('a'))
