# 공부 저장소
___

## - JavaScript

1. ### 변수
- 변수를 선언할 때는 let과 const 변수 앞에 붙여 선언해준다.
- ```js
  let age = 30; >> 'let'은 변할 수 있는 값을 선언할 때 사용.
  const speed = 26; >> 'const'는 변하지 않는 상수값을 선언할 때 사용. 
  ```
2. ### 자료형
- 문자형 표현법
  * "문자열" or '문자열' >> "" or '' 사용
  * `문자열은 총 ${변수}자리이다.` >> 백틱(``)사용 >> 문자열 안에 변수를 넣을 때 사용.

- 숫자형
  * 참고: NAN >> Not A Number의 약자 >> 숫자가 아님을 표현
 
- Boolean
  * 'true'와 'false'로 나타냄 >> 해당 코드의 참 거짓을 판별
 
- null, undefined
  ```js
  - undefined >> 변수를 선언만 하고 값을 할당하지 않으면 undefined.
  let age;
  console.log(age);

  - null >> 변수에 null을 할당하지만 변수가 존재하지는 않음
  let age = null;
  ```
3. ### alert, prompt, confirm
- alert
  - 알려줌

- prompt
  - 입력받음

- confirm 
  - 확인받음
  - ```js
    const NAME = confirm("당신의 이름은 MIKE가 맞습니까?");
    console.log(NAME); 
    >> MIKE가 맞으면 true를 아니면 false를 반환함
    ```
4. ### 형변환
- String() >> 문자형으로 변환
   
- Number() >> 숫자형으로 변환
              >> 숫자가 아닌 문자가 포함되어 있으면 NaN 반환
     
- Boolean() >> 불린형으로 변환
               >> 숫자(0), 빈 문자열(""), null, undefined, NaN은 false로 반환 나머지는 true로 반환

- 주의사항 >> Number(null) == 0, Number(undefined) == NaN

5. ### 기본 연산자
- 연산자 줄여서 쓰기
  ```js
  let num = 10;
  num = num + 5; -> num += 5; 변환 가능
  ```

- 증가 연산자, 감소 연산자
  ```js
  let num = 10;
  / let result = num++; >> 이 경우에는 num을 증가시키기 전에 result를 반환 >> result == 10.
  / let result = ++num; >> 이 경우에는 num을 증가시킨 후 result를 변환 >> result == 11.
  ```

6. ### 비교 연산자, 조건문
- 비교연산자
  - 같다: == / 다르다: !=   
  - 비교연산자는 불린값(true / false)를 반환한다
  - 동등연산자(==)와 일치연산자(===)
    - ```js
      const a = 1;
      const b = "1";
      
      console.log(a == b); >> true 반환 >> 동등연산자는 형 고려없이 반환
      console.log(a == b); >> false 반환 >> 일치연산자는 형 고려하여 반환      
      ``` 
- 조건문
  ```js
  - if(조건문 >> 불린형으로 반환 가능해야 함){
      실행문
  }
  ```

7. ### 논리연산자(AND, OR, NOT)
- OR(||)
  >> 하나라도 true면 true 반환(=모든값이 false일때만 false 반환)  
- AND(&&)
  >> 모든값이 true면 true 반환(=하나라도 false면 false 반환)
- NOT(!)
  >> true면 false, false면 true 반환
- 논리연산자 우선순위 >> AND가 OR보다 우선적으로 처리된다.
  ex) a && b || c >> (a && b) || c

8. ### 반복문
- for문
  ```js
  for(초기문; 조건문; 증감문;){
    문장  
  }
  ```
- do while문 >> while 반복문과 다르게 조건문 실행전 do 반복문이 최소 1번은 반복됨.
  ```js
  do{
    문장
  } while(조건문);
  ```
- while문
  ```js
  while(조건문){
    문장
  } 
  ```
- break문 >> 멈추고 반복문을 빠져나옴, continue문 >> 멈추고 다음 반복을 진행

### switch문 
- 사용: 어떤 대상을 case별 조건값을 기준으로 일치하는지 확인한 뒤 동작을 수행

- 로직
  ```js
  switch(대상) {
    case 조건값1;
      문장
      break; // 해당 case문을 빠져나오는 코드 >> 생략 가능
    case 조건값2;
      문장
      break;
  default: // 모든 조건값과 일치하지 않는 경우에 대한 코드 >> 생략 가능 
    동작  
  }
  ``` 

# 참고 리소스

[내게 실용적이었던 프로그래밍 공부 방법들](https://velog.io/@city7310/%EB%82%B4%EA%B0%80-%EA%B3%B5%EB%B6%80%ED%95%98%EB%8A%94-%EB%B0%A9%EC%8B%9D)
