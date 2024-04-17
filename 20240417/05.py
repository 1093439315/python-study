a = {1, 3, 5, 6, 7, 9, 0}

a.add(2)

print(a)

print(a.pop())
print(a.pop())

print(a)

a.remove(9)

print(a)

if 8 in a:
    a.remove(8)

print(1, a.discard(7))

print(a)

print(2, a.discard(8))
