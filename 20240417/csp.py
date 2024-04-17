# 凯撒加密
'''
for i in range(32, 127):
    print(chr(i), end='')
'''
# 元码
OC = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`{|}~'
# 偏移，钥匙码
MK = 15 # 15 - 20
# 偏移码
CM = OC[MK:] + OC[:MK]

org = 'Welcome to my home.'

# 加密
encode = ''
for ch in org.upper():
    if ch in OC:
        index = OC.index(ch)
        encode += CM[index]

print('原文', org)
print('密文', encode)

# 解密
text = ''
for ch in encode:
    if ch in CM:
        index = CM.index(ch)
        text += OC[index]

print('明文', text)
