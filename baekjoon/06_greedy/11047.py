#동전 0

n, w = map(int,input().split())

w_list = []
#n=10 w=4200
count = 0

for i in range(n):
    w_list.append(int(input()))

for i in range(n-1,-1,-1):
    if w==0:
        break
    if w_list[i] > w:
        continue
    count = count+w//w_list[i]
    w %= w_list[i]
print(count)