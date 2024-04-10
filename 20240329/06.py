# if-elif-else

score = 72

# 一定互斥
if score >= 90:
    print('A')
# score < 90
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('E')


## -----------------
    
if 70 <= score < 85:
    print('C')

if score < 60:
    print('E')

if 60 <= score < 70:
    print('D')

if score >= 90:
    print('A')

if 80 <= score < 90:
    print('B')
