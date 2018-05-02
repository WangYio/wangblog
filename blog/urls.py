from django.conf.urls import url
from .import views #从当前目录下导入views模块

app_name = 'blog' # 告诉 Django 这个 urls.py 模块是属于 blog 应用的，这种技术叫做视图函数命名空间
urlpatterns = [#保存网址和处理函数的关系
    url(r'^$', views.index, name='index'),#name是作为处理函数的别名
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
]