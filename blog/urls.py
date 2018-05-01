from django.conf.urls import url
from . import views #从当前目录下导入views模块

urlpatterns = [#保存网址和处理函数的关系
    url(r'^$', views.index, name='index')#name是作为处理函数的别名
]