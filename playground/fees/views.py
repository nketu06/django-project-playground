from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def fees_detail(request):
    return HttpResponse("<h1>your fee is free</h1>")
