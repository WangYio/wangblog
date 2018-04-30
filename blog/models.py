from django.db import models
from django.contrib.auth.models import User


# 分类表
class Category(models.Model):
    name = models.CharField(max_length=100)


#标签表
class Tag(models.Model):
    name=models.CharField(max_length=100)


# 文章
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=100, blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)


