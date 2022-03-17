from django.shortcuts import render
from django.urls import reverse, reverse_lazy
# Create your views here.
from django.views.generic import ListView, DetailView, CreateView

from blog.models import Category, Post, Tag, Comment

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

class CommentCV(CreateView):
    model = Comment
    fields= ['post', 'content']

    def get_success_url(self):
        url = reverse_lazy('blog:post-detail', args=(self.object.post.id,))
        return f'{url}#post'
    
