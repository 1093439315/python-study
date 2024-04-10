# for-in
# for-in-else
'''
for 迭代变量 in 序列:
    pass
else:
    pass

a = 'hello'
i = 0
while i < len(a):
    print(a[i])
    i += 1
'''
a = 'hello'
# len(a) ==> 5
for i in range(len(a)): # [0, 1, 2, 3, 4]
    print(a[i])
#else:
#    print('Fin')

for i in a:
    print(i)
