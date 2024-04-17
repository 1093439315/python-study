# 集合 set
# 无次序，元素（值）唯一
'''
a = 'hello world'
b = set(a)

print(a)
print(b)
'''

a = {1, 2, 3, 4, 5}
b = {5, 6, 7, 8, 9}

print('a | b', a | b)
print('a & b', a & b)

print('a - b', a - b)
print('b - a', b - a)

print(1, a ^ b)
print(2, (a | b) - (a & b))
print(3, (a - b) | (b - a))
