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

- app 디렉토리에서 `serializers.py`를 만드는 것부터 시작!
  - 클래스 정의를 먼저 하자.

```python
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'password', 'email',)
```

- shell_plus상에서 확인해보자.
  - 우리가 정의한 Model들을 편하게 쓸 수 있게 해준다.
  - Serializer를 알아서 import해주지는 않기 때문에 한번 직접 import해줘야 한다.

```python
>>> from articles.serializers import ArticleListSerializer
>>> ArticleListSerializer():   # 클래스로부터 인스턴스를 만드는 문법
# serializer를 정의했을 뿐인데 field를 만들어주고, 유효성 검사 도구도 제공해준다.
# model 정보를 이미 알고 있기 때문이다. modelForm과 유사한 부분들이 있다. 
ArticleListSerializer():
    id = IntegerField(label='ID', read_only=True)
    title = CharField(max_length=100)
    
>>> serializer = ArticleSerializer(Article)
# serializer라는 인스턴스를 ArticleSerializer로부터 만들어내야 한다.
# ArticleSerializer 안에 Article을 넣어줘야 하는데, 아직 가져온 적이 없다. 그러면?
# Article을 가져오는게 우선되어야 한다.
>>> article = Article.objects.get(pk=1)
>>> article
<Article: Article object (1)>   # 단일 객체

>>> serializer = ArticleSerializer(article)
>>> serializer
ArticleSerializer(<Article: Article object(1)>):  # 앞에서 넣었던 객체가 안에 들어있다
    id = IntegerField(label='ID', read_only=True)
    title = Chatfield(max_length=100)
    
# 이렇게 나온 데이터는 직렬화 작업을 통해 번역이 된(쿼리셋, 모델 인스턴스에서 JSON 형태로 바뀐) 것이다.
>>> serializer.data
{'id': 1, 'title': 'hello this is test data'}

>>> articles = Article.objects.all()
>>> articles   # 쿼리셋
<QuerySet[<Article: Article object(1)>, <Article: Article object(2)>, ... ]>
# 얘도 직렬화해야하지 않을까?

>>> serializer = ArticleSerializer(articles)
>>> serializer.data  # 쿼리셋이기 때문에 오류가 발생한다!
# 일반적인 딕셔너리 형태가 아니라면 뭔가 조치를 취해야 한다. 그게 many=True이다.
# 단일 객체가 아닌 여러 개의 객체를 직렬화하려는 경우 many=True 옵션을 적어줘야 한다.

>>> serializer = ArticleSerializer(articles, many=True)
>>> serializer.data
[OrderedDict([('id', 1), ('title', 'datadata'), ('content', 'data11'), ... ]), ...]
# 이 결과가 어떠한 형태로 변환되어 나온 것이라는 생각을 하는게 중요!
```



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
    - 기본 값은 GET
    - 반드시 구성을 리스트로!
  - `Response`
    - data는 응답을 위한 직렬화된 데이터이다. <- serializer.data를 넣어서 응답해주자!
    - data는 필수 인자이다.
    - serializer 자체가 데이터는 아니다. serializer.data로 접근하자.

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



### DRF를 활용한 CRUD

> HTML으로 응답해줬던 것들을 이제 JSON으로 응답한다!

- 여기서부터 템플릿을 활용해 무언가 하지는 않기 때문에 urls.py에서 app_name을 작성할 필요가 없다!
- 사용자가 요청을 보내면 직렬화 등의 과정을 통해 결과적으로 JSON 데이터를 응답해줘야 한다.
- 뭐부터 해야 할까?
  - 일단 DB 안에 있는 객체 하나이던 쿼리셋이던 불러와야 한다.
  - 그 다음에 Serializer에 객체를 넣어서 직렬화한다.
  - 응답해준다.

```python
from rest_framework.decorators import api_view

@api_view(['GET'])
def article_list_create(request):
    articles = Article.objects.all()   # 일단 DB에서 불러오고 
    serializer = ArticleSerializer(articles, many=True)   # 직렬화해서
    return Response(serializer.data)    # 응답

# 디테일은 객체 하나를 다루게 된다. Article이라고 하면 그 대상은 당연히 pk로 접근하게 된다.
# 자연히 request와 article_pk를 넘겨주게 되고, Article.objects.get(pk=article_pk)로 쓸 수 있다.
# 그런데 이거보다는 객체가 있으면 가져오고 없으면 404를 띄우게 해서 더 직관적으로 쓸 수 있다.
from django.shortcuts import get_object_or_404  # 이제 템플릿에서 뭔가 안 하기에 render는 빼자

@api_view(['GET'])
def article_detail_update_delete(request, article_pk): 
    article = get_object_or_404(Article, pk=article_pk)  # 역시 불러오고
    serializer = ArticleSerializer(article)   # 직렬화 / 단일 객체이기에 many=True 안 쓴다
    return Response(serializer.data)     # 응답
```

- 하나의 serializer를 사용하면 쿼리셋으로 전체를 봤을 때도, 디테일로 한 객체를 봤을 때에도 serializer에서 정의된 field들이 그대로 나온다. 뭔가 불편하다. 디테일한 페이지에서는 여러 데이터들을 보고 싶다면?
  - serializer를 새로 만들어보자.

```python
# 리스트(전체)에서 사용할 serializer
class ArticleListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = ('id', 'title',)

# 디테일 페이지에서 사용해줄 serializer
class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'created_at', 'updated_at', 'comment_set', 'comment_count',)
```

- 여기서 잠깐

  - 장고에서 글을 쓰면 어떻게 됬나?
    - 사용자가 요청을 보내면 서버가 문서를 응답으로 준다.
    - 그러면 사용자는 그 문서를 채워서 다시 서버한테 요청을 준다.
    - 서버는 이 데이터를 유효성 검사를 거쳐 DB에 저장하는 과정을 거친다.
    - 이 과정 후 redirect를 통해 응답을 준다.
  - 근데 DRF는?
    - 템플릿이 없기에 DRF가 제공하는 기본적인 어떤 폼을 사용한다.
    - JSON 형태로 요청을 보내면 서버는 동일하게 유효성 검사를 한 뒤 그 결과로 뭔가 줄 것이다.
    - 템플릿이 따로 필요가 없다.

- 어떠한 요청을 보냈을 때, get 요청이면 `request.GET`에, post 요청이면 `request.POST`에 데이터가 들어있었고, 그것을 Form에 넣어줬던 것이 기존 Django에서 Create 로직을 처리하는 방식이었다.

  - DRF에서는 해당 요청 데이터를 `request.data`를 통해 가져올 수 있다!
  - 이렇게 받아온 데이터를 DB에 저장해주어야 한다.
  - Serializer 안에 요청에 대한 데이터인 `request.data`를 넣어준다.
  - save하기 전에 유효성 검사가 필요하다! 생각해보면 ModelForm을 다룰 때도 유효성 검사를 진행했었다.
  - 여기서 유효성 검사를 통과하지 못했을 때 if문 바깥에 return문이 없는 경우 None을 반환한다.
  - 이를 해결하기 위해 DRF는 `raise_exception`이라는 키워드 인자를 제공한다.
    - 잘못된 요청에 대해 400 에러를 준다.

  - 게시글에 대한 정보를 반환해준다.
    - 보통 응답 메시지는 200 코드를 기본으로 하는데(성공한 경우), status를 통해 커스텀 가능하다. 

```python
from rest_framework import status

@api_view(['POST'])
def create_article(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serialier.data, status=status.HTTP_201_CREATED)
```

- 이번엔 DELETE를 이용해 삭제해보자
  - 뭐부터 하지?
    - 그 전의 경험으로 보면 일단 받아온 다음에 삭제했다.
    - 똑같이 하면 된다!
    - 삭제하고 나면 뭘 응답으로 줘야 할까?
    - 사실 삭제해버렸기에 딱히 응답으로 줄건 없다.
    - `204 No content status`코드를 돌려주면서 삭제되었다는 것을 알려줄 수도 있지만, 삭제된 것에 대한 정보도 응답을 주는 것이 좋다.
    - 최초 삭제 요청에는 삭제가 되고 이미 삭제된 객체에 대해 반복적으로 요청한 경우  404 코드를 돌려준다.

```python
from django.shortcuts import get_object_or_404

@api_view(['DELETE'])
def delete_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return Response({'id': article_pk}, status=status.HTTP_204_NO_CONTENT)
```

- 마지막으로 남은건 PUT
  - UPDATE는 로직상 CREATE와 유사하다.
  - 새로 만드는건 아니지만 기존 객체 정보와 비교해 뭔가 수정을 해야 한다.
  - CREATE 로직과 유사하다고 해서 CREATE 로직으로 그대로 들고 오고 메서드를 PUT으로 주면 어떻게 될까? 수정이 될까?
  - 안타깝게도 새로운 글이 계속 생길 것이다. 메서드 자체가 수정을 보장하는게 아니다. PUT으로 보낸다고 해서 내부 로직과 무관하게 수정이 되는게 아닌 것이다.
  - POST면 생성, PUT이면 수정.. 이와 같은 일종의 약속인 것이지 실제 내부 로직을 어떻게 구성하는지에 따라 결과는 달라질 수 있다!
  - CREATE 로직과 다른 부분은 serializer를 정의하는 부분에서 `data=request.data` 앞에 객체가 온다는 것이다. 

```python
@api_view(['PUT'])
def update_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = ArticleSerializer(article, data=request.data)  # 객체가 들어가는 것에 주목
	if serializer.is_valid(raise_exception=True):
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)
```

- 이렇게 CRUD 로직을 DRF를 이용해 각각 만들어보았다. 물론 Restful하지 않다.
- 어떻게 바꿔줄까?
  - 우선 코드는 겹치는 기능들을 한 묶음으로 다시 구성해주고, path도 수정해야 한다.
  - 어떻게 묶어줄까?
    - 우선 id(article_pk)의 유무로 나눌 수 있다.
    - 그러면 article 전체 조회, 생성으로 하나, 디테일 / 수정 / 삭제로 한 묶음으로 총 2개로 나눌 수 있다.
    - 그리고 디테일, 수정, 삭제 묶음 로직에서도 `get_object_or_404(Model, pk)`같은 경우 중복되어 쓰이게 된다. 이런 경우는 if 분기 밖으로 빼내어 공통적으로 쓸 수 있게 한다.
- 최종으로 정리된 코드는....

```python
@api_view(['GET', 'POST'])
def article_list_create(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    else:
        # print(request.data)
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def article_detail_update_delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)  # 겹치는 부분이라 밖으로 꺼냄

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'PUT':
        # serializer = ArticleSerializer(instance=article, data=request.data)
        ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:
        article.delete()
        return Response({ 'id': article_pk }, status=status.HTTP_204_NO_CONTENT)
```

- restful하다.



### 댓글 CRUD

- 댓글은 어떨까?
  - 우선 app의 models.py에서 댓글에 대한 모델을 정의한다.
  - 글과 댓글의 관계는 1:N이다. 한 글이 여러 댓글을 가질 수 있다.
  - 특정한 article 객체를 참조해야 한다.(article_pk)
  - 댓글도 결국 직렬화가 되어야 한다. 어떻게 직렬화해야 할지에 대한 부분은 어디서 작성할까?
    - serializers.py에 댓글에 대한 새로운 serializer를 만들어야 한다.
    - 어느 article을 참조하는지에 대한 정보가 필요하기에 serializer의 field에 article도 포함한다.

```python
class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # 참조할 모델 정보, 부모 객체가 삭제되었을 시 자식 객체를 어떻게 할지
```

```python
class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'content', 'article',)
        read_only_fields = ('article',)  # 왜 써야 하는지는 아래를 보자
```



- POST
  - 언뜻 보면 글 POST 로직과 비슷해보인다. 아예 가져다가 쓰면 어떨까? 이게 될까?
  - article이 필수 항목이라는 오류 메시지를 받을 것이다. 
  - 물론 postman상에서 article 번호를 넘겨주면 댓글은 달린다.
  - 그런데 이미 url상에서 몇번째 article인지가 특정된 상황에서 article 번호를 별도로 지정해 요청을 보내는게 매우 어색하다. 뭐가 문제일까?
    - serializer를 만들 때 field에 지정한 article이 걸린다.
    - 글 POST 로직을 그대로 가져온 코드는 댓글 작성 시도 시 유효성 검사를 통과하지 못하고 있다.
    - 그래서 일단 유효성 검사를 실행하지 않고, form으로 데이터를 넘길 것이 아니라는 것을 DRF에게 알려줘야 한다. 
    - 이럴 때 사용해야 하는 것이 `read_only` 라는 속성이다.(읽기 전용)
    - 이렇게 해서 해결되면 참 좋은데, 이제는 데이터 무결성 에러가 났다.
    - `read_only`를 지정하는 경우 읽기 전용으로 유효성 검사를 하지 않는다는 것을 의미한다. 그런데 유효성 검사를 하지 않음으로 그 코드를 통과했더라도 바로 뒤의 `serializer.save()`에서 넘어온 데이터가 없는 상태이기에 저장하는 시점에서 오류가 또 나는 것이다.
    - `save()`를 하는 시점에 데이터를 넘겨주어야 하는데, `save()`의 키워드 인자로 request.data에 포함되지 않은 데이터를 넘겨줄 수 있다.
    - article에 대한 정보를 받아오고, `serializer.save(article=article)`처럼 save()안에 위에서 정의한 article을 넣으면 유효성 검사 문제도 해결하고, DB에 save되는 시점에서 url에서 넘어오는 pk값인 article을`article=article` 처럼 넘겨줘서 저장할 수 있다.

```python
# 문제의 코드
@api_view(['POST'])
def create_comment(request, article_pk):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
# 수정된 코드
@api_view(['POST'])
def create_comment(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
```

