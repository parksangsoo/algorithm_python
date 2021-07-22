#사분면 고르기

A = int(input())
B = int(input())

if A > 0:
    if B > 0:
        print(1)
    elif B < 0:
        print(4)
elif A < 0:
    if B > 0:
        print(2)
    elif B < 0:
        print(3)