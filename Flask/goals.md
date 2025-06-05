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

# flask-MySQL

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
