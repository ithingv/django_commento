from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from blog.models import Post

class PostListView(ListView):
    template_name = 'blog/post_list.html'
    model = Post
