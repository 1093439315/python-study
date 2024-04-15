a = [-1, 0, 1]

a.append(10)
a += [100]

a.insert(0, 555)

print(a)

b = a.pop(0)

print(a, b)

ch = -1
if ch in a:
    #a.remove(ch)
    del a[a.index(ch)]

print(a, b)
