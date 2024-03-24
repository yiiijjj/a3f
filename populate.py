import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','a3f.settings')

import django
django.setup()

## FAKE POP SCRIPT
import random
from library.models import Author,Book
from faker import Faker

gen = Faker()

r_author = gen.name()

def add_author():
    a = Author.objects.get_or_create(name=r_author)[0]
    a.save()
    return a

#populate book
def populate(N=3):

    for entry in range(N):

        b_author = add_author()
        b_title = gen.company()
        b_summary = gen.paragraphs()
        b_isbn = gen.isbn13()
        b_genre = gen.bs()

        newbook = Book.objects.get_or_create(title=b_title,author=b_author,summary=b_summary,isbn=b_isbn,genre=b_genre)[0]

if __name__ == '__main__':
    print('populating script')
    populate()
    print('populating complete')