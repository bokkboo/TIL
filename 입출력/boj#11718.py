# 소스코드
while True:
    try:
        print(input())
    except EOFError:
        break


# 새로운 개념
  1. EOFError (End Of File Error)
  - 개념: 
    try-except 문에서 발생오류에 해당하는 부분으로 input을 사용한 입력 시 더 이상 입력할 파일이 없다는 뜻. 
  - 사용:
    except 옆에 써 더 이상 입력값이 없다면 break를 통해서 빠져 나오게 세팅.
