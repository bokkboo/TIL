# 소스코드
n = int(input())
for i in range(1, n+1):
    print('*'*i + ' '*2*(n-i) + '*'*i)
for j in range(1, n):
    print('*'*(n-j) + ' '*2*j + '*'*(n-j))

# 주의
- 숫자랑 다항식 사이의 곱셈 넣기.
    2(n-i)가 아니라 2*(n-i)로 표기.
