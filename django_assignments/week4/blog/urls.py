from django.urls import path

from blog import views


app_name = "blog"
urlpatterns = [
    # path('post/list/', views.PostLV.as_view(), name='post-list'),
    path('post/<int:pk>/', views.PostDV.as_view(), name='post-detail'),
    path('comment/create/', views.CommentCV.as_view(), name='comment-create')
]