from typing import *
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.forms import PostForm
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
    
# Post CRUD
class PostCV(LoginRequiredMixin, CreateView):
    template_name = 'blog/post_form.html'
    # model = Post
    # # fields = '__all__'
    # fields = ['title', 'image', 'category', 'description', 'content', 'tags']
    form_class = PostForm
    success_url = reverse_lazy('blog:post-change')

    def form_valid(self, form):
        # print(f"{self.request.user=}")
        form.instance.owner = self.request.user
        return super().form_valid(form)

class PostUV(UpdateView):
    template_name = ""
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:post-change")

class PostDelV(DeleteView):
    template_name = "blog/post_form.html"
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:post-change")

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self):
        pass

class PostChangeLV(LoginRequiredMixin, ListView):
    template_name = 'blog/post_change_list.html'
    model = Post