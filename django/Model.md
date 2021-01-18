# Model

- 이 그림이 기억나는가?
  - 이제 여기서 모델이 추가된다

![image-20210117223439151](C:\Users\Rin\AppData\Roaming\Typora\typora-user-images\image-20210117223439151.png)

- 모델이란?
  - 저장되어 있는 DB의 구조를 의미한다.
  - 사용자가 저장하는 데이터들의 필수적 필드, 동작을 포함하는 단 하나의 정보 소스
  - **Django는 모델을 통해서 데이터에 접속하고, 데이터를 관리한다.**
  - 각 모델은 하나의 DB 테이블에 매핑

# DB

- 데이터베이스: 체계화된 데이터의 모임
  - 여러 사람이 공유, 사용을 목적으로 관리되는 정보의 집합
  - 자료 항목의 중복을 없애 조직적으로 통합, 자료 구조화를 통해 기억시킨 자료의 집합체
- 쿼리: 조건에 맞는 데이터 추출, 조작, 조회하기 위한 명령어

- 스키마: DB 자료 구조, 표현, 관계 등을 정의. 
  - DBMS가 설정에 따라 스키마를 만든다.
  - 사용자가 자료에 접근하면 DBMS는 스키마를 통해 명령을 수행한다.
- 테이블
  - 필드: 모델에서 정의한 클래스 내부의 클래스 변수
  - 레코드: 해당 필드들에 넣은 데이터들
  - 기본키: 각 레코드의 고유 값. 반드시 설정할 것(ID같은 것들)

# ORM

- DB는 SQL문만 인식한다.
  - 하지만 우리는 파이썬에서 Django를 조작하는데 어떻게 해야 하나?
  - 여기서 ORM을 사용하게 된다.
  - 객체 지향 프로그래밍 언어로 호환이 안되는 시스템간(django-SQL)의 데이터를 변환한다.
    - 프로그래밍 언어에서 사용이 가능한 가상의 객체 DB를 만들어 쓰는 것.
  - SQL에 대한 이해가 부족해도 DB에 연동하고, 쿼리를 보낼 수 있다.
  - 다만 ORM만으로는 완벽하게 DB를 다루는게 쉽지 않고, 객체 지향 접근으로 생산성은 올라갈 수 있지만 프로젝트의 규모가 커질수록 설계하기 까다롭다. ( 유지보수, 디버깅이 어려움)
  - **DB의 편리한 관리, 객체로 조작하기 위한 목적이 주가 된다.**
- 파이썬 언어로 DB에 명령어를 보내는 방법 -> DB API
  - DB를 편하게 조작하게 도와준다.
  - django가 객체를 조회, 생성, 수정, 삭제하는 API를 자동으로 만들어준다.
- 왜 쓰는거야?
  - DB 조작을 OOP(객체 지향 프로그래밍)처럼 하려고 
- 어떻게 만드는거야?
  - `클래스 이름.매니저.쿼리셋 API` 의 순서를 따른다.
  - 예시를 들면 `Article.objects.all()`
  - all()은 클래스 안의 모든 데이터를 요구하는 api임. 이 동작을 수행하려면 objects라는 중간 매니저가 필요
  - objects는 고정! 클래스 이름과 쿼리셋 api만 바뀐다.
  - `manager`
    - DB와의 인터페이스 역할
    - 기본적으로 모든 모델 클래스에 objects라는 매니저를 자동으로 추가하고, 매니저로 특정 데이터를 조작 가능
  - 쿼리셋
    - DB로부터 데이터를 읽고, 필터를 적용하거나 정렬
    - 쿼리셋 안의 객체는 없거나, 하나, 그 이상
    - DB로부터 전달받은 객체 목록이면서 objects를 사용해 복수의 데이터를 다루는 함수를 썼을 때 반환되는 객체
- 어떻게 하는거야?
  - 일반 파이썬 쉘에서는 접근 안된다. django-extensions 패키지를 설치한 뒤 shell_plus를 사용하자.

# Model 뜯어보기

- title = models.CharField()
  - title은 CharField()라는 클래스의 인스턴스

![image-20210117225645575](C:\Users\Rin\AppData\Roaming\Typora\typora-user-images\image-20210117225645575.png)

- CharField
  - 길이 제한이 있는 문자열이 필요할 때 (150자까지)
  - max_length가 필수
  - DB에 저장될 때 글자 수 조건에 부합하는지의 유효성 검사도 수행
  - 기본 양식은 TextInput
- TextField
  - 글자 수가 많은 필드에 적용. 길이 제한 따로 없음
  - 기본 양식은 Textarea
- DateTimeField
  - DateField와의 차이점은 시간까지 기록하는지 아닌지
  - 사용자가 직접 작성하지는 않는다.
  - auto_now_add(기본값은 False)
    - 최초 데이터 입력시 현재 날짜, 시간으로 갱신 -> 테이블에 데이터를 최초로 넣을 때
  - auto_now(기본값은 False)
    - 최종 수정 -> 저장할 때마다 현재 날짜, 시간으로 갱신

# Migrations

- 모델에 생긴 변화를 반영하는 방법
  - models.py가 변경되었다 -> makemigrations로 파일을 만든다 -> migrate를 통해 DB에 적용한다
- `makemigrations`
  - 모델이 변경됬을 때 사용한다. 새로운 설계도를 작성하는 것.
  - 0001_initial_py라는 파일이 생기고, 수행할 때마다 숫자가 늘어난다.
  - DB를 초기화시켜서 파일을 다 지우지 않는 이상 파일이 쌓이는데, 이것으로 모델의 변화를 알 수 있다.
  - 처음 수행하고 나면 db.sqlite3 파일을 생성한다.
  - 수행하는 앱에서 urls.py가 만들어지지 않은 경우 ModuleNotFoundError를 반환한다.

```bash
$ python manage.py makemigrations
```

- `migrate`
  - `makemigrations`를 통해 만들어진 설계도를 실제 DB에 반영하는 과정이라 볼 수 있다.
  - 모델의 변경 사항, DB의 스키마가 동기화된다.
  - 뭔가 엄청 수행되는 것을 알 수 있다.

```bash
$ python manage.py migrate
```

- `sqlmigrate`
  - 마이그레이션에 대한 SQL 구문을 보고자 할 때 사용
  - 앱 이름과 `makemigrations`를 통해 만들어진 파일 숫자 입력

```bash
$ python manage.py sqlmigrate app_name 0001
```

- 그래서 잘 된거야?
  - DB를 열어보면 app name_model name식으로 생성되어있는 것을 알 수 있다.

![image-20210117231500714](C:\Users\Rin\AppData\Roaming\Typora\typora-user-images\image-20210117231500714.png)

# CRUD

- 가장 기본적인 데이터 처리 기능. 생성, 읽기, 갱신, 삭제를 묶어 부르는 말
- 기본적인 기능이라 묶어서 설명된다. 이게 안 된다면 제대로 된 SW가 아니다.

- `Create`
  - 클래스에 대한 인스턴스를 만들어주자.
  - 1번 방법
    - **인스턴스로 클래스 변수에 접근 -> 해당 인스턴스 변수 변경 -> 인스턴스 save해 메서드 호출**
    - save를 안 하면 DB에 저장이 안 된다.
  - 2번 방법
    - 함수에서 키워드 인자 넘기기
    - 여전히 save가 필요하다.
  - 3번 방법
    - create()를 사용해서 쿼리셋 객체 생성, 저장을 한번에!
  - `__str__`
    - 표준 파이썬 클래스 메서드인 str()을 정의해 각 객체가 문자열 반환하게 함
    - models.py에 변경 사항이 생겼지만 DB 설계에 영향을 주는건 아니라 makemigrations해도 변화 X

```shell
# 1
article = Article() # 클래스로 인스턴스 생성

article.title = 'abc'  # 인스턴스 변수에 값 할당하기
article.content = 'defg'

article.save()  
# 저장을 해야 DB에 값이 들어감 - 저장 안하고 article 조회하면 <Article: Article object (None)>
```

```shell
# 2
article2 = Article(title='abcd', content='efgh')   # 인스턴스 생성과 값 할당을 동시에 
article2.save()   # 여전히 저장은 필요하다
```

```shell
# 3
Article.objects.create(title='abcde', content='fghij') # 쿼리셋 객체 생성, 할당, 저장까지
```

```shell
# __str__

# models.py

class Article(models.Model):
	...
	
	def __str__(self):
		return self.title   # 각 객체의 title만 반환하게 하겠다
		
Article.objects.all()
<QuerySet [<Article: abc>, <Article: abcd>, <Article: abcde>]>
```

- `Read`

  - all()
    - 쿼리셋 리턴. 리스트 비슷하게 동작한다.

  - get() -> pk 조회할 때
    - 객체가 없다면 DoesNotExist 에러 발생. 객체가 여러 개면 MultipleObjectsReturned 에러 발생.
    - unique, not null 특징이 있으면 사용 가능 (id같은 것)
    - 반환 자체는 쿼리셋이 아니라 object 하나를 돌려준다.
    - 반환이 된다는 것은 그것을 변수에 할당도 가능하다는 것을 의미한다.
  - filter()
    - 쿼리셋을 리턴한다.
    - 찾는 것이 없더라도 일단 빈 쿼리셋을 돌려준다.
    - 지정된 조회 매개 변수와 일치하는 새 객체를 포함하는 새 쿼리셋을 반환
    - lookup
      - get(pk=1)은 get(id__exact=1)와 동일한 의미를 가진다.
      - 그렇기에 get(id=1)으로도 사용이 가능한 것이다. 

- `Update`

  - 무엇을 수정할 것인가? 선택이 먼저 ( 인스턴스 생성 )
  - 인스턴스 변수에 접근해 값을 변경하고 저장한다.
  - DB에 저장하는 시점은 마지막 save() 메서드!
  - 정보가 갱신이 되면 models.py의 updated_at도 바뀐다.

```shell
article.title
# 'abcd'

article.title = 'ababcd'   # 일단 변수는 수정했지만 아직 DB에는 아무런 영향이 없다.
article.save()

article.title
# 'ababcd'
```

- `Delete`
  - 무엇을 삭제할 것인가? 선택
  - `.delete()` 메서드를 호출하면 삭제가 된다.
  - 삭제하는 것이기 때문에 .save() 메서드를 사용하지 않는다.
  - pk값을 이렇게 지우고 나면 재사용되지 않는다. 새로 생성한 데이터의 pk값은 삭제된 pk값이 아니다.
  - 삭제한 pk값을 다시 조회 시도하면 DoesNotExist 에러를 돌려준다.

# Admin

- 서버 관리자가 활용하기 위한 페이지.  반드시 기본 테이블 생성 이후에 관리자를 생성해야 한다.
- 관리자 계정만 만든다고 끝이 아니다. 
  - models.py에서 정의한 모델을 admin.py에 등록해야 어드민 페이지에서 관리할 수 있다.



```shell
$ python manage.py createsuperuser   # 관리자 계정 만들기

# admin.py
from .models import Article   #  현재 앱의 models.py에서 Article 모델 클래스를 불러온다

admin.site.register(Article)  # 등록
```





# 정리

- django는 모델을 통해 데이터에 접속, 관리
- DB는 체계화된 데이터들의 집합
- ORM은 OOP 언어를 이용해 호환 안되는 유형의 시스템간 데이터를 변환하는 기술
- 모델 안에는 Char, Text, DateTime, Integer, Boolean 등의 필드가 있음
- 모델을 변경한 후에는 makemigrations하고 그것을 migrate해야 DB에 반영된다
- DB API를 이용해 쿼리를 보내서 CRUD 동작을 할 수 있다

