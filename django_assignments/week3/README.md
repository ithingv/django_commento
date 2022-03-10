#  2주차 과제

### 수업 내용

- `home.html`, `post_detail.html` 완성

- 템플릿 상속기능

- `listView`, `DetailView` 활용

-----

1. `home.html` 
    
    - about 삭제
    - url admin:index


2. 템플릿 상속

templates/blog
    post_detail.html
    post_detail-1.html
    post-detail-2.html
base.html
home-1.html
home-2.html

home.html 내용 지우고 home-1.html 전체를 붙여넣기

3.
error
href="{% url 'blog:post-detail' 1 %}"
namespace 등록

-> views
PostDV 


4. PostDV is missing a QuerySet. Define PostDV.model, PostDV.queryset, or override PostDV.get_queryset().

어떤 generic view를 상속받아야할지 잘 결정
테이블에서 특정 레코드 하나를 가져온다

5. startbootstrap blog -> post_detail 붙여넣기

6. post_detail.html 수정
post_detail-1 -> post_detail.html 

7. 템플릿 상속

home.html -> base.html 

base.html

```html
<!DOCTYPE html>

{% load static %}

<html lang="en">
<head>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"/>
    <meta name="description" content=""/>
    <meta name="author" content=""/>
    <title>{% block title %}{% endblock%}</title>
    <!-- Favicon-->
    <link rel="icon" type="image/x-icon" href="{% static 'assets/favicon.ico' %}"/>
    <!-- Bootstrap Icons-->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css" rel="stylesheet"/>
    <!-- Google fonts-->
    <link href="https://fonts.googleapis.com/css?family=Merriweather+Sans:400,700" rel="stylesheet"/>
    <link href="https://fonts.googleapis.com/css?family=Merriweather:400,300,300italic,400italic,700,700italic"
          rel="stylesheet" type="text/css"/>
    <!-- Core theme CSS (includes Bootstrap)-->
    <link href="{% static 'css/styles.css' %}" rel="stylesheet"/>
    {% block extra-style %}
    {% endblock%}
</head>

<body id="page-top">
<!-- Navigation-->
<nav class="navbar navbar-expand-lg navbar-light fixed-top py-3" id="mainNav">
    <div class="container px-4 px-lg-5">
        <a class="navbar-brand" href="#page-top">Creative Blog</a>
        <button class="navbar-toggler navbar-toggler-right" type="button" data-bs-toggle="collapse"
                data-bs-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false"
                aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
        <div class="collapse navbar-collapse" id="navbarResponsive">
            <ul class="navbar-nav ms-auto my-2 my-lg-0">
                <li class="nav-item"><a class="nav-link" href="#page-top">Home</a></li>
                <li class="nav-item"><a class="nav-link" href="#portfolio">Blog</a></li>
                <li class="nav-item"><a class="nav-link" href="#services">Iam</a></li>
                <li class="nav-item"><a class="nav-link" href="{% url 'admin:index' %}">Admin</a></li>
            </ul>
        </div>
    </div>
</nav>
<!-- Masthead-->
<header class="masthead">
    <div class="container px-4 px-lg-5 h-100">
        <div class="row gx-4 gx-lg-5 h-100 align-items-center justify-content-center text-center">
            <div class="col-lg-8 align-self-end">
                <h1 class="text-white font-weight-bold">Welcome My Blog !</h1>
                <hr class="divider"/>
            </div>
            <div class="col-lg-8 align-self-baseline">
                <p class="text-white-75 mb-5">IT 관련 개발사항과 소소한 일상생활을 기록하는 공간입니다.</p>
            </div>
        </div>
    </div>
</header>

{% block content%}
{%endblock%}

<!-- Footer-->
<footer class="bg-light py-5">
    <div class="container px-4 px-lg-5">
        <div class="small text-center text-muted">Copyright &copy; 2021 - Company Name</div>
    </div>
</footer>
<!-- Bootstrap core JS-->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
<!-- Core theme JS-->
<script src="{% static 'js/scripts.js' %}"></script>
{% block extra-script%}
{% endblock %}

</body>
</html>

```

8. post_detail-2.html -> post_detail.html

9. masterhead를 안보이게 하기위해 base_shrink.html 생성 navbar-shrink 추가 script 삭제, masterhead 삭제 -> post_detail이 base_shrink.html을 상속받게함

10. PostDV에서 Post 테이블의 레코드를 가져와 2022-02-15    shkim    IT    it, django  이
변경되도록 CreativeBLog/views.py HomeView가 listView를 상속받도록 하고 home.html의 post에 for문 설정

11 <img class="img-fluid" src="{{ post.image.url }}" alt="..."/>
models.ImageField

12. 사진을 업로드하기 위해 세팅

1. settings.py

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

2. urls.py

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


3. SomeModel.objects.filter(id=id).delete()

클래스형 뷰

https://ccbv.co.uk/projects/Django/4.0/django.views.generic.list/ListView/

13. detailview 바꾸고 template 변경을 위해 최종 post_detail.html을 복사해서 post_detail.html에 붙여넣는다.

14. 결과

<img src="./static/assets/img/week1/img_39.png">
