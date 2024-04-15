a = 200
b = 1234.567
c = 'Hello world'

'''
for i in range(105, 120):
    d = 'AX%05d' % (i) # 中间的 % 连接符
    print(d)
'''

# print('%06.0f   %06.2f' % (b, b))
print('%e   %E' % (33041, 33041))
print(0.01, 0.0001, 0.000001)
'''
k = '计算机' # 字符串是 utf-8 编码 >=v3.8
l = bytes(k, encoding='utf-8')
n = str(l, encoding='utf-8')
print(l)
print(n)
#j = b'\x8111' # byte-string 字节字符串
'''
