from django.shortcuts import render
from django.http import HttpResponse
import markdown

from . import util

def index(request):
    list_article = util.list_entries()

    if request.method == "POST":
        query = request.POST.get('q')

        result = [item for item in list_article if query in item]

        return render(request, "encyclopedia/index.html", {
            "entries": result or list_article,
        })
    return render(request, "encyclopedia/index.html", {
            "entries": list_article,
        })   

    

def get_article(request, title):    
    res = util.get_entry(title)
    markup = markdown.markdown(res)

    return render(request, "encyclopedia/article.html", {
        "title": title,
        "markup": markup,
    })   



