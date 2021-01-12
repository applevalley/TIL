# Django Rest Framework

### API란?

>운영체제나 프로그래밍 언어가 제공하는 기능을 제어할 수 있게 만드는 인터페이스

- 그러면 API Server는 무슨 일을 하지?
  - 어떠한 요청을 받으면 그에 맞는 응답(데이터)을 보내준다!
  - 프로그래밍을 통해 요청에 RESTful한 방식으로 JSON을 응답해주는 서버!

### REST?

> REpresentational State Transfer

- 자원을 정의하고, 자원에 대한 주소를 지정하는 전반적인 방법
- 웹의 자료를 HTTP 위에서 전송하기 위한 인터페이스
- 자원(URI), 행위(HTTP Method), 표현(Representations)으로 구성되어 있다.
- URI는 정보의 자원을 표현하고, 그 자원에 대한 행위는 HTTP Method로 표현한다!
  - GET, POST, PUT, DELETE
    - GET: 지정 리소스의 표시를 요청. 오직 데이터를 받기만 한다
    - POST: 클라이언트 데이터를 서버로 보낸다.
    - PUT(PATCH): 서버로 보낸 데이터를 저장하거나 지정한 리소스의 부분을 수정
    - DELETE: 지정한 리소스를 삭제

- URI? URL?
  - URL: 네트워크상에서 자원이 어디에 있는지 알려주기 위한 규약 (인터넷에서 자원의 위치를 말한다)
  - URI: 인터넷에 있는 자원을 나타내는 유일한 주소
    - 하나의 리소스를 가리키는 문자열
    - 가장 흔한 URI는 URL이다. 웹 상의 위치로 리소스를 식별한다.
      - URL은 URI 안에 포함된다.
    - URI는 자원 표현뿐 아니라 계층적 표현이라는 특성 또한 가지고 있다.(상 -> 하)
- 자원에 대한 행위는 동사가 아닌 HTTP Method로!
  - URI는 자원을 표현하는 것에만 집중해야 한다.
  - 가령 `POST/accounts/3/create`이라는 것보다는 `POST/accounts/3/`이 더 RESTful하다는 것이다.
  - 조회는 GET 생성은 POST 수정은 PUT 삭제는 DELETE
  - Method만으로도 어떤 동작을 하고자 하는 것인지 알 수 있게끔 디자인하자

### JSON?

> JavaScript Object notation -> JS 객체 표기법

- 가벼운 데이터 교환 형식
- 완전히 언어 독립적인 텍스트 포맷
- JSON의 공식 인터넷 미디어 타입은 application/json이다.

### Serialization

> 직렬화. 데이터 구조, 오브젝트 상태를 동일하거나 다른 컴퓨터 환경에 저장하고, 나중에 재구성 가능한 포맷으로 변환하는 과정이다. 

- 쿼리셋이나 모델 인스턴스를 JSON이나 XML같은 데이터 타입으로 바꿔주는 일을 한다.
- Form과 ModelForm과 유사하다!
  - serializers.py에서 상속을 받아 사용하는데, 마치 Model과 유사하다.
- ModelSerializer
  - 모델에 기반한 필드를 자동으로 만들어주고, 
  - serializer를 위한 기본 유효성 검사 도구를 생성하고,
  - 기본적인 `.create()`, `.update()`를 포함한다는게 기존 serializer와 조금 다르다.
  - ModelSerializer를 통해 쿼리셋과 단일 모델 인스턴스를 직렬화해 JSON으로 응답

```python
from rest_framework import serializers
from .models import Account

class UserSerializer(serializers.ModelSerializer):
	email = serializers.Emailfield()
    name = serializers.Charfield(max_length=20)
    password = serializers.Charfield(max_length=16)
    
class AccountSerializer(serializers.modelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'email', 'password')
        # 여러 가지로 활용 가능
        # fields = '__all__'
        # exclude = ('users')
   
```

```python
# ModelForm이랑 얼마나 비슷할까?
from django import forms
from .models import Account

classs AccountForm(forms.Modelform):
    class Meta:
        model = Account
        fields = ('id', 'email', 'password')
```



|       | Django    | DRF             |
| ----- | --------- | --------------- |
| 응답  | HTML      | JSON            |
| Model | ModelForm | ModelSerializer |

### Serializer 활용하기



##### 더미 데이터 만들기

- django-seed 라이브러리

```bash
$ python manage.py seed app_name --number=20  # app 안에 더미 데이터 20개 생성
```

### HTML -> JSON

- HTML은 그 자체로 완결성이 있는 문서이기에 데이터 추출에는 적합하지 않다.
- 따라서 JSON을 직접 구성해 응답해야 하는데, 필드를 직접 구성해야 한다. 
  - 딕셔너리가 아니라면 `safe=false`라는 파라미터가 별도로 필요하다.
  - 딕셔너리를 넘겨주지 않았는데 위의 safe=false를 인자로 넘겨주지 않으면 오류가 난다.
- `JsonResponse`는 JSON-encoded된 응답을 제공해주고, 이것의 컨텐트 타입은 application/json이다.
  - 원하는 필드를 추가하거나, 주석처리해 안 보이게 할 수도 있다.
  - 이는 사용할 때마다 필드를 정의해주어야 한다는 것을 의미하기도 한다.
- `HttpResponse`를 사용하면 해당 필드들을 우리가 정의하지 않아도 된다.
  - 받아온 쿼리셋을 `data = serializers.serialize("json", QuerySet)`안에 넣으면 장고가 알아서 얘를 직렬화해준다.
  - `content_type=` 키워드 인자를 다양한 타입으로 활용할 수 있는데, 기본 값은 `text/html`이다.
- DRF 활용
  - `@api_view(['Method'])`가 없으면 동작을 안 한다!
  - `Response`
    - data는 응답을 위한 직렬화된 데이터이다. <- serializer.data를 넣어서 응답해주자!

```python
from django.http.response import JsonResponse
def user_list(request):
    users = User.objects.all()
    users_json = []
    
    for user in users:
        users_json.append({
            'name': user.name,
            'password': user.password,
            'email': user.email,
        })
    return JsonResponse(users_json, safe=False)

from django.http import HttpResponse
def user_list2(request):
    users = User.objects.all()
    data = serializers.serialize("json", users)
    return HttpResponse(data, content_type='application/json')

from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(['GET'])  # <- Get 요청만!
def user_list3(request):
    user = User.objects.get(pk=1)
    serializer = ArticleSerializer(user)
    return Response(serializer.data)
```

- Django serialization framework는 쿼리셋, 오브젝트같은 파이썬 모델 타입들을 다른 포맷으로 바꿔준다.

- Django를 기반으로 하지만, API 서버 개발을 위한 도움을 주는 라이브러리가 `djangorestframework`이다.
  - 여태까지는 순수한 장고로 데이터를 직렬화하고 Json으로 응답을 보냈다면, 이제 이러한 응답을 담당해주는 drf를 사용하게 되는 것이다.