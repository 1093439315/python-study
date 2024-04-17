# ** <==> dict key-value

a = {'x': 100}
b = {'y': 60, 'z': -10}

c = {**a, **b} # 字典的合并 **键值对
print(c)

