from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from blog.models import Post

# Create your models here.

class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'comments')
    created_date = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    def __str__(self):

        return f'{str(self.author)}, {self.post.title[:30]}'
