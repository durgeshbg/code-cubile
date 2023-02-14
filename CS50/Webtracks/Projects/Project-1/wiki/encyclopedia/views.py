from django.shortcuts import render
from markdown2 import markdown
from django.http import HttpResponseRedirect
from random import choice
import re
import os

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    content = util.get_entry(title)
    if content is None:
        return render(request, "encyclopedia/error.html", {
            "message": f"{title} doesn't exist!"
        })
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": markdown(content)
    })

def search(request):
    entries = util.list_entries()
    matches = []
    q = request.GET["q"]
    if q != "":
        if q in entries:
            return HttpResponseRedirect(f"wiki/{q}")
        for entry in entries:
            if re.search(q, entry, re.IGNORECASE):
                matches.append(entry)
    return render(request, "encyclopedia/search.html", {
        "entries": matches
    })

def add(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        if title in util.list_entries():
            return render(request, "encyclopedia/error.html",{
                "message": f"{title} already exists!"
            })
        util.save_entry(title, content)
        return HttpResponseRedirect(f"wiki/{title}")    
    else:
        return render(request, "encyclopedia/add.html")

def random_entry(request):
    title = choice(util.list_entries())
    return HttpResponseRedirect(f"wiki/{title}")

def edit(request, title):
    if request.method == "POST":
        content = request.POST["content"]
        util.save_entry(title, content)
        return entry(request, title)
    else:
        if title not in util.list_entries():
            return render(request, "encyclopedia/error.html", {
                "message": "Page not found"
            })
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": content
        })