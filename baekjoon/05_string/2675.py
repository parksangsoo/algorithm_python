#문자열 반복

n1 = int(input())

for i in range(0,n1):
    n2, string = input().split()
    text = ''
    for j in string:
        text += int(n2)*j
    print(text)