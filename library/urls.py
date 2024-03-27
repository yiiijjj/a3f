from django.urls import path,reverse
from . import views

urlpatterns = [
    path("",views.index),
    path("book_list/",views.book_list,name="book_list"),
    path("author_list/",views.author_list,name="author_list"),
    path("book/<int:pk>",views.book_detail,name="book_detail"),
    path("author/<int:pk>",views.author_detail,name="author_detail")
]