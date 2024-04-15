'''
1. 车牌6位, 前2位大写字母, 后4位数字
2. 允许出行: 一三五单数, 二四六双数, 周日全部
假定：今天是周一，判断车牌是否能通行
'''
today = int(input('今天是周几（0周日，1~6）？ '))
car_num = input('输入车牌号（XX8888）： ')

p2 = car_num[:2]  # 前2位
p4 = car_num[-4:] # 后4位

if len(car_num) == 6 and \
   p2.isalpha() and p2 == p2.upper() and \
   p4.isdigit():
    tail = int(car_num[-1])

    if today == 0 or \
       (tail + today) % 2 == 0:
        print('PASSED')
    else:
        print('NO')
else:
    print('非法车牌')
