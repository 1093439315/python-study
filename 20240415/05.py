# 不可变数据类型的内置方法不会影响自身
a = 'Hello'
c = a.upper()
print(c)
print(a)

# 可变数据类型的内置方法几乎都是影响自身的
b = [3, 2, 1]
b.sort()
print(b)

