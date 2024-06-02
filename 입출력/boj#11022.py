# 소스코드
T = int(input())
for i in range(1,T+1):
    A, B = map(int, input().split())
    print(f"Case #{i}: {A} + {B} = {A+B}")

# 설명
print문에서 변수와 연산기호들을 각각 따옴표를 씌워 처리해도 되지만 f-string을 사용해 포매팅 했으므로 ""안의 변수들 i, A, B, A+B 모두 중괄호로 묶어서 처리하는게 더 깔끔. (각각 따옴표 씌울 필요 없음)
