# 凯撒加密

code = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
key = 7
encd = code[key:] + code[:key]
origin = 'Helloworld'.upper()

print(code)
print(encd)

# 加密
encode = ''
for ch in origin:
    if ch in code:
        index = code.index(ch)
        encode += encd[index]

print('原文', origin)
print('密文', encode)

# 解密
text = ''
for ch in encode:
    if ch in encd:
        index = encd.index(ch)
        text += encd[index]

print('明文', origin)
