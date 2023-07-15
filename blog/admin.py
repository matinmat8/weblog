from django.contrib import admin
from .models import Post, PostView


# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('auther', 'pk', 'title', 'draft_note', 'create', 'slug')


@admin.register(PostView)
class PostViewAdmin(admin.ModelAdmin):
    list_display = ('IPAddress', 'post')
