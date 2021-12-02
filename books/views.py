from django.shortcuts import render
from .models import Book

# Create your views here.
def books(request):
  
    books = Book.objects.all()
    
    return render(request, 'books/books.html',{"books":books})

def book(request, pk):
   
    book = Book.objects.get(id=pk)
    
    return render(request, 'books/book.html', {'book': book})