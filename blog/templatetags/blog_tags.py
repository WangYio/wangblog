from ..models import Post, Category
from django import template

register = template.Library()


#这个函数的功能是获取数据库中前 num 篇文章，这里 num 默认为 5。注册这个函数为模板标签
@register.simple_tag #首先导入 template 这个模块，然后实例化了一个 template.Library 类，并将函数 get_recent_posts 装饰为 register.simple_tag。
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    # 别忘了在顶部引入 Category 类
    return Category.objects.all()