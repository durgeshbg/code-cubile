from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, "posts/index.html")

def posts(request, start, end):
    posts_list = []
    for i in range(start, end+1):
        posts_list.append(f"post #{i}")

    return JsonResponse({"posts": posts_list})