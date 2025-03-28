from django.db import models
from category.models import Category

class Post(models.Model):
    title = models.CharField(max_length=64, null=False, blank=False)
    category = models.ForeignKey(Category)
    
