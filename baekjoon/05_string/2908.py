#상수

a,b = input().split()

are = int(a[::-1])
bre = int(b[::-1])

if are > bre:
    print(are)
else:
    print(bre)