# 공부 저장소
___

## - JavaScript

1. ### 변수
- 변수를 선언할 때는 let과 const 변수 앞에 붙여 선언해준다.
- ```js
  let age = 30; >> 'let'은 변할 수 있는 값을 선언할 때 사용.
  const speed = 26; >> 'const'는 변하지 않는 상수값을 선언할 때 사용. 
  ```
* var, let, const의 구체적인 차이점
  ```js
  - TDZ(Temporal Dead Zone) >> 스코프 시작 지점부터 초기화 시작 지점까지의 구간
  - 변수의 선언 3단계
    1. 선언단계 >> 변수 등록 
    2. 초기화 단계 >> 값을 저장하기 위한 메모리 공간 확보 후 undefined 할당
    3. 할당 단계  
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

### 함수(function) 기초
- 로직
  ```js
  funcion 함수명(매개변수){ >> 함수 생성
    문장
  }
  
  함수명(인수); >> 함수 호출 >> 해당 인수는 함수의 매개변수로 전달됨
  ```
- 전역변수 & 지역변수
  ```js
  전역변수 >> 함수 밖에서 선언된 변수
  function Hello(name){
    const sen = `hello ${name}`; >> sen 변수가 함수 안에서 선언
    console.log(sen)  
  }

  지역변수 >> 함수 안에서 선언된 변수  
  ```

### 함수 표현식, 화살표 함수
- 함수 표현식, 함수 선언문
  ```js
  - 함수 선언문 >> function 키워드로 시작하고 함수명을 명시하는 형태 >> 함수를 어디서든 호출 가능
  Plus(1, 2); >> 선언 전에 호출해도 값이 반환됨
  
  function Plus(a, b) {
    console.log(a+b);
  }
  
  - 함수 표현식 >> 변수에 함수를 할당하는 형태 >> 함수 선언 후에만 호출 가능  
  ```
  
  * 호이스팅(hoisting)
    - 뜻: 끌어 올리기  
    - 기능: 선언한 변수나 함수가 선언 범위의 최상단으로 올라가 작동하는 것
    - 함수 선언문 >> 호이스팅 영향 받음 >> 함수 어디서든 호출 가능
      함수 표현식 >> 호이스팅 영향 안 받음 >> 함수 선언 후에만 호출 가능
      * 선언과 표현이 차이가 나는 이유? >> 'var'변수 사용의 차이

### 객체(Object)
- 의미: 여러 속성을 하나의 변수에 저장할 수 있게 하는 데이터 타입
  * 프로퍼티(Property) ~~ 속성
    >> 'key'와 'value'로 이루어짐
- 로직
  ```js
  const 객체 = {
    key: 'value',
  }  
  ```

### 배열
```js
- 로직
  let 변수명 = ['인덱스1', '인덱스2']; 

- 특징
  - 변수명.length >> 배열의 길이  
  - 변수명.push('인덱스') >> 배열 끝에 인덱스 추가
  - 변수명.pop() >> 배열 끝 요소 제거
  - 변수명.unshift('인덱스'); >> 배열 앞에 추가  
  - 변수명.shift(); >> 배열 앞에 제거
```

# 참고 리소스

- [내게 실용적이었던 프로그래밍 공부 방법들](https://velog.io/@city7310/%EB%82%B4%EA%B0%80-%EA%B3%B5%EB%B6%80%ED%95%98%EB%8A%94-%EB%B0%A9%EC%8B%9D)
- 모던 자바스크립트 deep dive >> [[https://poiemaweb.com/js-object](https://poiemaweb.com/)]
