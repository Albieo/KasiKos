from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    restuarant = models.CharField(max_length=150)
    address = models.TextField()
    description = models.TextField()
    rating = models.PositiveIntegerField(default=0)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)


    class Meta:
        ordering = ['-created_at'] 
