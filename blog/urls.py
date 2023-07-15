from django.urls import path
from .views import Index, PostLIst, PostsDetailsView

app_name = 'blog'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('list/', PostLIst.as_view(), name='list'),
    path('detail/<slug:slug>/', PostsDetailsView, name='detail'),
]
