Django

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

# model 만들 때 절차

1. 폴더 생성
2. config/setting에 등록
3. 코드 작성
4. admin.py 에 등록
5. migration, migrate

```
python manage.py startapp users
```

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
# Custom Admin

- 비밀번호 해쉬화, 비밀번호 저장 등의 기능을 장고에서 사용
- 사용법

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