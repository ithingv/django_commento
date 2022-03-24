from django.urls import path

from blog import views


app_name = "blog"
urlpatterns = [
    # path('post/list/', views.PostLV.as_view(), name='post-list'),
    path('post/<int:pk>/', views.PostDV.as_view(), name='post-detail'),
    path('comment/create/', views.CommentCV.as_view(), name='comment-create'),

    # Post CRUD
    path('post/create/', views.PostCV.as_view(), name='post-create'),
    path('post/change/', views.PostChangeLV.as_view(), name='post-change'),
    path('post/<int:pk>/update/', views.PostUV.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDelV.as_view(), name='post-delete'),

]