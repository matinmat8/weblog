from django.shortcuts import render
from django.views.generic import View
from .models import Post

# Create your views here.


class Index(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'blog/index.html')