from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.

text = [
    "yqweyuwiqehqiwhukhqewqjgyaxg eja ywegwqjXGEQYXYKEKWWgqugewX",
    "DSJHGKGSFAJHUFKSHFKSAHDFJKASHAFJSDFBAHJKSKB,HJSDFKUJAMGFDA",
    "AFJYSDGYDJGUMSCJDUKGJKGYCUJMHSDGCJHAJGWMDSGJAMGSCAGJGACJGHM",
]

def index(request):
    return render(request, "sections/index.html")

def sections(request, id):
    return HttpResponse(text[id - 1])