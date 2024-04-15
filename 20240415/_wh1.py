'''
0   *    2 1 () n - i
1  ***   1 3
....
n *****  0 5 (*) n * 2 + 1
'''
n = 7

for i in range(n):
    #for j in range(i * 2 + 1):
    #    print('*', end='')
    print(' ' * (n - i - 1), end='')
    print('*' * (i * 2 + 1))
