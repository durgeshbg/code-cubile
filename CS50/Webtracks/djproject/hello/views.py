from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, "hello/index.html")

def durgesh(request):
    return HttpResponse("Hello Durgesh")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize(),
    })