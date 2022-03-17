from django.urls import path, include

from accounts import views


# app_name = 'accounts'
urlpatterns = [
    path('register/', views.UserCreateView.as_view(), name='register'),
    path('register/done/', views.UserCreateDoneTV.as_view(), name='register_done'),

    path('', include('django.contrib.auth.urls')),
]
