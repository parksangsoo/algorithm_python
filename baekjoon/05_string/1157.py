#단어 공부

s = input().upper()
s2 = list(set(s))
n = []

for i in s2:
    count = s.count(i)
    n.append(count)

if n.count(max(n)) >= 2:
    print("?")
else:
    print(s2[n.index(max(n))])