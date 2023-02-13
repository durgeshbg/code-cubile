from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django import forms

class TodoFrom(forms.Form):
    task = forms.CharField(label="New task")

# Create your views here.

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "todo/index.html", {
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == "POST":
        form = TodoFrom(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("todo:index"))
        else:
            return render(request, "todo/add.html", {
                "form" : form
            })
    else:
        return render(request, "todo/add.html", {
            "form" : TodoFrom()
        })