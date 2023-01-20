from django.shortcuts import render
from django.http import HttpResponseRedirect
from random import randint
import markdown2

from . import util   


def search_article(request, list_article):
    query = request.POST.get('q')

    result = [item for item in list_article if query.lower() in item.lower()]
    if len(result) == 1:
        return HttpResponseRedirect(f'wiki/{result[0]}')


    return render(request, "encyclopedia/index.html", {
            "entries": result or list_article,
        })


def index(request):
    list_article = util.list_entries()

    if request.method == "POST":

       return search_article(request, list_article)

    return render(request, "encyclopedia/index.html", {
            "entries": list_article,
        })      


def get_article(request, title):    
    res = util.get_entry(title)
    markup = markdown2.markdown(res)

    return render(request, "encyclopedia/article.html", {
        "title": title,
        "markup": markup,
    }) 

def create_new_page(request):
    return render(request, "encyclopedia/create_page.html")


def random_page(request):
    list_article = util.list_entries()

    random = randint(0, len(list_article))

    return get_article(request, list_article[random])