x, y, z = 100, -50, 0 # 解构赋值

print(1, 'x =', x, 'y =', y)

'''
int x = 100;
int y = -50;
int temp = x;
x = y;
y = temp;


var a = {'a': 10, 'b': 20, 'c': 30}
'''

a = {'a': 10, 'b': 20, 'c': 30}

x, y = y, x
'''
x, y = -50, 100
'''

print(2, 'x =', x, 'y =', y)

