# range() 等差序列发生器 generator
# 可数的 iterable 可迭代的
# range(start, end, step) = sequence[start, end-step]
# step = 1: range(start, end)
# start = 0: range(end)
a = range(10)
print(a, type(a))

print(list(a))
print(tuple(a))


# [1, 3, 5, 7, 9]
print(list(range(1, 10, 2)))
