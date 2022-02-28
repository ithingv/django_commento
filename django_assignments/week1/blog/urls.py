from django.urls import path

from blog import views

urlpatterns = [
    path('post/list/', views.PostListView.as_view(), name='post-list'),
]