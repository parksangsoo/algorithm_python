#ATM

n = int(input())
# n =5
m = list(map(int, input().split()))
# m = 3 1 4 3 2

m.sort()
sum = 0
num = 0
for i in m:
    sum = sum + i
    num = num + sum
print(num)