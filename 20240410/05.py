# 循环、迭代、遍历
# circle, loop (repeat)
# Pythonic
a = 'hello'
i = 0
running = True
while i < 5 and running: # i 迭代变量
    print(a[i])
    i = i + 1   # 1, 2, 3, 4, 5
    if i > 3:
        # break # 跳出整个循环(包含else)
        running = False
else:
    # not for expression
    print('Fin')

print('Finish')
