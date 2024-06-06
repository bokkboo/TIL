# 소스코드
word = input()
for i in range(0, len(word), 10):
    print(word[i:i+10])

# 설명
  - 입력받은 단어를 10개씩 끊어서 출력해야 하므로 print() 안에 10개의 단어가 들어가게 세팅 해주면 됨 >> 문자열 인덱싱, 슬라이싱 사용

# 새로운 개념
1. for 반복문 range() 함수
  - form:
    range(start, stop, step)
  - 설명:
    start: 특정 범위에서 첫 번째 값
    stop: 특정 범위를 초과하는 최대 한계치
    step: 특정 범위 안에 있는 값들의 증가값 제어 >> start 값을 전달한 다음 값으로 start+step 값을 전달
