from django.views import generic
from blog.models import Post

class PostView(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog/index.html"
    context_object_name = "post_list"   # garante compatibilidade com o template

class PostDetail(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
