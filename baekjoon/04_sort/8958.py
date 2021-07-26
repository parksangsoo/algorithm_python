#OX퀴즈

n = int(input())

for i in range(1,n+1):
    a = input()
    score = 0
    count = 0
    for j in range(len(a)):
        if a[j] == "O":
            count = count+1
            score = score+count
        else:
            count = 0
    print(score)