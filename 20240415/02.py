a = 'Hello world!'
#    012345678901

print('L->R', a.index('o'))

print('R->L', a.rindex('o'))

# in 序列(str, list, tuple, range())
for i in [True, 'Home', 100, None]:
    print(i)


ch = 'w'
if a.count(ch): # 0, 1,.... '' ' '
    print(ch, 'index of a is:', a.index(ch))
else:
    print(ch, 'not in a')

print(ch, 'in a count:', a.count(ch))
