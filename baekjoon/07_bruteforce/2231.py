# 분해합

n = int(input())
# n = 216
result = 0
for i in range(1, n+1):
    A = list(map(int, str(i)))
    result = i + sum(A)
    if result == n:
        print(i)
        break
    if i == n:
        print(0)


