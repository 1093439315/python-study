a = dict()

keys = ('x', 'y', 'z')
values = (100, -50, None)

for i in range(3):
    key = keys[i]
    value = values[i]
    a[key] = value

print(a)

print(a.keys())
print(a.values())
print(a.items())

print('x', 'x' in a.keys())
print('y', 'y' in a.keys())
print('z', 'z' in a.keys())
print('a', 'a' in a.keys())
print('None', None in a.values())
