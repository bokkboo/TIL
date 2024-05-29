# 소스코드
T = int(input())
for i in range(T):
    A,B = map(int, input().split())
    print(A+B)

# 새 개념
1. map()함수
  - 역할: 함수와 반복 가능한 데이터를 입력 받아 입력 받은 각 요소를 함수에 적용시킨 값을 리턴해줌
  - form: map(함수, 반복 가능한 데이터)
  - 주의: map함수는 결과값을 map객체로 리턴하므로 리스트로 출력하려면 앞에 list를 붙여준다. ex) list(map(int, [1, 2, 3]))
