#블랙잭

n,r = map(int,input().split())
list = list(map(int, input().split()))
result = 0

for i in range(0,n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if list[i] + list[j] + list[k] > r:
                continue
            else:
                result = max(result, list[i] + list[j] + list[k])

print(result)