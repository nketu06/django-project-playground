from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def course_name(request):
    return HttpResponse('<h1>first_course</h1>')
