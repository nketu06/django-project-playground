from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def fees_detail(request):
    print(request,'------>',type(request))
    return render(request,"fee_detail.html")
