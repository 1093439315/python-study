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
'''.lower()

txt = ''
for ch in text:
    if ch.isalpha():
        txt += ch

lts = set(txt)
print(lts)

data = [] # (53, 'A')

# 遍历集合
for ch in lts:
    #print(ch, txt.count(ch))
    data.append((txt.count(ch), ch))

print(data)

data.sort(reverse=True)
#print(data[:3])

for cnt, ch in data[:3]:
    print(ch, cnt)


