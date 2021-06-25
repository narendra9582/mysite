from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("hello, you are at polls index page")

def homepage(request):
    context = "hello from homepage"
    return render(request,"index.html", context)
