from django.urls import path
from django.contrib.auth.views import login
from . import views
app_name='users'
urlpatterns = [
    path('',views.index,name='index'),
    path('login/',login,{'template_name':'users/login.html'},name='login'),

]