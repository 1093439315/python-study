# 演示代码：进度和进度条
'''
  0%  [................................]
 50%  [#################...............]
100%  [################################]
'''
import tkinter
import time

for i in range(101):
    p = i // 2
    c = '#' * p
    b = '.' * (50 - p)
    if i < 10:
        s = '  '
    elif i < 100:
        s = ' '
    else:
        s = ''
    print(s, i, '%  [', c, b, ']', sep='', end='\r')
    time.sleep(0.05)
