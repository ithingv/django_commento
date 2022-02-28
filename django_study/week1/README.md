# Django


### 특징
- 장고는 high levl python web framwork로 빠른 개발, 클린한 디자인을 가졌다. 장고는 번거로운 웹 개발을 대부분 처리하므로 원하는 기능을 구현하는데 집중할 수 있으며 무료이고, 오픈소스이다.

### 속도

- 장고는 개념 학습에서부터 프로젝트를 완성하는데까지 빠른 속도로 개발이 가능하다.

### 기능
-  장고는 일반적인 웹 개발 작업을 처리하는데 사용할 수 있는 수십 가지 추가 기능을 가지고 있다. 장고는 사용자 인증, 콘텐츠 관리, 사이트 맵, RSS 피드등의 기능을 사용할 수 있다.

    - [ORM](https://docs.djangoproject.com/en/4.0/topics/db/models/)
    - [URLs and Views](https://docs.djangoproject.com/en/4.0/topics/http/urls/)
    - [Templates](https://docs.djangoproject.com/en/4.0/topics/templates/)
    - [Forms](https://docs.djangoproject.com/en/4.0/topics/forms/)
    - [Authentication](https://docs.djangoproject.com/en/4.0/topics/auth/)
    - [Admin](https://docs.djangoproject.com/en/4.0/ref/contrib/admin/)
    - [Internationalization](https://docs.djangoproject.com/en/4.0/topics/i18n/)
    - [Security](https://docs.djangoproject.com/en/4.0/topics/security/)
        - Clickjacking
        - Cross-site scripting
        - Cross Site Request Forgery (CSRF)
        - SQL injection
        - Remote code execution


### 보안
    
-  장고는 보안을 중요하게 생각하며 SQL Injection, 사이트간 스크립팅(cross-site scripting), 사이트간 요청 위조(cross-site request forgery) 및 클릭재킹(clickjacking)과 같은 많은 보안 이슈를 회피할 수 있도록 도와준다. 사용자 인증 시스템은 사용자 계정과 비밀번호를 관리할 수 있는 방법을 제공한다.

### 확장성
- [Django’s cache framework](https://docs.djangoproject.com/en/4.0/topics/cache/)

    사용자 트래픽에 맞춰 유연하게 확장할 수 있는 기능을 사용할 수 있다.

-----
## 궁금한 것 정리

<br>

### `projects` vs `app`

<br>

    An app is a web application that does something – e.g., a blog system, a database of public records or a small poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.

---
### `include()`

<br>

    The `include()` function allows referencing other URLconfs. Whenever Django encounters include(), it chops off whatever part of the URL matched up to that point and sends the remaining string to the included URLconf for further processing.

    The idea behind include() is to make it easy to plug-and-play URLs. Since polls are in their own URLconf (polls/urls.py), they can be placed under “/polls/”, or under “/fun_polls/”, or under “/content/polls/”, or any other path root, and the app will still work.

    다른 URL 패턴을 포함하는 경우 `admin.site.urls`를 제외하고 반드시 사용해야한다

---
### `path`

<br>

- path는 4개 arguments를 가지고 route, view는 필수이고 kwargs, name은 선택이다. 

- route
    
    route는 url pattern을 포함하는 string이며 request를 처리할 때 장고가 `urlpatterns`에 있는 패턴들 중 요청된 requestsed URL과 일치하는 패턴을 찾게된다.

    ```python
    https://www.example.com/myapp/ 이라는 request가 들어온 경우 URLconf가 myapp/을 찾으며 https://www.example.com/myapp/?page=3 일 경우 URLconf는 myapp/ 을 찾는다.
    ```

-   view

    장고가 매칭 패턴을 찾을 때 첫 번째 인수로 `HttpRequest`  객체를 사용하고 키워드 인수로 경로에서 `captured` 값을 사용하여 지정된 view 함수를 호출합니다 .

- kwargs

    임의의 키워드 인수를 target view에 dictionary를 전달할 수 있다.

- name

    URL 이름을 지정하면 Django의 다른 곳, 특히 템플릿 내에서 명확하게 참조할 수 있다. 


---
### [`Database setup`](https://docs.djangoproject.com/en/4.0/intro/tutorial02/)

<br>

- Default는 `SQLite` 이며 파이썬에 내장되어있어 새로 설치할 필요가 없다. 확장을 위해 `PostgreSQL`, `MySQL`로의 전환을 고려해볼 수 있다.

- 다른 데이터 베이스를 사용할 경우 다음과 같이 적절하게 `database bindings`을 설정해야한다.

- If you’re using `PostgreSQL`, you’ll need the `psycopg2` package. Refer to the PostgreSQL notes for further details.

- If you’re using `MySQL` or `MariaDB`, you’ll need a DB API driver like `mysqlclient`. See notes for the MySQL backend for details.

- If you’re using `SQLite` you might want to read the `SQLite backend notes`.

- If you’re using `Oracle`, you’ll need a copy of `cx_Oracle`, but please read the notes for the Oracle backend for details regarding supported versions of both Oracle and cx_Oracle.

- If you’re using an `unofficial 3rd party backend`, please consult the documentation provided for any additional requirements.

    - `ENGINE` 
        
        -   django.db.backends.sqlite3
        -   django.db.backends.postgresql
        -   django.db.backends.mysql
        -   django.db.backends.oracle

    - `NAME`
        - Full absolute path
        - default value : BASE_DIR / 'db.sqlite3`

    <br>
    
    - 다른 DB를 사용할 경우 `USER`, `PASSWORD`, `HOST`가 추가되야한다. 

        ```python
        
        # db.sqlite3
        DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'mydatabase',
            }
        }   


        # other dbs
        DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'mydatabase',
            'USER': 'mydatabaseuser',
            'PASSWORD': 'mypassword',
            'HOST': '127.0.0.1',
            'PORT': '5432',
            }
        }
   
        ```
---
### `INSTALLED_APP`

- 이것은 이 Django 인스턴스에서 활성화된 모든 Django 애플리케이션의 이름을 보유한다. 앱은 여러 프로젝트에서 사용할 수 있으며 프로젝트에서 다른 사람이 사용할 수 있도록 패키지 및 배포할 수 있다.


    | APP | 기능|
    |:---|:---|
    |django.contrib.admin | 관리 사이트|
    |django.contrib.auth |인증 시스템|
    |django.contrib.contenttypes|콘텐츠 유형에 대한 프레임워크|
    |django.contrib.sessions|세션 프레임워크|
    |django.contrib.messages| 메시징 프레임워크|
    |django.contrib.staticfiles|정적 파일 관리를 위한 프레임워크|
    
    이러한 응용 프로그램 중 일부는 최소한 하나의 데이터베이스 테이블을 사용하므로 사용하기 전에 데이터베이스에 테이블을 생성해야 한다

    ```python
    python manage.py migrate
    ```

    `migrate` 명령어 실행시 설정을 살펴보고 `INSTALLED_APPS`의 데이터베이스 설정과 `settings.py`, 앱과 함께 제공되는 데이터베이스 마이그레이션에 따라 필요한 테이블을 생성하며 적용되는 각 마이그레이션에 대한 메세지가 표시된다. 관심있는 경우 데이터베이스에 대한 명령줄 클라이언트를 실행하고 mysql의 경우 show tables, select table_name from user_tables; 등으로 데이터베이스를 사용해볼 수 있다.

---

###  Don’t repeat yourself (DRY)¶


- Every distinct concept and/or piece of data should live in one, and only one, place. **Redundancy is bad. Normalization is good**. The framework, within reason, should deduce as much as possible from as little as possible.

