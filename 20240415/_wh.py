# 九九乘法表
'''
1
2   2
3   3   3
4   4   4   4
5   5   5   5   5
6   6   6   6   6   6
7   7   7   7   7   7   7
8   8   8   8   8   8   8   8
9   9   9   9   9   9   9   9   9
------------------------------------
1   2   3   4   5   6   7   8   9
'''

for i in range(1, 10):
    for j in range(1, i + 1):
        print(j, 'x', i,
              '=', i * j,
              sep='', end='\t')
    print()
