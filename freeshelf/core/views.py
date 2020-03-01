from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Book, Category
# from .forms import BookForm

def books_list(request):
    books = Book.objects.all()
    return render(request, 'core/books_list.html', {'books': books})

def books_detail(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'core/books_detail.html', {'book': book, "pk":pk})

def book_by_category(request, slug):
    category = Category.objects.get(slug=slug)
    book_by_category = Category.objects.filter(category=category)
    return render(request, 'core/book_by_category.html', {'books':book_by_category, 'category': category})