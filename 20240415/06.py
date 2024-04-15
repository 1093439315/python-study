'''a = 'fghtesgtbADDSAC'
b = '3464342365264326'
print(a.isalpha())
print(b.isdigit())

print(1, '0123456789'.isnumeric())
print(2, '〇一二三四五六七八九十'.isnumeric())
print(3, '零壹贰叁柒捌玖百千万亿'.isnumeric())
print(4, '¼½¾'.isnumeric())
# chr(188) ¼
# chr(189) ½
# chr(190) ¾
print(5, '  \t\n\r\v'.isspace())
print(6, '4635fdsbvtnytny'.isalnum())
print(7, 'Hello World'.istitle()) # 分词
'''

a = 'Hello World, Welcome to My Home'
# print(a.replace(' ', '\n', 2))

b = a.replace(' ', '\n') \
     .replace(',', '') \
     .replace('H', 'A')
print(b)
