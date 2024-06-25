from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'result/home.html')

def info(request):
    return render(request,'result/info.html')

# def about(request):
#     return HttpResponse("<h1>info</h1>")
