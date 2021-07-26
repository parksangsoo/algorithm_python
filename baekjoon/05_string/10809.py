#알파벳 찾기

n = int(input())

for i in range(0,n):
    num, a = input().split()
    result = ''
    for i in (0,len(a)):
        result += int(num)*i
    print(result)