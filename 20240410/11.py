# 解构赋值
'''
# a = 100
# b = 50

a, b, c = 100, 50, 0
#print(a, b, c)

x, y, *z = 10, 200, 300, 4000
#print(x, y, z)

# *k = 1, 2, 3, 4
# print(k)

# print(*args) *不定长

a = (1, 2, 3)
b = (4, 5, 6)
c = a + b
print(c)
#c += [7, 8, 9]
#print(c)

c = (*a, *b)
print(c)
'''

# 变量值的交换

a = (100, 200, 300)
b = [50, 150]
c = True
print(a, b, c)
'''
tmp = a
a = b
b = tmp
print(a, b)
'''

# 赋值=等号右侧永远是字面量
a, b, c = b, c, a
# a, b = [50, 150], (100, 200, 300), True
print(a, b, c)




