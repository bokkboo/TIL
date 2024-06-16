# 소스코드
n = int(input())
for i in range(1, n+1):
    print(' '*(i-1) + '*'*(2*(n-i)+1))
for j in range(1, n):
    print(' '*(n-1-j) + '*'*(2*j+1))
