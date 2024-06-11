# 소스코드
n = int(input())
num = list(map(int, input().split()))
max = num[0]
min = num[0]

for i in range(1, n):
    if num[i] > max:
        max = num[i]
    elif num[i] < min:
        min = num[i]
        
print(min, max)


# 주의
1. 1번째 배열부터 n-1번째 배열까지 비교하는 범위는 range 함수 상 (1, n)으로 표현 됨.
2. 배열을 num[1]식으로 써도 
