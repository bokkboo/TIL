# 소스코드
a = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
b = [31,28,31,30,31,30,31,31,30,31,30,31]
total = 0
x, y = map(int, input().split())
for i in range(x-1):
    total += b[i]
week = (total+y) % 7
print(a[week])

# 설명
- 요일 배열 a 생성, 달별 일수 배열 b 생성

- x월 y일이 무슨 요일인지 계산하는 법: 
  1. 1월부터 x-1월까지의 일수를 더하고 y일을 더한 값을 총합으로 잡는다.
  2. 총합을 7로 나눈 나머지 값이 a 배열의 자리값을 의미함.

- 2번에서 구한 값을 출력하면 x월 y일의 해당 요일이 출력됨.
