# 소스코드
1. 
n = int(input())
total = 0
for i in range(n+1):
    total += i
print(total)

2. 
n = int(input())
print(sum(range(1, n+1))) >> range 함수로 반복 가능한 정수 자료형 생성.

# 새로운 개념
1. sum() 함수
  - form:
    sum(x) / sum(x, start)  x: 반복 가능한 정수 자료형(리스트, 튜플, 딕셔너리), start: 처음으로 다시 더해줄 숫자 
    반환: 반복되는 정수를 다 더해 반환하거나 start가 있다면 첫번째 인자 합 + start 반환
