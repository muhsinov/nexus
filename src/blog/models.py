from django.db import models
from category.models import Category
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=256, null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False, related_name="posts")
    description = models.TextField(null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=False, related_name="posts")
    media = models.TextField(null=False, blank=False)
    is_sticky = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True, editable=False)
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False, related_name="comments")
    content = models.TextField(null=False, blank=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="replies")
    created_at = models.DateTimeField(auto_now=True, editable=False)
    
    def __str__(self):
        return f"{self.author.username} - {self.post.title}"
    