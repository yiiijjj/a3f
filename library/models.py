from django.db import models
from django.urls import reverse

class Author(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    biography = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse("author_detail", args=[self.id])

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    summary = models.TextField(blank=True)
    isbn = models.CharField('ISBN', max_length=13, unique=True, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.CharField(max_length=100, blank=True, help_text='Enter a book genre (e.g. Science Fiction, Romance)')

    def get_absolute_url(self):
        return reverse("book_detail", args=[self.id])

    def __str__(self):
        return self.title
