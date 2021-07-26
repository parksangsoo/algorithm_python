#평균의 넘겠지

n = int(input())

for i in range(n):
    m = list(map(int,input().split()))
    avg = (sum(m)-m[0])/m[0]
    count = 0
    for j in range(1,m[0]+1):
        if m[j] > avg:
            count = count + 1

    per = (count/m[0])*100
    print('%.3f' %per + '%')
