from django.shortcuts import render
from django.views.generic import View, ListView
# from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, PostView


# Create your views here.


class Index(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'blog/index.html')


class PostLIst(ListView):
    model = Post
    template_name = 'blog/list.html'

    def get_queryset(self):
        obj = super().get_queryset()
        return obj.filter().order_by('publish')


def PostsDetailsView(request, slug):
    post = Post.objects.get(slug=slug)
    user_ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if user_ip:
        ip = user_ip.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    PostView.objects.get_or_create(IPAddress=ip, post=post)
    return render(request, 'blog/detail.html', {'post': post})
