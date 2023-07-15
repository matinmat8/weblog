from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.


STATUS_CHOICES = (('draft', 'Draft'), ('published', 'Published'))


class Post(models.Model):
    auther = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=150)
    body = models.TextField()
    create = models.DateTimeField(auto_now_add=True)  # sort by this date (admin panel)
    update = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(auto_now=False, auto_now_add=False, default=timezone.now())
    draft_note = models.CharField(max_length=250, blank=True)  # Note of why it is draft and when it is going to publish
    slug = models.CharField(max_length=150, unique_for_date='publish')  # for making unique urls
    status = models.CharField(max_length=60, choices=STATUS_CHOICES, default='draft')

    @property
    def views_count(self):
        return PostView.objects.filter(post=self).count()

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})


class PostView(models.Model):
    IPAddress = models.GenericIPAddressField(default="45.243.82.169")
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return '{0} in {1} post'.format(self.IPAddress, self.post.title)
