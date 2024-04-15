a = ' \t \t Hello\tworld \r \n '
print(a)

print(a.strip().replace('\t', ' '))
print(a.strip('\n'))
