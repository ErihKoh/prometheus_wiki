from django.shortcuts import render
from django.http import HttpResponse
import markdown

from . import util

    # title = request.path_info.split('/')[-1]


def index(request):

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
    })

    

def get_article(request, name_article):    
    res = util.get_entry(name_article)
    markup = markdown.markdown(res)
    title = request.path_info.split('/')[-1]
    return render(request, "encyclopedia/article.html", {
        "title": title,
        "markup": markup,
    })    


