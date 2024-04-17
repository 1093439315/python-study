text = '''
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If a the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''.upper()

chars = dict()

for ch in text:
    # print(ch, end='')
    if not ch.isalpha():
        continue
    if ch in chars.keys():
        chars[ch] += 1
    else:
        chars[ch] = 1

print(chars)

#for el in chars.items():
#    print(el)

chs = list(chars.items())
# chs.sort(reverse=True) # 内置方法作用自身

def by2(el):
    return el[1]

a = sorted(chs, key=by2, reverse=True) # 产生新的字面量

# while
i = 0
while i < 3:
    print(a[i][0], a[i][1])
    i += 1

# for-in
i = 0
for ch, cnt in a: # ch, cnt = 'A', 53
    print(ch, cnt)
    i += 1
    if i > 2:
        break







