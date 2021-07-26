#나머지


n = []
for i in range(0,10):
    a = int(input())
    n.append(a%42)

n = set(n)
print(len(n))
