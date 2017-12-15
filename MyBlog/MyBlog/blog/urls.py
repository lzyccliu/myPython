from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),        #这里''表示本目录下views路径,views.index表示view内index方法
    path('blog/', views.get_blogs,name='blogs'),
    path('<int:blog_id>/', views.get_details, name = 'blog_get_detail'),
]