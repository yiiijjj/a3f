from django.urls import path
from . import views

urlpatterns = [
    path("",views.index),
    path("book_list/",views.book_list,name="book_list"),
    path("<int:id>",views.book_detail,name="book_detail"),
    path("author_list/",views.author_list,name="author_list"),
    path("<int:id>",views.author_detail,name="author_detail")
]