from django.views.generic import TemplateView, ListView

from blog.models import Post

class HomeView(ListView):
    template_name = 'home.html'
    # model = Post
    queryset = Post.objects.all()
    paginate_by = 3

    def get_queryset(self):
        # self.request.GET['category']
        self.category = self.request.GET.get("category")
        self.tag = self.request.GET.get("tag")

        if self.category:
            qs = Post.objects.filter(category__name=self.category)
        elif self.tag:
            qs = Post.objects.filter(tags__name=self.tag)
        else:
            qs = Post.objects.all()
        return qs   
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['category'] = self.category
        context['tag'] = self.tag
        return context
