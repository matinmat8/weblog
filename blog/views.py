from django.shortcuts import render
from django.views.generic import View, ListView
from .models import Post, PostView

from .decorators import debugging_decorator
from django.utils.decorators import method_decorator


# Create your views here.


class Index(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'blog/index.html')

    @method_decorator(debugging_decorator)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class PostLIst(ListView):
    model = Post
    template_name = 'blog/list.html'

    def get_queryset(self):
        obj = super().get_queryset()
        return obj.filter().order_by('publish')

    @method_decorator(debugging_decorator)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


@debugging_decorator
def PostsDetailsView(request, slug):
    post = Post.objects.get(slug=slug)
    user_ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if user_ip:
        ip = user_ip.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    PostView.objects.get_or_create(IPAddress=ip, post=post)
    return render(request, 'blog/detail.html', {'post': post})
