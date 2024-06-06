# 소스코드
1(내 코드). 
n = int(input())
for i in range(1, n+1):
    print(n+1-i)
2(다른 코드). 
n = int(input())
for i in range(n, 0, -1):
    print(i)

# 설명
  - 1번 코드: 출력값을 나열 해보고 range()함수 안의 리스트를 나열했을때 각 자리를 더하면 n+1임을 이용한 풀이

  - 2번 코드: step 인자는 시작값이 1이므로 이를 -1로 바꿔주면 n부터 -1을 계산한 값이 출력되게 된다.
