a = 100
b = 100
# 字面量全局唯一
# 变量赋值其实是给字面量贴标签
# 变量赋值，等号的左边必须是变量名，
# 等号的右侧必定是字面量
print(1, a == b) # == 判断值相等
print(2, a is b) # 对象（变量）相等
print('a:', id(a))
print('b:', id(b))
# 字面量
# charactor/char  byte 字节
# 界定符
# str: 'a' "b" '''c''' """d"""
# list: []
# tuple: ()
# dict: {}
'''
0000 0000 比特 8 bits = 1 Byte

200MBits = 200 / 8 = 25 MBytes
45 MBytes

1000 B = 1 KB
1000 K = 1 M
1000 M = 1 G
1000 G = 1 T

8 2^3
1024 B = 1 K
1024 K = 1 M
1024 M = 1 G
1024 G = 1 T

128 G = 128 * 1.024 * 1.024 * 1.024 
'''
