from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from blog.models import Category, Post, Tag

class PostLV(ListView):
    template_name = 'blog/post_list.html'
    model = Post

class PostDV(DetailView):
    template_name = 'blog/post_detail.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cateList'] = Category.objects.all()
        context['tagList'] = Tag.objects.all()
        return context