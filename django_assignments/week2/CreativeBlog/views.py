from django.views.generic import TemplateView, ListView

from blog.models import Post

class HomeView(ListView):
    template_name = 'home.html'
    # model = Post
    queryset = Post.objects.all()
    paginate_by = 3
