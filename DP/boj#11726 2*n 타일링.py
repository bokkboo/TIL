# 소스코드
n = int(input())
d = [0]*1001 >> 1001 숫자 개수에 맞춰 잘 입력해야 함.
d[1] = 1
d[2] = 2
for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]
print(d[n]%10007)

# 설명
1. 상황: 
  - 해당 문제의 수열을 나열하다 보면 피보나치 수열과 같은 형식이 됨. 
2. 두 번째 열에서 필요한 타일 개수를 저장하는 리스트를 생성.
