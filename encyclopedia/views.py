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
    content = util.get_entry(title)
    markup = markdown2.markdown(content)

    return render(request, "encyclopedia/article.html", {
        "title": title,
        "markup": markup,
        "search_form": forms.SearchForm()
    })


def create_new_page(request):
    list_article = util.list_entries()
    if request.method == "POST":
        form = forms.NewPageForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]

            content = f"# {title}\n\n {content}"
            if title not in list_article:
                util.save_entry(title, content)
                return HttpResponseRedirect(reverse("get_article", kwargs={'title': title}))

            messages.error(request, 'Page has already exist.')

    return render(request, "encyclopedia/create_page.html", {
        "form": forms.NewPageForm()
    })


def edit_page(request, title):
    content = util.get_entry(title)

    if request.method == "POST":
        form = forms.EditPageForm(request.POST)

        if form.is_valid():
            content = form.cleaned_data["content"]

            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("get_article", kwargs={'title': title}))

    return render(request, "encyclopedia/edit_page.html", {
        "form": forms.EditPageForm(initial={'content': content}),
        "title": title,
    })


def random_page(request):
    entries = util.list_entries()
    selected_page = choice(entries)
    return HttpResponseRedirect(reverse("get_article", kwargs={'title': selected_page}))
