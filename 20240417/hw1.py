'''
十二星座的日期：
水瓶座：1月20日～2月18日
双鱼座：2月19日～3月20日
白羊座：3月21日～4月19日
金牛座：4月20日～5月20日
双子座：5月21日～6月21日
巨蟹座：6月22日～7月22日
狮子座：7月23日～8月22日
处女座：8月23日～9月22日
天秤座：9月23日～10月23日
天蝎座：10月24日～11月22日
射手座：11月23日～12月21日
摩羯座：12月22日～1月19日
'''

zodiac = ('水瓶座', '双鱼座', '白羊座',
          '金牛座', '双子座', '巨蟹座',
          '狮子座', '处女座', '天秤座',
          '天蝎座', '射手座', '摩羯座')
# 7, 1
dates = ((1, 20), (2, 19), (3, 21),
         (4, 20), (5, 21), (6, 22),
         (7, 23), (8, 23), (9, 23),
         (10, 24), (11, 23), (12, 22))

p = input('输入生日(月 日)： ')

# str.split 拆分字符串
lst = p.split()
month, day = tuple(map(int, lst))
print(month, day)

date = month, day

'''
for i in range(11, -1, -1): # 11 ~ 0
    # print(i)
    if date > dates[i]:
        print(zodiac[i])
        break
else:
    print(zodiac[11])
'''

for i in range(12):
    # print(i, date < dates[i])
    if date < dates[i]:
        print(zodiac[i - 1])
        break
else:
    print(zodiac[11])
