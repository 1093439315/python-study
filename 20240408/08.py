# 位操作运算符
'''
<< 左移
>> 右移
'''
'''
a = 100 # 0x64   0x32 = 16 * 3 + 2 = 50
b = a * 16 # = a * (2 ** 4)
c = a << 4
'''
'''
HEX         6    4
BIN      0110 0100  0b01100100
<<1      1100 1000  x2
<<1 0001 1001 0000  x2
<<1 0011 0010 0000  x2
<<1 0110 0100 0000  x2

print(a, b, c)
c = 100 / 4 # 100 >> 2
print('100 >> 2', 100 >> 2)
print('100 >> 3', 100 >> 3)

0110 0100 |
0011 0010 | >> 1 == / 2
0001 1001 | >> 1 == / 2
0000 1100 | >> 1 == / 2
0000 0110 | >> 1 == / 2
0000 0011 | >> 1 == / 2
0000 0001 | >> 1 == / 2
0000 0000 | >> 1 == / 2
'''

# 位逻辑运算符
'''
~ 位逻辑非    真为假，假为真
& 位逻辑与    真真为真，其余为假
| 位逻辑或    有真为真，全假为假
^ 位逻辑异或  相同为假，不同为真
'''
'''
a = 0b00010111 # = 23
b = 0b00001010 # = 10
c = a ^ b
d = c ^ b
'''
'''
      00000010 =  2 (&)
      00011111 = 31 (|)
      00011101 = 29 (^)
      00001010   10
      00010111 = 23 (^)
   1010
   0110
&  0010
|  1110
'''
'''
print('a & b', a & b)
print('a | b', a | b)
print('a ^ b', c) # 异或加密，b为密钥
print('d ^ b', d) # 异或解密，b为密钥
'''
'''
# 加密
s = 'Hello'
k = '$'
key = ord(k)
v1 = ord(s[0]) ^ key
v2 = ord(s[1]) ^ key
v3 = ord(s[2]) ^ key
v4 = ord(s[3]) ^ key
v5 = ord(s[4]) ^ key
t = chr(v1) + chr(v2) + chr(v3) + \
    chr(v4) + chr(v5)

print('origin', s, 'k', k)
print('encode', t)

# 解密
s = 'lAHHK'
k = '$'
key = ord(k)
v1 = ord(s[0]) ^ key
v2 = ord(s[1]) ^ key
v3 = ord(s[2]) ^ key
v4 = ord(s[3]) ^ key
v5 = ord(s[4]) ^ key
t = chr(v1) + chr(v2) + chr(v3) + \
    chr(v4) + chr(v5)

print('encode', s, 'k', k)
print('decode', t)
'''
#加密联系

'''
a = '717'
b = 'A'
key = ord(b)
v1 = ord(a[0]) ^ key
v2 = ord(a[1]) ^ key
v3 = ord(a[2]) ^ key
t = chr(v1) + chr(v2) + chr(v3)
print('加密文件',a )
print('密钥' ,b)
print('加密结果',t)

print('解密')
z1 = ord(t[0]) ^ key
z2 = ord(t[1]) ^ key
z3 = ord(t[2]) ^ key
y = chr(z1) + chr(z2) + chr(z3) 
print(' 解密结果',y)
'''


'''
# 十进制转换为二进制
a = 717
print(bin(a))
'''
'''
a = 717
a = bin(a)
b = 0xA
b = bin(b)
key = b
t = a ^ key
print('加密文件',a )
print('密钥' ,key)
print('加密结果',t)

print('解密')
y = t ^ key
print(' 解密结果',y)
'''
a = 717
a = bin(a)
b = 0xA
b = bin(b)
key = b

print(a , b , key)

x = 0b1011001101
y = 0b1010
Y = x ^ y
print(Y)
z = Y ^ y
print(z)

#a, b 表示的都是二进制，为什么不能加密（or怎么将其表示为字符串）
