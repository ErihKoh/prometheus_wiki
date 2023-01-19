from django.shortcuts import render
from django.http import HttpResponse
import markdown

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

    

def get_article(request, name_article):
    res = util.get_entry(name_article)
    html = markdown.markdown(res)
    return HttpResponse(html)    


