# 不可变数据类型(局部元素不可改)
# str, tuple, int, float, bool
# 可变数据类型
# list, dict, set

a = '100'
b = ['1', '0', '0'] # 可变（改）
c = ('1', '0', '0')

print(a[0], b[0], c[0])

b[0] = '0'
print(b)
