#평균

n = int(input())
sl = list(map(int,input().split()))
Max = max(sl)
sum = 0
for i in range(n):
    a = sl[i]/Max*100
    sum = sum + a

avg = sum/n
print(avg)


