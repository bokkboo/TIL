# 소스코드
while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break

# 새로운 개념
1. while 반복문 사용: 특정한 범위 없이 계속해서 반복할 시 'while True:'문 사용

2. 오류 예외 처리 방법 (try-except문)
  - form: try:
            ...
          except [발생오류 [as 오류변수]]:  // []표시 안에 있는 내용은 생략 가능하다는 뜻. 필요하면 쓰고 필요 없으면 생략 가능
            ...
    except만 포함 / + 발생오류 / + 오류변수 - 총 3가지 케이스

  - 위 문제는 첫 번째 case. try문을 실행하고 오류가 나는 입력값(ex. ㄱ, ㄴ)은 except문으로 넘어가 break문에서 반복문 종류
