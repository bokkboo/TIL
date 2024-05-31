# 소스코드
T = int(input())
for i in range(T):
    A, B = map(int, input().split(','))
    print(A+B)

# 설명
1. split 함수 ()안에 ','가 입력 시 ,를 기준으로 입력값을 나눈다는 뜻

2. 반복문 범위 range:
range(a)라면 0부터 a-1까지 이므로 a개, range(1, a+1)라면 1부터 a 까지 이므로 a개. 
a보다 하나 작은 수까지로 생각하고 그 개수만큼 반복한다고 생각.
