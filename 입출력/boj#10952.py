# 소스코드
while True:
    A, B = map(int, input().split())
    if (A == 0) and (B == 0):
        break
    else:
        print(A+B)

# 설명:
A,B에 값을 입력 받다가 입력값이 모두 0이면 반복을 멈춰야 하므로 if문 사용해 0 0이 나오면 break를 사용해 빠져나오게 설정
다른 경우는 입력값의 합 출력
