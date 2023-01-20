from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from random import choice
import markdown2
from django.urls import reverse

from . import util
from . import forms


def search_article(request, list_article):
    form = forms.SearchForm(request.POST)

    if form.is_valid():
        query_search = form.cleaned_data["search"]

        result = [item for item in list_article if query_search.lower() in item.lower()]
        if len(result) == 1:
            return HttpResponseRedirect(f'wiki/{result[0]}')

        return render(request, "encyclopedia/index.html", {
            "entries": result,
            "header": "Searching articles",
            "search_form": forms.SearchForm()
        })


def index(request):
    list_article = util.list_entries()
    if request.method == "POST":
        return search_article(request, list_article)

    return render(request, "encyclopedia/index.html", {
        "header": "All Pages",
        "entries": list_article,
        "search_form": forms.SearchForm()
    })


def get_article(request, title):
    res = util.get_entry(title)
    markup = markdown2.markdown(res)

    return render(request, "encyclopedia/article.html", {
        "title": title,
        "markup": markup,
        "search_form": forms.SearchForm()
    })


def create_new_page(request):
    list_article = util.list_entries()
    if request.method == "POST":
        form = forms.NewPage(request.POST)

        if form.is_valid():
            query_title = form.cleaned_data["title"]
            query_content = form.cleaned_data["content"]

            content = f"# {query_title}\n\n {query_content}"
            if query_title not in list_article:
                util.save_entry(query_title, content)
                return HttpResponseRedirect(reverse("get_article", kwargs={'title': query_title}))
                
            messages.error(request, 'Page has already exist.')

    return render(request, "encyclopedia/create_page.html", {
        "form": forms.NewPage()
    })


def random_page(request):
    entries = util.list_entries()
    selected_page = choice(entries)
    return HttpResponseRedirect(reverse("get_article", kwargs={'title': selected_page}))
