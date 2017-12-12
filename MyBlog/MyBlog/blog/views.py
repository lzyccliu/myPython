#coding=utf-8
from django.shortcuts import render
from .models import BlogsPost
from django.shortcuts import render_to_response

# Create your views here.
def index(request):
    blog_list = BlogsPost.objects.all()         #获取数据库里面所拥有BlogPost对象
    context ={'BlogsPost':BlogsPost}
    return render(request,'index.html',context)         #返回一个页面(index.html)，顺带把数据库中查询出来的所有博客内容（blog_list）也一并返回。