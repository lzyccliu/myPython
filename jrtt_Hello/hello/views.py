from django.http import HttpResponse
from django.shortcuts import render
from .models import Owner
# Create your views here.

def index(request):
    template = ('hello/index.html')
    owners = Owner.objects.all()
    context= {'index': index}
    return render(request,request,template,context)

# def hello(request):
#     """显示所有主人"""
#     owners = Owner.objects.all()
#     context = {'owners': owners}
#     return render(request,'hello/owners.html',context)