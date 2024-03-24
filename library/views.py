from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Author,Book

# Create your views here.

def index(request):
    return render(request,'library/index.html')

def book_list(request):
    books = Book.objects.all()
    return render(request,'library/book_list.html',{'books':books})

def book_detail(request, id):
    book = get_object_or_404(Book, pk=id)
    book_detail = {
        'title': book.title,
        'author': book.author,
        'summary': book.summary,
        'isbn': book.isbn,
        'genre': book.genre
    }
    return render(request,'library/book_detail.html',context=book_detail)

def author_list(request):
    authors = Author.objects.all()
    return render(request,'library/author_list.html',{'authors':authors})

def author_detail(request, id):
    author = get_object_or_404(Author, pk=id)
    author_detail = {
        'name': author.name,
        'dob': author.date_of_birth,
        'biography': author.biography
    }
    return render(request,'library/author_detail.html',context=author_detail)