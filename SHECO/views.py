from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "SHECO/index.html")

def brain(request):
    return HttpResponse("hello, brain")

def greet(request,name):
    return render(request, "SHECO/greet.html",{"name":name.capitalize()})

