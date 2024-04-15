

a = ''
while not a.isdigit():
    a = input('Please enter a number: ')
    if '.' in a:
        a = a[:a.index('.')].strip()
        if len(a) > 0:
            break


print(a, type(a))

n = int(a)
print(n, type(n))
