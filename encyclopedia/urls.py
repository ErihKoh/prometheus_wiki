from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.get_article, name='get_article'),
    path("create-new-page", views.create_new_page, name="create_new_page"),
    path("random-page/", views.random_page, name="random_page"),
    path("edit-page", views.edit_page, name="edit_page"),

]
