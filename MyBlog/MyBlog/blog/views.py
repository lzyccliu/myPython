from django.shortcuts import render,render_to_response,HttpResponse
from .models import *

from .forms import CommentForm
from django.http import Http404

# Create your views here.

def index(request):
    context={}
    context['hello'] ='Mr.刘的博客'
    return render(request,'index.html',context)

def base(request):
    # context = {}
    # context['top'] = 'http://xiaoxia.org'
    # context['main'] = 'http://www.ibaiyang.org'
    # context['right'] = 'http://www.xiaoxins.com'
    blogs = Blog.objects.all().order_by('-pub')
    return render(request,'base.html',{'blogs':blogs})

def get_blogs(request):
    blogs = Blog.objects.all().order_by('-pub')     #获得所有的博客按时间排序
    return render_to_response('blog_list.html',{'blogs':blogs})     #传递context:blog参数到固定页面

def get_details(request,blog_id):
    #检查异常
    try:
        blog=Blog.objects.get(id=blog_id)       #获取固定的blog_id的对象；
    except Blog.DoesNotExist:
        raise Http404

    if request.method =='GET':
        form = CommentForm()
    else:                                       #请求方法为POST
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['blog']=blog
            Comment.objects.create(**cleaned_data)
    ctx={
        'blog':blog,
        'comments':blog.comment_set.all().order_by('pub'),
        'form':form
    }                                           #返回3个参数
    return render(request,'blog_details.html',ctx)