a = 'hEllO wOrld'

print(a.upper())
print(a.lower())
print(a.title())
print(a.capitalize())
print(a.swapcase())


username = 'alice'
password = '123456'

user = ''
pswd = ''
while username != user.lower() or \
      password != pswd:
    user = input('请输入用户名：')
    pswd = input('请输入密码：')

print('Login successful!')


