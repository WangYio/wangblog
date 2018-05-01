from django.contrib import admin
from blog.models import Category, Tag, Post

admin.site.register([Post, Tag, Category])
