from django.urls import path
from .views import Index, PostLIst

app_name = 'blog'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('list/', PostLIst.as_view(), name='list'),
]
