# 百元百物
'''
手里100元，买100件，商品：
1、茶杯 5 元 1 只
2、调羹 3 元 1 只
3、杯垫 1 元 3 只
问：买了几个茶杯、几个调羹和几个杯垫？

分析：
茶杯 x 最多买20个
调羹 y 最多买33个
杯垫 z = 100 - x - y

查找符合条件的 x, y 和 z:
x * 5 + y * 3 + (100 - x - y) / 3 = 100
'''

step = 0

for x in range(1, 20):
    step += 1
    for y in range(1, 33):
        step += 1
        z = 100 - x - y
        # 注意：z 一定要是 3 的倍数
        if z % 3: # 相当于 z % 3 != 0
            # 取得的余数不是 0，表达式为真
            continue # 继续找...
        # print(x, y, z)
        step += 1
        qx = x * 5   # 茶杯钱
        qy = y * 3   # 调羹钱
        qz = z // 3  # 杯垫钱, z//3速度比z/3更快
        if qx + qy + qz == 100:
            print(x, y, z)


print('step =', step)
