a = dict()
b = {'x': 10}
c = {0: 10, 1: 100,'x': 100,
     True: True, False: False,
     'x': 20, 'y': 100}

print(c)
print(c['y'])
print(c.get('z'))
print('get value:' + c.get('z', 'None'))

c['z'] = 230
print(c)
del c['z']

'''
b = [-10, -1, 0, 1, 2, 3, 4]
b.append(5)
b.insert(0, -1)
b.sort()
print(b)
'''
