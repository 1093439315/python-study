# 字面量, 变量（字面量的标签）
#print('Hello world')
#print(1, 20, 300)

# Python 里面变量是大小写敏感的
# 赋值的等号=左边永远是变量，右边永远是字面量
a = 10
b = 10

print('a == b', a == b) # 值相等判断 ==
# 布尔值 True, False

print('id(a) == id(b)', id(a) == id(b))
# id() 查询变量对应字面量内存地址的函数
print('a is b', a is b)

c = '''hello world'''
# 字符串的界定符 'a' "a" '''a''' """a"""
d = """hello world"""
print('c is d', c is d)


e = True
f = 1
print('e == f', e == f)
print('e is f', e is f)




