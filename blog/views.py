from django.shortcuts import render
from django.views.generic import View, ListView
# from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post


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
