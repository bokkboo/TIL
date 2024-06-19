# 소스코드
n = int(input())
for i in range(1, n+1):
    if(i==1 or i==n):
        print(' '*(n-i) + '*'*(2*i-1))
    else:
        print(' '*(n-i) + '*' + ' '*(2*(i-1)-1) + '*')

  # 설명
  1. else문 출력식에서 공백식은 식에 맞는 수열을 발견해야 함.
  2. if문에서 첫줄과 끝줄을 묶어서 처리
