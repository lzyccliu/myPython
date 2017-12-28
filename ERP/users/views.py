from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    template = ('users/index.html')
    context= {'index': index}
    return render(request,request,template,context)