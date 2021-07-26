#최댓값

a = []
#a 리스트 선언

for i in range(0,9):
    a.append(int(input()))
#리스트에 숫자 넣기

max = max(a)
#숫자값들 중 최대값 구하는 함수
print(max)

idx = a.index(max)
print(idx+1)


