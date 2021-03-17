# DB

- DB는 체계화된 데이터의 모임.
- 여러 사람이 공유하고, 사용할 목적으로 통합 관리되는 정보의 집합이다.
- 몇 개의 자료 파일을 조직적으로 통합해 자료 항목의 중복을 없애고 자료를 구조화해 기억시켜 놓은 자료의 집합체이다.

### 장점

- 데이터 중복 최소화
- 데이터 무결성 - 정확한 정보 보장
- 데이터 일관성
- 데이터 독립성 - 물리적 / 논리적
- 데이터 표준화
- 데이터 보안 유지

### RDBMS

- 관계형 데이터베이스 관리 시스템
  - 관계형 모델을 기반으로 한다.
- 관계형 데이터베이스?
  - 관계를 표현하기 위해 2차원의 표를 사용한다. - 릴레이션
  - 행은 튜플이 되고, 열은 어트리뷰트가 된다.
  - 어트리뷰트의 수를 차수라 하고, 튜플의 수를 카디널리티라 한다.
- 스키마: DB에서 자료의 구조, 표현 방법, 관계등을 정의한 구조
  - 테이블: 열(컬럼)과 행(레코드)의 모델을 사용해 조직된 데이터 요소들의 집합.
  - 열: 각 열에는 고유한 데이터 형식이 지정된다.(INTEGER, TEXT 등..)
  - 행(레코드): 테이블의 데이터는 행에 저장된다. 

### SQL

- 관계형 데이터베이스 관리 시스템의 데이터를 관리하기 위해 설계된 특수 목적의 프로그래밍 언어
- DBMS에서 자료의 검색과 관리, DB 스키마 생성과 수정, DB 객체 접근 조정 관리를 위해 고안됨
- SQLite는 별도로 PRIMARY KEY 속성 컬럼 작성해주지 않으면 값이 자동으로 늘어나는 PK 옵션을 가진 rowid 컬럼을 정의한다!!
  - rowid는 자동으로 작성된다. 하지만 직접 id 컬럼을 만든 경우 id를 명시하지 않으면 자동으로 입력되지 않는다.
- INTEGER PRIMARY KEY 타입으로 컬럼을 만들면 이것이 rowid를 대체할 수 있다.
- 꼭 필요한 정보라면 공백으로 비워두면 안된다!!!



- DDL(데이터 정의어) - CREATE / ALTER / DROP

- DML(데이터 조작어) - INSERT / UPDATE / DELETE / SELECT

- DCL(데이터 제어어) - GRANT / COMMIT / ROLLBACK / REVOKE

- DDL

  - CREATE

    - 테이블 정의 - CREATE TABLE table(이름);

    ```
    CREATE TABLE classmates (
    	id INTEGER PRIMARY KEY,
        name TEXT
    );
    
    CREATE TABLE classmates (
    	name TEXT,
    	age INTEGER,
    	address TEXT
    );
    
    CREATE TABLE customers (
    	id INTEGER PRIMARY KEY,
    	name TEXT NOT NULL,
    	age INT NOT NULL,
    	address TEXT NOT NULL
    );
    ```

  - DROP

    - 특정 table 삭제 - DROP TABLE table(이름);

    ```
    DROP TABLE classmate;
    ```

  - ALTER

    - 특정 테이블의 이름을 변경한다. 
    - ALTER TABLE exist_table RENAME TO new_table;

- DML

  - 테이블에 데이터 삽입 -  INSERT
  - 데이터 삭제(행 제거) - DELETE
  - 데이터 갱신 - UPDATE
  - 데이터 검색 - SELECT

  - SELECT

    - SELECT * FROM table; -> table에 있는 모든 데이터를 조회하는 명령어
    - SELECT column1 FROM table; -> 특정한 table에서 특정 column만 가져오기
    - SELECT column1 FROM table LIMIT num; -> 특정 table에서 원하는 개수만큼 column 가져오기
    - SELECT column1 FROM table LIMIT num OFFSET num; -> table에서 특정 column값을 특정 위치에서부터 몇 개만 가져온다면?
    - SELECT column1 FROM table WHERE column = value -> table에서 column 값중 특정한 값만 가져온다면?
    - SELECT DISTINCT column FROM table -> table에서 특정 값을 중복 없이 가져오기
    - SELECT COUNT(column) FROM table; -> 레코드의 개수를 반환한다!
    - SELECT AVG/SUM/MIN/MAX(column) FROM table -> 숫자일 때 가능한 표현식

    ```
    SELECT rowid, name FROM classmates;
    rowid name
    ---
    1 김
    2 이
    3 박
    
    SELECT rowid, name FROM classmates LIMIT 2;
    rowid name
    ---
    1 김
    2 이
    
    SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;
    3번째 값만 가져온다
    
    SELECT rowid, name FROM classmates WHERE address='서울';
    ---
    1 김
    
    SELECT COUNT(*) FROM classmates;
    
    SELECT MAX(age) FROM classmates;
    ```

    

  - INSERT

    - 특정 table에 새로운 행을 추가해 데이터를 추가할 수 있다
    - INSERT INTO table (column1, ..) VALUES (value1, ...)
    - 값을 지정하지 않은 column에는 NULL이 들어간다!
    - column 값을 전부 집어넣을 때에는 column을 생략하고 values만 넣을수도 있다!!

    ```
    INSERT INTO classmates (name, age) VALUES ('홍길동', 25);
    
    name age address
    홍길동 25 NULL
    
    INSERT INTO classmates VALUES ('통키', 7, '화산');
    
    name age address
    통키 7 화산
    
    # 여러개도 작성이 된다.
    INSERT INTO classmates VALUES ('김',20, '서울'), ('이', 40, '제주');
    ```

    

  - DELETE

    - 특정 table의 특정한 레코드를 삭제할 수 있다.
    - DELETE FROM table WHERE condition;
    - 삭제의 기준은? 중복이 불가능한 UNIQUE 값인 rowid가 기준이 된다!

    ```
    DELETE from classmates WHERE rowid=4;
    ```

  - UPDATE

    - 특정 table의 특정한 레코드를 수정할 수 있다.
    - UPDATE table SET column1=value1 WHERE condition;

    ```
    UPDATE classmates SET age=30 WHERE rowid=1; 
    
    UPDATE classmates SET name='김김', address='제주' WHERE rowid=3;
    ```

## 와일드카드

- 정확한 값에 대한 비교가 아닌, 패턴을 확인해 해당하는 값을 반환한다.

- `-` : 반드시 이 자리에 **한 개** 의 문자가 존재해야 한다!

  ```
  _4%: 아무 값이나 들어가고 두번째가 4로 시작하는 값
  9__: 9로 시작하고 3자리
  7__%: 7로 시작하고 적어도 3자리(%에 값이 들어오면 4자리)
  ```

  

- `%` : 이 자리에 문자열이 없을 수도 있다.

  ```
  2%: 2로 시작하는 값
  %2: 2로 끝나는 값
  %7%: 7이 들어가는 값
  ```



## 정렬

- SELECT columns FROM table ORDER BY column1 ASC/DESC ( 오름차순은 기본값-안써도 적용)

- GROUP BY: 지정된 기준에 따라 행 세트를 그룹으로 결합함. 데이터 요약시 주로 사용.

  - SELECT column, COUNT() FROM table GROUP BY column;

  

## 연습해보기

- table에서 age가 30 이상인 사람만 가져오면?

```
SELECT * FROM table WHERE age>=30;
```

- table에서 age가 30 이상인 사람의 이름만 가져오면?

```
SELECT name FROM table WHERE age>=30;
```

- table에서 age가 40 이상인 사람의 수는?

```
SELECT COUNT(*) FROM table WHERE age>=40;
```

- 50살 이상인 사람들의 평균 나이는?

```
SELECT AVG(age) FROM table WHERE age>=50;
```

- table에서 나이순으로 오름차순 정렬해 상위 10개만 추리면?

```
SELECT * FROM tables ORDER BY age LIMIT=10;
```

- user 테이블 전체 데이터 조회

```
SELECT * FROM users_user;
```

- id가 19인 사람의 age 조회

```
SELECT age FROM users_user WHERE id=19;
```

- 모든 사람의 age 조회

```
SELECT age FROM users_user;
```

- age가 40 이하인 사람들의 id와 balance

```
SELECT id, balance FROM users_user WHERE age<=40;
```

- 성이 김이고 balance가 500 이상인 사람들의 이름을 조회

```
SELECT last_name FROM users_user WHERE first_name='김' AND balance>=500;
```

- 이름이 '수'로 끝나면서 행정구역이 경기도인 사람들의 balance

```
SELECT balance FROM users_user WHERE address='경기도' AND last_name LIKE '%수';
```

- balance가 2000 이상이거나 age가 40 이하인 사람의 수

```
SELECT COUNT(*) FROM users_user WHERE balance>=2000 or age<=40;
```

- 번호 앞자리가 010으로 시작하는 사람의 수

```
SELECT COUNT(*) FROM users_user WHERE phone LIKE '010%';
```

- 이름이 박옥자인 사람의 행정구역을 경기도로 수정

```
UPDATE users_user SET address='경기' WHERE first_name='옥자' AND last_name='박';
```

- 이름이 괴물인 사람을 삭제

```
DELETE id FROM users_user WHERE first_name='괴물';
```

- balance를 기준으로 상위 4명의 이름, 성, balance를 조회

```
SELECT first_name, last_name, balance FROM users_user ORDER BY balance DESC LIMIT 4;
```

- 번호에 123을 포함하고 age가 30 미만인 정보를 조회

```
SELECT * FROM users_user WHERE age<30 AND phone LIKE '%123%';
```

- 번호가 010으로 시작하는 사람들의 행정 구역을 중복 없이 조회

```
SELECT DISTINCT counrty FROM users_user WHERE phone LIKE '%010%';
```

- 모든 인원의 평균 age

```
SELECT AVG(age) FROM users_user;
```

- 박씨의 평균 balance

```
SELECT AVG(balance) FROM users_user WHERE last_name = '박';
```

- 경북에 사는 사람 중 가장 많은 balance의 액수를 조회

```
SELECT MAX(balance) FROM users_user WHERE country='경북';
```

- 제주에 사는 사람 중 balance가 가장 많은 사람의 이름

```
SELECT first_name FROM users_user WHERE country='제주' ORDER BY balance DESC LIMIT 1;
```

