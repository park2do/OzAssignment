Flask

# 특징

    확장가능성이 높다
    실전용은 낮다. MVP 개발용도

# 풀스택 프레임워크 VS 마이크로 프레임워크

    풀스택
        전체적인 애플리케이션에 필요한 모든 것을 포괄적으로 제공하는 프레임워크
        기능의 포괄성
        내부 일괄성
        1. Java Spring
        2. Python Django
        3. Ruby on Rails
    마이크로
        기능에 중점, 선택적으로 추가한다.
        경량성
        유연성
        1. Flask
        2. Express.js (Node.js)
            비동기 프로그램이 장점

# Flask 프로젝트 세팅

    프로젝트 폴더 생성
    가상환경 생성
        poetry (django)
            Python -m venv .venv
        conda
        venv
    flask 모듈 설치
    app.py 생성
    flask 실행
        flask run

# 라우팅

서버의 사용
flask run 개발환경에서 사용
WSGI 배포단계에서 사용

    사용
        기본경로 설정

    Jinja(Template Engine)
        동적 데이터 렌더링

        {% ... %}
            제어 구조
            반복문

# REST API (Representational State Transfer Application Programming Interface)

자원(Resources, 데이터) 중심으로 설계

프로토콜 메소드를 통해 자원에 대한 작업을 수행함.

> **자원 식별**: 사용자 정보 자원은 `/users/{userId}`URI를 통해 식별 <br/> > **자원 표현**: 사용자 정보는 JSON, XML의 형태로 클라이언트에게 전달 <br/> > **자원에 대한 행위**: 사용자 정보를 조회하기 위해 `GET /users/{usrId}`요청을 사용하고 , 사용자를 생성하기 위해 POST `/users`요청을 사용

CRUD(Resources) => PGPD(Protocol Methods)

## API의 구성 요소

> (1) 자원(resource): URI <br/>
> 클라는 위와 같은 URI 형식을 통해 서버에 데이터를 요청 <br/><br/>
> (2) 행위(methods, status): <br/>1. GET <br/>2.POST<br/> 3. PUT<br/> 4. DELETE</li><br/><br/>
> (3) 표현(representation):<br/>서버에서 클라로의 데이터 전달 방법 (`xml`, `json`, `txt`, `rss`)

## 원칙

- (1) 자원 기반의 URL <br/>
- (2) statelessness
  - 독립적인 요청: 각 API 요청은 다른 요청과 독립적으로 처리됨. 서버는 요청에 대한 정보를 기억하지 않음.
  - 서버의 상태 저장 없음: 서버에 이전 행동에 관한 정보를 저장하지 않음. 모든 요청은 필요한 모든 정보를 포함해야함. `(사용자 인증 정보)`
  - 세션 관리의 부재: 세션 상태`(로그인 상태, 이전 작업 등)`를 기억하거나 관리하지 않음
- (3) 표준화된 메소드 사용
- (4) Representation

## REST API 해석 연습

### 1.

- feeds/1

  - GET: id가 1인 게시글 데이터 보내줘
  - POST: id가 1인 게시글 만들어줘
  - PUT: id가 1인 게시글 수정해줘
  - DELETE: 1번 게시글 삭제해줘

- feeds/all

  - GET: 게시글 데이터 전부 보내줘
  - POST: X
  - PUT: X
  - DELETE: X

- myinfo

  - GET: 내 정보 보여줘
  - POST: X
  - PUT: 내 정보 수정
  - DELETE: 회원탈퇴

- users/1
  - GET: 1번 유저의 정보

### 2. 인스타그램 API

| 작업               | 메소드 | URL                       | 설명                      |
| ------------------ | ------ | ------------------------- | ------------------------- |
| 사용자 프로필 조회 | GET    | /users/{username}         | 사용자 프로필 정보를 조회 |
| 게시물 목록 조회   | GET    | /posts                    | 모든 게시물 조회          |
| 새 게시물 작성     | POST   | /posts                    | 새로운 게시물 작성        |
| 게시물 수정        | PUT    | /posts/{posts_id}         | 게시물 수정               |
| 게시물 삭제        | DELETE | /posts/{posts_id}         | 게시물 삭제               |
| 댓글 목록 조회     | GET    | /posts/{post_id}/commnets | 게시물 댓글 조회          |
| 댓글 작성          | POST   | /posts/{post_id}/commnets | 게시물 댓글 작성          |
| 팔로우             | POST   | /user/{user_id}/follow    | 사용자 팔로우             |
| 언팔로우           | DELETE | /user/{user_id}/follow    | 사용자 언팔로우           |

# JSONIFY

- Python 데이터를 JSON 형식으로 변환하여 HTTP응답으로 반환하는 함수
- Python의 기본 데이터 타입(딕셔너리, 리스트)를 JSON 문자열로 변화
- JSON (JavaScript Object Notion)
  - Key, Value 형태
  - 컴퓨터간 상호작용의 형식

## 1. Library Import

```
from flask import request, jsonify
```

## 2. GET Method

```
@app.route('/api/v1/feeds', methods=['GET'])
def get_all_feeds():
    data={'result': 'success', 'feeds': ['feed1', 'feed2', 'feed3']}
    return jsonify(data)
```

## 3. POST Method

POSTMAN 설치

```
@app.route('/api/v1/feeds', methods=['POST'])
def create_feed():
    name = request.form['name']
    age = request.form['age']

    print(name, age)

    return jsonify({'result': 'success'})
```

```
request.get_json() #들어오는 데이터는 json형태로 받겠다.
```

### 에러

```
400 Bad request. The browser (or proxy) sent a request that this server could not understand.
```

- POST parmeter 없을 시 발생
- 제대로 된 param(BODY)에 보냈는지 확인

`출처: https://skylit.tistory.com/316 [초코아빠*:티스토리]`

# Flask-RESTfulAPI

## Flask-RESTfulAPI 설치

```
pip install flask-restful
from flask_restful import Resource
```

## 사용예시

/resources/item.py

```
class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return {"msg": "Item not found"}, 40
```

app.py

```
from flask_restful import Api
from resources.item import Item

api = Api(app)

api.add_resource(Item, '/item/<string:name>') # add default route
```

# smorest

- REST API를 쉽게 작성할 수 있도록 도와주는 라이브러리
- Flask-REST보다 더 많은 기능과 OpenAI(Swagger)문서 자동 생성 기능을제공

## smorest 설치

```
pip install flask-smorest
```

## flask app 진입점

```
from flask import Flask
from flask_smorest import Api
from api import blp

app = Flask(__name__)

# OpenAPI 관련 설정

app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui" #페이지를 예뻐보이게 하는 기능

app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)
api.register_blueprint(blp)

if __name__ == "__main__":
    app.run(debug=True)
```

## Schemas 설정

`pip3 install marshmallow`

```
from marshmallow import Schema, fields
# marshmallow 라는 모듈에서 Schema와 fields를 불러옴

class ItemSchema(Schema)
# 클래스명을 ItemSchema 라고 하고 marshmallo 에서의 Schema를 상속받음

    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str()
    # 위 세 줄의 형태를 객체라고 하며, 이 객체를 나중에 직렬화하거나
    역직렬화할 때 실제로 거기에 데이터에서 뭔가 잘못된 것이 있는지 체크해줌
```

## Blueprint

- 블루프린트는 애플리케이션의 특정 기능 별로 라우팅, 뷰 함수, 템플릿, 정적 파일 등의 관리가 가능
  - API가 복잡해질 수록 관리의 필요성이 증가함.

주요 기능:

- 모듈화
- 라우팅 관리: 블루프린트의 자체 URL 규칙
- 기능별 분리: 블루프린트 특정 기능에 대한 라우팅, 뷰 함수, 에러 핸들러, 템플릿 등등

사용법:

- 블루프린트 구문 작성
- 앱에 블루프린트 등록

```
from flask import Flask, Blueprint, render_template, request

app = Flask(__name__)

# 첫 번째 블루프린트
my_blueprint = Blueprint('my_blueprint', __name__)

@my_blueprint.route('/hello')
def hello():
    return "Hello from my blueprint!"

@my_blueprint.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}!"

# 두 번째 블루프린트
another_blueprint = Blueprint('another_blueprint', __name__, url_prefix='/another')

# /another/world
@another_blueprint.route('/world')
def world():
    return "Hello, world, from another blueprint!"

# /another/echo
@another_blueprint.route('/echo', methods=['POST'])
def echo():
    data = request.json
    return f"Received: {data}"

# 블루프린트에 템플릿을 사용하는 예제
@another_blueprint.route('/template')
def using_template():
    return render_template('example.html')

# 세 번째 블루프린트
third_blueprint = Blueprint('third_blueprint', __name__, url_prefix='/third')

@third_blueprint.route('/bye')
def goodbye():
    return "Goodbye from the third blueprint!"

# 애플리케이션에 블루프린트 등록
app.register_blueprint(my_blueprint)
app.register_blueprint(another_blueprint)
app.register_blueprint(third_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
```

## Abort

- 기능
  - API 개발 중 오류 처리
  - 오류 상태와 메세지 전달
- Flask와 Flask-smorest에서 함수 처리 요청 중 오류가 발생 했을 때 사용됨.

### 기본 사용법

```
from flask_smorest import abort

# 오류 상황에서 abort 호출
abort(404, message = "Resource not found")
```

```
from flask import Flask, abort

app = Flask(__name__)

@app.route('/example')
def example():
    error_condition = True

    # 어떠한 조건에서 오류를 발생시키고 처리
    if error_condition:
        abort(500, description = "An error occurred while processing the request.")

    # 정상적인 응답
    return "Success"
```

# flask-MySQL (DB)

### 필요한 도구

- Flask
- MySQL
- MySQL Workbench
- Flash-MySQL-DB

설치: Cloud Service DB의 경우 경로만 바꾸어주면 OK~.

## flask MysQL 설치

`pip install flask-mysqldb`

## tabel(MySQL) 생성 및 DB관련 코드(app.py) 작성

MySQL

```
CREATE DATABASE oz;
USE oz;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);
```

app.py

```
from flask import Flask
from flask_mysqldb import MySQL
from flask_smorest import Api
# user_routes에서 Blueprint 직접 임포트 대신 함수 임포트
from user_routes import create_user_blueprint

app = Flask(__name__)

# MySQL 연결 설정
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'oz-password'
app.config['MYSQL_DB'] = 'oz'

mysql = MySQL(app)

# blueprint 생성 및 등록
app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

user_blp = create_user_blueprint(mysql)
api = Api(app)
api.register_blueprint(user_blp)


from flask import render_template
@app.route('/users_interface')
def users_interface():
    return render_template('users.html')


if __name__ == '__main__':
    app.run(debug=True)
```

## Error

클래스 내의 어트리뷰트가 없음.

`'NoneType' object has no attribute 'name'`

# ORM (Flask-SQLAlchemy / DB)

- 파이썬의 객체 관계 매핑 (Object Relational Mapping)
  - SQL이 아닌 ORM 방식으로 DB의 데이터를 조회할 수 있도록 도와줌.

## ORM (Object-Relational Mapping)

객체 : 객체, 클래스, 속성의 구조
관계형 데이터 베이스: 테이블 로우 컬럼과 같은 구조

- 데이터베이스의 테이블을 객체로 매핑하고, 객체 간의 관계를 데이터베이스의 외래 키 등으로 매핑하는 방식
- 객체 - Python(Flask, Django)
- Relational DataBase
- 위 두 가지를 Mapping 시키는 것
  => DB에 있는 데이터들을 객체처럼 사용할 수 있도록 도와줌. SQL 쿼리문 없이 데이터 CRUD가 가능.

기능

1. Model

- DB 테이블 생성을 해줌

2. ORM

- DB 테이블 데이터를 읽음

WHY ORM??

- 데이터베이스 코드가 간결해짐
- 결과 오류를 줄임 (쿼리에 대한 증명이 가능 > Schema)
- 쿼리를 쉽게 작성할 수 있음 (진입장벽 넘어가면 쉬움.)

## Flask-SQLAlchemy

- Flask에서 SQLAlchemy(ORM)을 사용할 수 있도록 도와주는 라이브러리

## 설치 목록

라이브러리 설치 / Flask-sqlAlchemy

```
pip install Flask-sqlAlchemy
pip install pymysql #connect with mysql through sqlAlchemy
```

## 파일 구조 구축

```
│ ├ └ ─

├─app.py
├─db.py
├─models.py
└─routes
    ├─users.py
    └─board.py
```

- app.py
  - 구동하는 코드 작성
- moedels.py
  - 스키마 작성
    - `boards = db.relationship('Board', back_populates='author', lazy='dynamic') `
      - 상호참조(역참조),
      - lazy='dynamic'설정(lazy=dynamic 이 쿼리셋은 데이터 베이스에서 즉시 모든 데이터를 로딩하지 않음. 일부만 로딩하려할 때 유용하다. 사용자가 작성한 게시판 글들의 목록을 관리할 때, 한번에 모든 글을 로드하지 않고 필요에 따라 특정 글들만 조회할 수 있도록 한다.)

## python 작성

## html 작성

- /templates 작성
- 그 안에 html 만들기
  - /templates/boards.html
  - /tempaltes/users.html

app.py

```
from flask import Flask
from flask_smorest import Api
from db import db
from models import User, Board

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:As583346!@@127.0.0.1/oz' #MySQL 연결
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #추적 기능 비활성화

db.init_app(app)  # db 객체를 Flask 앱에 연결, db객체는 중복 사용하므로 모듈화

#blueprint 설정
app.config['API_TITLE'] = 'My API'
app.config['API_VERSION'] = 'v1'
app.config['OPENAPI_VERSION'] = '3.1.3'
app.config['OPENAPI_URL_PREFIX'] = '/'  # OpenAPI URL 접두사 설정
app.config['OPENAPI_SWAGGER_UI_PATH'] = '/swagger-ui'  # Swagger UI 경로 설정
app.config['OPENAPI_SWAGGER_UI_URL'] = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'  # Swagger UI 리소스 URL

api = Api(app)  # Api 객체 생성

from flask import render_template # 라우팅
@app.route('/manage-boards')
def manage_board():
    return render_template('boards.html')

@app.route('/manage-users')
def manage_users():
    return render_template('users.html')

if __name__ == '__main__':
    with app.app_context():
        print("main run")
        db.create_all()

    app.run(debug=True)
```

model.py

```
# Model -> Table
# 게시글 - board
# 유저 - user
# 추후 모델들을 models/user.py models 디렉토리를 만들어 관리하는 것이 좋음.
from db import db

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    boards = db.relationship('Board', back_populates='author', lazy='dynamic')
    #역참조 개념, 사용자가 작성한 모든 게시물을 나타냄 ()
    #lazy=dynamic 이 쿼리셋은 데이터베이스에서 즉시 모든 데이터를 로딩하지 않음.
    #일부만 로딩할 때 유용함. 사용자가 작성한 게시판 글들의 목록을 관리할 때,
    #한번에 모든 글을 로드하지 않고 필요에 따라 특정 글들만 조회할 수 있도록 함.

class Board(db.Model):
    __tablename__ = "boards"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    author = db.relationship('User', back_populates='boards')
    #역참조, 게시물 작성한 사용자(user)를 나타냄.
```

board.py

```
from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint
from db import db
from models import Board

board_blp = Blueprint('Boards', 'boards', description='Operations on boards', url_prefix='/board')



# id 값이 필요한지 아닌지에 대한 유무
@board_blp.route('/')
class BoardList(MethodView):
    def get(self): # 모든 게시글 불러오기
        boards = Board.query.all() # Board의 모든 데이터 가져옴.
        return jsonify([{"user_id": board.user_id,
                        "id": board.id,
                        "title": board.title, "content": board.content, "author": board.author.name} for board in boards])

    def post(self): # 게시글 만들기
        data = request.json # 데이터는 json 형태로 받음
        new_board = Board(title=data['title'], content=data['content'], user_id=data['user_id'])
        # 데이터베이스에 추가하기 위한 {key:value} 형태로 변환
        db.session.add(new_board) # 데이터 베이스에 추가
        db.session.commit()
        return jsonify({"message": "Board created"}), 201

#
@board_blp.route('/<int:board_id>')
class BoardResource(MethodView):
    def get(self, board_id): #(self, board_id)
        board = Board.query.get_or_404(board_id)
        #id값으로 얻어야 하기에 Board.query.all() -> Board.query.get_or_404(board_id)로 가져옴
        return jsonify({"title": board.title, "content": board.content, "author": board.author.name})

    def put(self, board_id): #업데이트한데용~
        board = Board.query.get_or_404(board_id)
        data = request.json
        board.title = data['title'] #title과 content만 바꿈
        board.content = data['content']
        db.session.commit()
        return jsonify({"message": "Board updated"})

    def delete(self, board_id):
        board = Board.query.get_or_404(board_id)
        db.session.delete(board)
        db.session.commit()
        return jsonify({"message": "Board deleted"})
```

users.py

```
from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint
#블루프린트는 애플리케이션의 특정 기능 별로 라우팅, 뷰 함수, 템플릿, 정적 파일 등의 관리가 가능
from db import db
from models import User

user_blp = Blueprint('Users', 'users', description='Operations on users', url_prefix='/users')

@user_blp.route('/') #유저의 id가 필요 없기에 '/' 사용
class UserList(MethodView):
    def get(self): # 유저를 전부 가져옴.
        users = User.query.all() # 전부 주세여~
        user_data = [{"id":user.id, "name": user.name, "email": user.email} for user in users]  # Convert to list
        return jsonify(user_data)

    def post(self):
        print("요청은 오는가?")
        user_data = request.json # request.json -> 유저가 보낸 데이터
        new_user = User(name=user_data['name'], email=user_data['email'])
        # key:value로 나누기, 데이터 형식 구분
        db.session.add(new_user) # 데이터베이스에 추가
        db.session.commit()
        return jsonify({"message": "User created"}), 201

@user_blp.route('/<int:user_id>') # id값이 필요
class Users(MethodView):
    def get(self, user_id): # self, user_id
        user = User.query.get_or_404(user_id) # 하나만 조회 -> get_or_404(user_id) 사용
        return {"name": user.name, 'email': user.email}

    def put(self, user_id): # 업데이트
        user = User.query.get_or_404(user_id)
        user_data = request.json

        # update 항목
        user.name = user_data['name']
        user.email = user_data['email']

        db.session.commit()
        return {"message": "User updated"}

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted"}
```

## 에러

`Errno 11003` > SQLAlchemy 1.4를 사용하면 해결됨.

- 1. SQL Alchemy 1.4 사용
- 2. MySQL80 서비스 실행
- 3. 해결 못해서 MySQL 삭제 해버림

# db 객체 모델 정의 방법 2가지

## db 객체와 모델 클래스를 같은 파일에 위치시키기

models.py

```
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    #... User model

Class Board(db.Board):
    # ... Board model
```

app.py

```
db.init
```

## db 객체와 모델 클래스를 분리하기 (모델이 많아져서 관리해야할 시)

db.py

```
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy
```

model.py

```
from db import db

class User(db.Model):
    # User Model

class Board(db.Model):
    # Board Model
```

app.py

```
db.init_app(app)
```

# Schema와 Model의 차이

| 이름   | 정의                                                                    | 용도                           |
| ------ | ----------------------------------------------------------------------- | ------------------------------ |
| Schema | 데이터의 직렬화와 역직렬화, 유효성 검증을 위해 사용됨                   | 직렬화,역직렬화에 초점         |
| Model  | 데이터베이스의 테이블을 의미함, ORM 도구를 통해 데이터베이스와 상호작용 | 데이터베이스와 상호작용에 초점 |

## 직렬화와 역직렬화 (Schema의 주요 용도)

### 직렬화(Serialization)

복잡한 데이터 구조를 JSON과 같은 포맷으로 변환하는 과정

```
# Python Data
user_instance = User(id=1, username='JohnDoe')

# Serialization
class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str()

# Result
{
    "id": 1,
    "username": "JohnDoe"
}
```

### 역직렬화(Deserialization)

JSON 데이터를 Python과 같은 데이터 구조로 바꾸는 것

```
# JSON Data
{
    "username": "JaneDoe"
}

# Deserialization
user_data = {"username": "JaneDoe"}
user_schema = UserSchema()
user_instance = user_Schema.load(user_data)

# Result
User(username='JaneDoe')
```

# Flask-Migrate

- 데이터베이스의 변화를 알려주는 라이브러리 (Django는 장착되어 있음)
- Alembic: SQLAlchemy 사용 시에 데이터베이스를 관리해주는 Python기반의 마이그레이션 도구.
  - 데이터베이스 스키마 변경 감지
  - 데이터베이스 버전 컨트롤

## 설치

```
pip install Flask-Migrate
```

## Migrate 설정

app.py

```
from flask_migrate import Migrate

migrate = Migrate(app, db)
```

### 초기 Migration 생성

데이터베이스 마이그레이션을 사용하기 위해 초기 마이그레이션 파일 생성이 필요

```
flask db init
```

## flask db Migrate

- github commit과 비슷

```
flask db migrate
flask db migrate -m "Your migration message"
```

## flask db upgrade

- github push와 비슷

```
flask db upgrade
```

# Flask Authentication

## 1. Session

- Session 웹-애플리케이션이 사용자의 상태를 유지하기 위해 주로 사용됨. 서버 측에 사용자 정보를 기록하고, 로그아웃하면 그 상태를 제거함.
- 왜 필요한가?
  - HTTP는 stateless 프로토콜이기 때문에, session을 통하여 서버에 저장.

### 보안상의 문제

- 브라우저는 세션 ID를 쿠키에 저장하므로, 쿠키가 해킹될 가능성이 있음.
- SECRET_KEY의 유출 위험
  - SECRET_KEY > 암호화 하는 키.
- 서버의 리소스를 많이 잡아먹음.

### 세션 인증의 동작 방식

- 로그인 > 세션 ID > 상태 유지 > 로그아웃

1. 로그인: 사용자가 로그인 폼을 제출하면, 서버는 이를 검증하고 세션에 사용자 인증 정보를 저장.

2. 세션ID: 저장된 인증 정보를 서버 내의 고유한 세션 ID 생성 및 브라우저에 쿠키 형태로
   전송. 이후 모든 요청에서 세션ID를 서버에 전송.

3. 상태 유지: 서버는 받은 세션 ID를 사용하여 사용자의 인증 상태와 관련 데이터를 조회. 로그인 상태 확인, 해당 사용자에게 적절한 응답 제공.

4. 로그아웃: 사용자 로그아웃 시, 서버는 해당 사용자의 세션을 제거하고 세션ID를 무효화.

## 2. HTTP 기본 인증

## 3. Flask-Login

## 4. JWT-Extended

# 기타

정적 웹사이트
클라이언트 <=> 웹 서버

동적 웹사이트
클라이언트 <=>
웹 서버(NGiNX) <=>
Gateway Interface(WSGI) <=>
웹 어플리케이션 서버(Flask, Django) <=(ORM)=>
Database

# 미주

- oz코딩스쿨
- 한 권으로 정리하는 파이썬 백엔드
- 플라스크 공식문서 https://flask-docs-kr.readthedocs.io/ko/latest/
- 본인 벨로그: https://kkjjww1102.tistory.com/5
- smorest velog: https://velog.io/@legendofjiwon/flask-smorest
- smorest doc: https://flask-smorest.readthedocs.io/en/latest/
