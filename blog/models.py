from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# import uuid

# Create your models here.

class Post(models.Model):

    # uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length = 256)
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'blogs',)
    body = models.TextField()
    published_date = models.DateTimeField(default = timezone.now)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):

        return self.title
    
class Like(models.Model):
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)