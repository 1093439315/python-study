a = 1000
b = 123.456
c = 'Hello world'


# print('{}  {}  {}'.format(a, b, c))
# print('{0:b}  {0:06d}  {0:,.2f}'.format(a))

# d = bin(a)
e = '{0:b}  {0:o}  {0:X}'.format(a) # b: Binary
# print(e)

#print('%30s' % (c))
#print('{0:<30}\n{0:>30}\n{0:^30}'.format(c))

# print(c.center(len(c) + 2, ' ').center(30, '*'))

#print(f'{"Hello world, Welcome":^30}')
#print(f'{c:<30}\n{c:>30}\n{c:^30}')

from datetime import datetime as dt

today = dt.today()
#print(today.hour, today.minute, today.second)
text = f'{today.hour:02}:{today.minute:02}:{today.second:02}'
print(text)

