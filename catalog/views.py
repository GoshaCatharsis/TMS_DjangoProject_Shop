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
    

