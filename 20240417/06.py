'''
a = [1, 2, 3]
b = [4, 5, 6]

c = a + b # [1, 2, 3, 4, 5, 6]
print(c)

d = [*a, *b] # *去除[]
print(d)
'''
a, b, *c = 100, 50, 10, 0, -1 # * 垃圾收集
print(a, b, c)

a = (0, 100, 50, 0, -1, 200)
#        x    z          y
print(a)

x, y, z = a[1], a[-1], a[2]
print(x, y, z)

_, x, z, *_, y = a
print(x, y, z)

'''
d = 'hello '
e = 'world'
f = d + e
print(f)
'''
