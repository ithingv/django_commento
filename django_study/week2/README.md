# postgre 설치

설치환경
- ubuntu 20.04 
- 참고: https://ko.linux-console.net/?p=748


```
# Create the file repository configuration:
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

# Import the repository signing key:
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

# Update the package lists:
sudo apt-get update

# Install the latest version of PostgreSQL.
# If you want a specific version, use 'postgresql-12' or similar instead of 'postgresql':
sudo apt-get -y install postgresql
```

- postgres DB 설치 확인

```
$ sudo systemctl is-active postgresql
$ sudo systemctl is-enabled postgresql
$ sudo systemctl status postgresql
```

<div align="left">
    <img src="img\img1.PNG">
</div>

- postgresql 데이터베이스 생성

```
sudo su - postgres
psql

alter user postres with password '1234';
```
<div align="left">
    <img src="img\img2.PNG">
</div>


- 데이터베이스 및 사용자 생성


```
CREATE USER ithingv WITH PASSWORD '[email protected]';
CREATE DATABASE ithingv_db;
GRANT ALL PRIVILEGES ON DATABASE ithingv_db to ithingv;
\q

```
<div align="left">
    <img src="img\img3.PNG">
</div>

- pgAdmin4 설치
```
curl https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo apt-key add

sudo sh -c 'echo "deb https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'



sudo apt install pgadmin4

sudo /usr/pgadmin4/bin/setup-web.sh
```

- django와 postgresql 데이터베이스 연결

```
sudo apt-get install libpq-dev

pip install psycopg2
```

```python
# settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'test_db',
        'USER': 'ithingv',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': 5432
    }
}


```

db 변경사항 반영
```
python manage.py migrate
```

<div align="left">
    <img src="img\img4.PNG">
</div>


```python

# project/example

from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=30)

```