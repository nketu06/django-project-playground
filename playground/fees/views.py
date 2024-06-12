from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def fees_detail(request):
    print(request,'------>',type(request))
    context={'name':'ketu','price':"zero","today":datetime.now()}
    return render(request,"fees/fee_detail.html",context)
