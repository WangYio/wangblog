from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from blog.models import Post, Category
from comments.forms import CommentForm
from django.views.generic import ListView,DetailView
import markdown


# def index(request):
#     post_list = Post.objects.all().order_by('-created_time')
#     return render(request, 'blog/index.html', context={
#       'post_list': post_list
#     })

#基于类的视图函数
class IndexView(ListView): #ListView 就是从数据库中获取某个模型列表数据的
    model = Post #model 指定为 Post，告诉 Django 我要获取的模型是 Post。
    template_name = 'blog/index.html' #指定这个视图渲染的模板
    context_object_name = 'post_list' #获取的模型列表数据保存的变量名。这个变量会被传递给模板




# def detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     post.increase_views()
#     post.body = markdown.markdown(post.body,
#                                   extensions=[
#                                       'markdown.extensions.extra',
#                                       'markdown.extensions.codehilite',
#                                       'markdown.extensions.toc',
#                                   ]
#     )
#     form= CommentForm()
#     comment_list = post.comment_set.all()
#     context = {
#         'post': post,
#         'form': form,
#         'comment_list': comment_list
#     }
#     return render(request,'blog/detail.html', context=context)


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        response = super(PostDetailView, self).get(request, *args, **kwargs)
        self.object.increase_views()
        return response

    def get_object(self, queryset=None):
        post = super(PostDetailView, self).get_object(queryset=None)
        post.body = markdown.markdown(post.body,
                                      extensions=[
                                          'markdown.extensions.extra',
                                          'markdown.extensions.codehilite',
                                          'markdown.extensions.toc',
                                      ])
        return post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        form = CommentForm()
        comment_list = self.object.comment_set.all()
        context.update({
            'form': form,
            'comment_list': comment_list
        })
        return context





#归档
# def archives(request, year, month):
#     post_list = Post.objects.filter(created_time__year=year,
#                                     created_time__month=month
#                                     ).order_by('-created_time')
#     return render(request, 'blog/index.html', context={
#         'post_list': post_list
#     })


class ArchivesView(IndexView):
    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        return super(ArchivesView, self).get_queryset().filter(created_time__year=year,
                                    created_time__month=month)





#分类
# def category(request, pk):
#     cate = get_object_or_404(Category, pk=pk)#根据传入的 pk 值（也就是被访问的分类的 id 值）从数据库中获取到这个分类
#     post_list = Post.objects.filter(category=cate).order_by('-created_time')
#     return render(request, 'blog/index.html',context={'post_list': post_list})
class CategoryView(IndexView): #直接继承IndexView
    def get_queryset(self):  #该方法默认获取指定模型的全部列表数据
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category=cate)
