from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Book
from .models import Author


class IndexView(TemplateView):
    template_name = 'catalog/index.html'

    def get(self, request):
        books = Book.objects.all()
        booksCount = books.count()
        authors = Author.objects.all().count()
        return render(request, self.template_name, {'books': books, 'booksCount': booksCount, 'authors': authors})


class BookView(TemplateView):
    template_name = 'catalog/book.html'

    def get(self, request, id):
        book = Book.objects.get(id=id)
        params = {
            'book': book
        }
        return render(request, self.template_name, params)



