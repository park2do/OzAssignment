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
