#  4주차 과제
인증기능
1. 로그인버튼 로그아웃 버튼
img1
img2
- https://getbootstrap.com/docs/5.1/components/dropdowns/
- 
```html
<li class="nav-item dropdown">
                    {% if user.is_authenticated %}
                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" data-bs-toggle="dropdown">
                            <i class="fas fa-user"></i> &nbsp; {{ user.username }}
                        </a>
                        <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                            <li><a class="dropdown-item" href="{% url 'logout' %}#logout">Logout</a></li>
                            <li><a class="dropdown-item" href="{% url 'password_change' %}#password_change">Password
                                change</a></li>
                        </ul>
                    {% else %}
                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" data-bs-toggle="dropdown">
                            <i class="fas fa-user"></i> &nbsp; anonymous
                        </a>
                        <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                            <li><a class="dropdown-item" href="{% url 'login' %}#login">Login</a></li>
                            <li><a class="dropdown-item" href="{% url 'register' %}#register">Register</a></li>
                        </ul>
                    {% endif %}
                </li>

```

2. 로그인 클릭시
   
   img3

   accounts/models.py
   - 장고에 이미 있는 user 테이블이 있어서 models.py를 따로 설정할 필요가 없다.
   - 장고의 `auth` 모듈이 메모리에 로딩되면서 동작한다.
     - img4
   - LoginView
     - template_name = 'registration/login.html'
     - 우리가 직접 만들어줘야한다. 
  ```html
  {% extends 'base_shrink.html' %}

{% block title %}login.html{% endblock %}

{% block extra-style %}
<style>
    .errorlist {
      width: 100%;
      margin-top: 0.25rem;
      font-size: 0.875em;
      color: #dc3545;
    }
</style>
{% endblock %}

{% block content %}
<section class="page-section" id="login">
    <div class="container px-4 px-lg-5">
        <div class="row gx-4 gx-lg-5 justify-content-center">
            <div class="col-lg-8 col-xl-6 text-center">
                <h2 class="mt-0">Login</h2>
                <hr class="divider" />
                <p class="text-muted mb-5">please enter your id and password.</p>
            </div>
        </div>

        <div class="row gx-4 gx-lg-5 justify-content-center mb-5">
            <div class="col-lg-6">
                {{ form.non_field_errors }}
                <form id="contactForm" action="" method="post"> {% csrf_token %}
                    <div class="form-floating mb-3">
                        <input class="form-control" name="username" type="text" />
                        <label for="name">username</label>
                        {{ form.username.errors }}
                    </div>
                    <div class="form-floating mb-3">
                        <input class="form-control" name="password" type="password" />
                        <label for="email">password</label>
                        {{ form.password.errors }}
                    </div>
                    <div class="d-grid">
                        <button class="btn btn-primary btn-xl" id="submitButton" type="submit">Submit</button>
                        <input type="hidden" name="next" value="{{ next }}">
                    </div>
                </form>
            </div>
        </div>

    </div>
</section>
{% endblock %}
     ```

     img5
     - 장고 form
     - html을 만들어준다.
     - form의 name이 key로하고 실제 입력이 value가 된다.
     - img6
3. 회원가입 성공시

```python
class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    model = User
    fields = "__all__"
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')
```

register.html
```html


```

4. User에는 password가 하나이지만 Registration의 re-password를 추가해야하므로
   formclass를 직접 만들어야한다.
   - 장고에 이미 존재함
     - UserCreationForm
     - img7

5. 비밀번호 변경 FORM

auth/views.py

PASSWORD CHANGE FORM


```html
{% extends 'base_shrink.html' %}

{% block title %}password_change_form.html{% endblock %}

{% block extra-style %}
<style>
    .errorlist {
      width: 100%;
      margin-top: 0.25rem;
      font-size: 0.875em;
      color: #dc3545;
    }
</style>
{% endblock %}

{% block content %}
<section class="page-section" id="password_change">
    <div class="container px-4 px-lg-5">
        <div class="row gx-4 gx-lg-5 justify-content-center">
            <div class="col-lg-8 col-xl-6 text-center">
                <h2 class="mt-0">Password Change</h2>
                <hr class="divider" />
                <p class="text-muted mb-5">please enter old password and then new password twice.</p>
            </div>
        </div>

        <div class="row gx-4 gx-lg-5 justify-content-center mb-5">
            <div class="col-lg-6">
                {{ form.non_field_errors }}
                <form id="contactForm" action="" method="post"> {% csrf_token %}
                    <div class="form-floating mb-3">
                        <input class="form-control" name="old_password" type="password" id="old_password" />
                        <label for="old_password">old password</label>
                        {{ form.old_password.errors }}
                    </div>
                    <div class="form-floating mb-3">
                        <input class="form-control" name="new_password1" type="password" />
                        <label for="email">new password</label>
                        {{ form.new_password1.errors }}
                    </div>
                    <div class="form-floating mb-3">
                        <input class="form-control" name="new_password2" type="password" id="new_password2" />
                        <label for="email">new password confirm</label>
                        {{ form.new_password2.errors }}
                    </div>
                    <div class="d-grid">
                        <button class="btn btn-primary btn-xl" id="submitButton" type="submit">Submit</button>
                    </div>
                </form>
            </div>
        </div>

    </div>
</section>
{% endblock %}
```
img8

- 비밀번호 변경시 회원정보가 안뜸 template 수정

6. 로그아웃 이동

```html
{% extends 'base_shrink.html' %}

{% block title %}logged_out.html{% endblock %}

{% block content %}
<section class="page-section" id="logout">
    <div class="container px-4 px-lg-5">
        <div class="row gx-4 gx-lg-5 justify-content-center">
            <div class="col-lg-8 col-xl-6 text-center">
                <h2 class="mt-0">Logged out</h2>
                <hr class="divider" />
                <p class="text-muted mb-5">
                    <i class="fas fa-quote-left"></i>
                    &emsp;
                    <span class="h6">Thanks for visiting this web site.</span>
                    &emsp;
                    <i class="fas fa-quote-right"></i>
                </p>
            </div>
        </div>
    </div>
</section>
{% endblock %}
```
7. CRUD

include/navbar.html

```html

    <div class="container px-4 px-lg-5">
        <a class="navbar-brand" href="{% url 'home' %}#page-top">Creative Blog</a>
        <button class="navbar-toggler navbar-toggler-right" type="button" data-bs-toggle="collapse"
                data-bs-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false"
                aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
        <div class="collapse navbar-collapse" id="navbarResponsive">
            <ul class="navbar-nav ms-auto my-2 my-lg-0">
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'home' %}#page-top" data-bs-target="#page-top">HOME</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'home' %}#portfolio" data-bs-target="#portfolio">BLOG</a>
                </li>

                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" data-bs-toggle="dropdown">
                        CHANGE
                    </a>
                    <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                        <li><a class="dropdown-item" href="{% url 'blog:post-create' %}#create">Create</a></li>
                        <li><a class="dropdown-item" href="{% url 'blog:post-change' %}#change">Change list</a></li>
                    </ul>
                </li>

                <li class="nav-item">
                    <a class="nav-link" href="{% url 'home' %}#services" data-bs-target="#services">IAM</a>
                </li>
                <li class="nav-item"><a class="nav-link" href="{% url 'admin:index' %}">ADMIN</a></li>

                <li class="nav-item dropdown">
                    {% if user.is_authenticated %}
                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" data-bs-toggle="dropdown">
                            <i class="fas fa-user"></i> &nbsp; {{ user.username }}
                        </a>
                        <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                            <li><a class="dropdown-item" href="{% url 'logout' %}#logout">Logout</a></li>
                            <li><a class="dropdown-item" href="{% url 'password_change' %}#password_change">Password
                                change</a></li>
                        </ul>
                    {% else %}
                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" data-bs-toggle="dropdown">
                            <i class="fas fa-user"></i> &nbsp; anonymous
                        </a>
                        <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                            <li><a class="dropdown-item" href="{% url 'login' %}#login">Login</a></li>
                            <li><a class="dropdown-item" href="{% url 'register' %}#register">Register</a></li>
                        </ul>
                    {% endif %}
                </li>

            </ul>
        </div>
    </div>
```
*** 비밀번호 변경시 로그인된 유저 정보가 navbar에 안뜨는 현상
base_shrink.html 수정

8. base.html ---> head.html / navbar.html / footer.html 로 쪼개기
include 추가



9.  POST CRUD

blog/url.py
```python
    # Post CRUD
    path('post/create/', views.PostCV.as_view(), name='post-create'),
    path('post/change/', views.PostChangeLV.as_view(), name='post-change'),
    path('post/<int:pk>/update/', views.PostUV.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDelV.as_view(), name='post-delete'),

]
```

```python
class PostCV(CreateView):
    template_name = "blog/post_form.html"
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("home")

class PostUV(UpdateView):
    template_name = ""
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("home")

class PostDelV(DeleteView):
    template_name = ""
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self):
        pass

```
img9

10. django widget tweak
    ```
    pip install django-widget-tweaks
    ```
    새로운 패키지를 가져올 때는 가상환경에 설치하고 settings.py에 등록해야한다.
    django-widget-tweak

11. POST CREATE
    img11

    - owner를 표시
    - img12
    - img13
- 
    -  폼에 연결된 모델의 레코드의 owner
    -  요청 파라미터에는 항상 user 필드가 들어있다.
    -  form.instance.owner = self.request.user
  

12. CREATE VIEW

- ccbv.co.uk

img14
img15

13. 디테일 페이지 오른쪽에 수정버튼
14. change-list
    
    post_change_list.html
    ```
    {% extends 'base_shrink.html' %}

{% block title %}post_change_list.html{% endblock %}

{% block content %}
<section class="page-section" id="change">
    <div class="container px-4 px-lg-5">
        <div class="row gx-4 gx-lg-5 justify-content-center">
            <div class="col-lg-8 col-xl-6 text-center">
                <h2 class="mt-0">Post Change List</h2>
                <hr class="divider" />
                <p class="text-muted mb-5">you can update or delete for Post table.</p>
            </div>
        </div>

        <div class="row gx-4 gx-lg-5 justify-content-center mb-5">
            <div class="col-lg-12">

<table class="table table-striped table-hover">
  <thead>
    <tr>
      <th scope="col">ID</th>
      <th scope="col">Title</th>
      <th scope="col">Description</th>
      <th scope="col">Owner</th>
      <th scope="col">Update</th>
      <th scope="col">Delete</th>
    </tr>
  </thead>
  <tbody>
  {% for post in object_list %}
    <tr>
      <th scope="row">{{ post.id }}</th>
      <td>{{ post.title }}</td>
      <td>{{ post.description }}</td>
      <td>{{ post.owner }}</td>
      <td><a href="{% url 'blog:post-update' post.id %}#create">UPDATE</a></td>
      <td><a href="{% url 'blog:post-delete' post.id %}#delete">DELETE</a></td>
    </tr>
  {% endfor %}
  </tbody>
</table>

            </div>
        </div>

    </div>
</section>
{% endblock %}
    ```

    