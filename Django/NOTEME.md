Django

# Django 단계 정리
1. Django 설치
2. Project 생성
3. App 생성
4. Model 정의
5. Migration 
6. 관리자 페이지 설정
7. View 설정
8. UR 설정
9. 서버 실행 및 확인
10. 템플릿 사용

# 폴더 구조

│ ├─ └─

```
├─db.sqlite3
├─manage.py
├─NOTEME.md
├─poetry.lock
├─pyproject.toml
├─.venv/
│   └─virtual env.
├─boards/
│   └─python apps
├─config/
│   └─python apps
├─feeds/
│   └─python apps
└─user/
    └─python apps
```

# 설치

```
poetry add Django # 라이브러리 설치
poetry shell # 가상환경 실행
django-admin startproject config . # 장고 프로젝트 생성
django-admin startapp myapp # 앱 생성
django-admin makemigrations
django-admin

```

추천

```
https://legend-palm-1f1.notion.site/04-Django-3-4-afc627b0a42b47c3b35967aee46a8d22
```

# URL & VIEW

## 파일로 따로 나누어 URL 관리

# Model

- Board > Table 개념
- Table

> DB에서 등록하려면 migration 해줘야함.
> makemigration > migrate : 사전 등록 > 완전 등록

orm 방식으로 사용하기

```
python manage.py shell
```

## model 만들 때 절차

1. 폴더 생성
2. config/setting에 등록
3. 코드 작성
4. admin.py 에 등록
5. migration, migrate

```
python manage.py startapp users
```

## Foreign KEY

```
콜럼이름 =  models.ForeignKey("부를 모델", 참조된 유저가 삭제되면 그 유저와 관련된 레코드도 삭제.)
user = models.ForeignKey("users.User", on_delete=models.CASCADE)
```
 
## REFERENCES
`https://legend-palm-1f1.notion.site/09-2-4-046fb212b1814589a9c88e222b4fbd32`

# Admin Panel
- 웹 애플리케이션의 데이터를 관리하기 위한 사용자 친화적인 인터페이스. (어드민 페이지)

1. 관리자 인터페이스 활성화
2. 모델을 관리자 페이지에 등록
3. 관리자 계정 생성
    - 생성
        `python manage.py createsuperuser` at zsh
4. 관리자 페이지 접속 및 사용    
5. 관리자 페이지 커스터마이징
    - Titling
        ```
        def __str__(self):
            return self.name
        ```
        at models.py
    - Categorizing 
        `list_display` at admin.py
    - Filtering
        `list_filter` at admin.py
    - Searching
        `search_field` at admin.py
    - Ordering
        `ordering` at admin.py
    - Readonly
        `readonly_fields` at admin.py
    - Detailing (fieldsets)
        ```
        filedsets = (
            (None, {'field': {'a', 'b'}}),
            ('Advanced options', {`field`:('x', 'y', 'z'), 'classes': ('colapse',)}),
        )
        
        ```

# Django User Model > 유저 정보 설정

- 장고 내에서 만들어 놓은 User Model이다. (여러가지 클래스가 담겨있어.)
- 비밀번호 해쉬화, 비밀번호 저장 등등의 기능의 다양한 기능

## 사용법

(0) users.app
```
python manage.py startapp users
```

(1) users/models.py 수정
```
from django.contrib.suth.models import AbstractUser

class User(AbsractUser)
    pass
```

(2) users/admin.py 
```
from django.contrb.auth.admin import UserAdmin

@admin.register(User)
class CustomerUserAdmin(UserAdmin):
    pass
```
(3) config/settings.py
```
AUTH_USER_MODEL = "user.User"
```

(4) users/migrations 폴더에서 00001,0002로 시작하는 파일 삭제 / db.sqlite3 삭제
(5) migrate
(6) user create
- db 초기화해서 해야함
```
python manage.py createsuperuser
```

# Django Common Model > 다양하게 사용 가능
- Logic: Common Model을 생성함으로써 공통으로 필요한 값을 만들어 놓고 그 안에 상속받을 Model을 따로 설정한다.
- CommonModel's Structure: 각 객체에 공통적으로 설정할 수 있는 정보(값) 
> ex) 만든 시각, 수정된 시각 등등 
- 이러한 값에 대한 app을 따로 설정하여 필요한 상황에 꺼내어 쓴다.

## 서순

1. common 예시 앱 생성
2. 상속
3. Migration
4. Custom Admin Panel 

## 코드
1. common 앱 생성
```
pyhton manage.py startapp common
```
2. 상속
상속해준다.
```
from common.models import CommonModel

class Chiren(CommonModel):
    ~~~
```
3. Migration
4. Custom Admin Panel 

## META
- DB 테이블에는 추가하지 않되, 추상 기반 class 저장하여 꺼낼 수 있다.
> model.py에 DB TABLE을 설정하지 않아도. 
> admin.py에서 쓸 수 있다는 의미.

# ORM (Object-Relational Mapping)
- Object (장고)
- Relatinal Datbase (RDBMS)
- Mapping

## 자주 사용하는 함수
1. filter()
    - 찾고 싶은 객체 반환
2. exclude()
    - 제외하고 싶은 객체 빼고 반환
3. annotate()
    - 쿼리 결과에 계산된 필드를 추가
4. aggregate()
    -  QuerySet에 포함된 객체들에 대해 집계연산 싫행 // 데이터베이스 단계에서 실행.
5. order_by()
    - 정렬
6. all()
    - 전체반환
7. get()
    - 데이터 반환, 값이 하나만 있어야함
8. exists()
    - 쿼리셋에 하나 이상의 객체가 존재하는 지에 대한 여부 확인
9. count()
    - 숫자 세기
10. select_related() / prefetch_related()
    - 관련된 객체를 효율적으로 불러오기 위한 메소드,
        - select_related() : JOIN을 사용하여 관련 객체를 한 번의 쿼리로 불러옴
        - prefetch_related() : 별도의 쿼리를 실행하여 관련 객체리르 미리 가져옴


## python manage.py shell
django 프로젝트에서 Python 인터프리터 환경을 Django와 연결하여 실행하는 명령어.
> Django ORM을 포함한 전체 프로젝트 환경에서 Python 코드를 실시간으로 실험하거나 실행할 수 있는 "개발용 콘솔"

```
python manage.py shell 
```

## ORM CRUD

### 기본 사용법
- model 불러오기
```
from board.models import Board // Board 테이블 가져오기
```

### CRUD
- 쿼리문 작성 

```
// Board 테이블 내에 id 값이 1인 쿼리 가져오기
board = Board.objects.get(id=1) 
```

```
// 제목 전부 불러오기
boards =  Board.objects.all() 
for i in boards:
    print(i.title)
```
### REVERSE ACCESSORS
- 역으로 데이터를 찾는 법. (부모 -> 자식 X;  자식 -> 부모 O)

```
from users.models import User

user = User.objects.get(pk=1) # pk가 1인 user를 가져옴
user.board => X 
    => user.board_set
board.user => O 

dir(user) # 이 함수를 통해서 user에서 사용가능한 모든 함수의 리스트를 본다.

BOARD => USER
USER <= BOARD (X)

user.board_set
user.board_set.all()
user.review_set

> user.board_set.all()
<QuerySet [<Board: 제목>, <Board: title2>, <Board: updated title>]>

```


## QUERY SET

- Django의 QuerySet은 데이터베이스의 데이터를 조회하고 필터링하는 데 사용되는 핵심 개념. 
- QuerySet = 테이블로부터의 객체 집합. 여러가지 방식으로 이 집합을 조직.

1. Lazy Excution
    - 천천히 불러와 데이터베이스의 부담을 지우기
    - 최대한 천천히 불러옴.
    - 사용할 때 바로 쿼리함.
2. Method Chaining
    - QuerySet의 메소드들을 연결하여 하나의 쿼리 문장을 만든다. (여러가지 쿼리를 하나의 쿼리를 묶는다.)
3. Main Methods
    - filter()
    - exclude()
    - annotate()
    - order_by()
    - all()
    - get()
4. Caching
    - 한번 사용한 QuerySet을 캐싱하여, 재사용 가능.
5. Slicing
    - 파이썬의 특정 부분만 추출 가능 / 인스타그램 피드 30개 제한처럼
6. Q / F Object 
    - Q 객체를 사용하여 복잡한 쿼리 조건 구성 가능
    ```
    from django.db.models import Q
    User.objects.filter(Q(is_staff=True) | Q(is_superuser=True))
    ```
    ```
    User.objects.filter(~Q(is_active=True))  # 비활성 유저 찾기
    ```
    - F 객체를 사용하여 필드 간의 관게나 조건 표현 가능.
    ```
    # 가격을 10% 올리기
    Product.objects.update(price=F('price') * 1.1)
    # views 수 1 증가
    Post.objects.filter(id=3).update(views=F('views') + 1)
    ```
| 항목     | Q 객체                           | F 객체                          |
| ------ | ------------------------------ | ----------------------------- |
| 목적     | 조건을 복합적으로 구성할 때 사용             | 필드 간의 비교나 연산을 할 때 사용          |
| 예시 용도  | OR / AND / NOT 조건 만들기          | stock < min\_stock 같은 비교      |
| 대표 메서드 | `filter()`, `exclude()` 등에서 사용 | `filter()`, `update()` 등에서 사용 
7. Database Optimization
    - 관련된 객체를 효율적으로 불러오기 위한 메소드,
    - select_related() : JOIN을 사용하여 관련 객체를 한 번의 쿼리로 불러옴
    - prefetch_related() : 별도의 쿼리를 실행하여 관련 객체를 미리 가져옴

    - **예시**:
    
    두 함수의 차이는 객체들을 불러오는 방식에 차이가 있습니다.
    
    **1. `select_related()` 사용 예시**
    
    - **상황**: "블로그 글"과 "작성자"가 있으며, 각 블로그 글은 하나의 작성자와 연결되어 있습니다.
    - **모델 구조**:
        
        ```python
        class Author(models.Model):
            name = models.CharField(max_length=100)
        
        class BlogPost(models.Model):
            title = models.CharField(max_length=100)
            content = models.TextField()
            author = models.ForeignKey(Author, on_delete=models.CASCADE)
        ```
        
    - **`select_related()` 사용**:
        
        ```python
        # BlogPost와 연관된 Author 객체를 한 번의 쿼리로 불러옵니다.
        posts = BlogPost.objects.select_related('author').all()
        
        for post in posts:
            print(post.title, post.author.name)
        ```
        
        여기서 **`select_related('author')`**는 BlogPost와 Author 테이블을 JOIN하여 한 번의 쿼리로 데이터를 가져옵니다. 이는 관련된 객체가 "하나"일 때 유용합니다.
        
    
    **2. `prefetch_related()` 사용 예시**
    
    - **상황**: "강사"와 "강의"가 있으며, 각 강사는 여러 강의를 진행할 수 있습니다.
    - **모델 구조**:
        
        ```python
        class Instructor(models.Model):
            name = models.CharField(max_length=100)
        
        class Course(models.Model):
            title = models.CharField(max_length=100)
            instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
        ```
        
    - **`prefetch_related()` 사용**:
        
        ```python
        # 각 Instructor에 연결된 모든 Course 객체를 별도의 쿼리로 미리 가져옵니다.
        instructors = Instructor.objects.prefetch_related('course_set').all()
        
        for instructor in instructors:
            print(instructor.name)
            for course in instructor.course_set.all():
                print(course.title)
        ```
        
        여기서 **`prefetch_related('course_set')`**는 Instructor와 연결된 모든 Course 객체를 별도의 쿼리로 가져온 후, Python에서 이를 조합합니다. 이는 관련된 객체가 "여럿"일 때 유용합니다.
        
        이러한 방식으로 **`select_related()`**와 **`prefetch_related()`**를 사용하면 데이터베이스의 부담을 줄이면서 필요한 데이터를 효과적으로 불러올 수 있습니다.


# RESET API

REST API (Respresentational State API)
- 자원을 이름으로 표현하여 자원의 상태를 주고 받는 것. (표현 방식: URI)

1. Django REST FRAME 설치
2. SEIRIALIZING

### URI or URL?
URI > URL (Link)

## 1. Django REST frame 설치

(1) frame install
```
poetry shell
poetry add djangorestframework
```

(2) config/settings.py
```
INTALLED_APPS = [
    ...
    'rest_framework',
]
```

(3) INSTALLED_APPS 분리
```
INSTALLED_APPS = CUSTOMEDE_APPS + DJANGO_APPS
```

## 2. SERIALIZING
직렬화:  Django(Objects) -> JSON
역질렬화: JSON -> Django(Objects)

CLINET(REACT, VUE etc..) <-X-> DJango(Object)
    - 상호간 이해가 불가함.

### Serializer.py
- Serialzing Model Data 
- Serializer.py 클래스 생성후 ModelSerializer 상속.
```
# users/serializers.py
from rest_framework.serializers import ModelSerializer
from .models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__" # Model의 전체 field 가져옴
        fields = ("nickname", "email") # 원하는 특정 field만 가져옴
        exclude = ("password",) # 특정 field 제외 가능
```

### views.py

[views.py](http://views.py) ⇒ status에 따라서 처리 + Objects → JSON

- http 요청에 따라 get, post, put, delete 함수 실행됨.
- Objects 데이터 ⇒ Json 데이터로 직렬화하는 과정

```python
# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import Serializer

class Datas(APIView):
	def get(self, request):
		datas = Model.objects.all()
		serializer = Serializer(datas) # QuerySet이 2개 이상일 때 Object->JSON
		return Response(serializer.data) # serialized된 데이터를 return

	def post(self, request):
		data = request.data => JSON
		datas = Model.objects.create(Serializer(data)) # JSON->Objects

	def put(self, request):
		data = request.data => JSON
		datas = Model.objects.update(Serializer(data)) # JSON->Objects

	def delete(self, request):
		JSON => ID값 뽑아와서 
		data = Model.objects.get(id=id)
		data.delete()  # 객체 삭제 -> dir()
```

**urls.py**

- as_view() ⇒ APIVIew와 url을 맵핑시켜주는 함수

```python
from django.urls import path
from . import views

urlpatterns = [    
		path("", views.Models.as_view())
]
```

## Serializing WorkFlow
<strong> Model -> Serialzer -> View -> URL </strong>


## Feeds

### 3. GET/Feeds API (1/2)

---
### WorkProcess

- 1. app 및 model 생성
- 2. rest_framework 불러오기 in views.py
    - `from rest_framework.views import APIView`
        - CBV (Class Based View)
         - FBV (Function Based View)
- 3. views.py 작성
- 4. serializer 및 model 불러오기 
- 5. serializers.py 작성

```
class FeedSerializer(ModelSerializer):
    class Meta:
        model = Feed # Feed라는 모델이라는 직렬화 할 것이다.
        field = "__all__" # Feed의 모든 field를 직렬화 할 것이다.
``` 

6. serializer 불러오기 in views.py

7. views.py 작성 (2)

```
class Feeds(APIView):
    # 전체 게시글 조회
    def get(self,request):
        feeds = Feed.objects.all();

        # 객체 -> JSON (Serialize)
        serialized = FeedSerializer(feeds, many=True)

        return Response(serialized.data)
```
8. urls.py 작성 (해당 app 내)
    urlpatterns = [ 
        path("", views.Feeds.as_view()),
    ]

### 4. GET/Feeds API (2/2) 

1. 피드에서 유저 데이터도 불러옴
    - depth : 1
2. 유저 데이터에서 민감한 정보도 같이 불러와짐
3. 차단해야함
    - users/serializer.py
    - user = FeedUserrSerializer()

### 5. POST/Feeds API  

- 1. POST 작성 in views.py
```
def post(self, request):
    serializer = FeedSerializer(data=request.data) 
    feed = serializer.save(user = request.user) # 받은 데이터 저장 시, 유저 데이터도 받아야 함으로 넘겨줘야 함.
    serializer = FeedSerializer(feed)
    print("post serializer", serializer)

    return Response(serializer.data)
```

- 2. save() 함수 사용 시, is_valid() 함수로 먼저 확인해줘야함. (django가 그렇게 하래)
    - `serializer.is_valid()`  

## Users

### 6. POST/users API

- 1. password

- 2. other information towards users

### 7. UPDATE/users API

- 1. Get, Put 이용하기

```
class MyInfo(APIView):
    def get(self, request): 
        user = request.user 
        serializer = MyInfoSerializer(user)
        return Response(serializer.data)
    
    def put(self, request):
        user = request.user
        serializer = MyInfoSerializer(user, data=request.data, partail=True)
        
        if serializer.is_valid():
            user = serializer.save()  
            serializer = MyInfoSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
```

- 2. 클래스 이용. 

- 3. 업데이트 설정 가능한 웹페이지 따로 생성하여 교체. # URL 설정

## Reviews

### 8. GET/ reviews API

models.py
```
from django.db import models
from common.models import CommonModel
# Create your models here.
class Review(CommonModel):  
    content = models.CharField(max_length= 100)
    likes = models.PositiveBigIntegerField(default=0)
    
    user = models.ForeignKey("users.User", on_delete=models.CASCADE) 
    feed = models.ForeignKey("feeds.Feed", on_delete=models.CASCADE)

```
serializers.py
```
from rest_framework.serializers import ModelSerializer
from .models import Review

class ReviewsSerializer(ModelSerializer):
    class Meta:
        model: Review
        fileds = "__all__" 
           
```
Views.py
```
from rest_framework.views import APIView
from .models import Review
from .serializers import ReviewsSerializer
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

# Create your views here.
class Reviews(APIView):
    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewsSerializer(reviews, many=True)
        return Response(serializer.data)

class ReviewDetail(APIView):
    def get(self, request, review_id):
        try: 
            review = Review.objects.get(id=review_id)
        except:
            raise NotFound
        
        serializer = ReviewsSerializer(review)
        return Response(serializer.data) 
```
urls.py
```
from django.urls import path
from . import views


urlpatterns = [
    path("", views.Reviews.as_view()),
    path("<int:review_id>/", views.ReviewDetail.as_view())
]
```