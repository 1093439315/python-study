score = {'语文': 72,
         '数学': 76,
         '外语': 75}
# 最好 mx
# 最差 mn
# 平均分

# print('Max value:', max(score.values()))
# print('Min value:', min(score.values()))

mx, mn, avg, n = ('', 0), ('', 100), 0, 0

for item, value in score.items():
    print(item, value)
    if value > mx[1]:
        mx = item, value
    if value < mn[1]:
        mn = item, value
    avg += value
    n += 1

print('total:', avg, 'count:', n)
print('avrage:', round(avg / 3))
print(mx, mn)
