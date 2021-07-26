#다이얼

number = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
a = input()

sum = 0
for i in range(0,len(a)):
    for j in number:
        if a[i] in j:
            sum = sum + number.index(j) + 3

print(sum)
