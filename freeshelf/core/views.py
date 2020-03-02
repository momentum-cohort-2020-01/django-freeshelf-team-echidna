from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Book, Category
# from .forms import BookForm

def books_list(request):
    books = Book.objects.all()
    return render(request, 'core/books_list.html', {'books': books})

def books_detail(request, pk):
    book = Book.objects.get(pk=pk)
    is_favorite = False
    if book.favorite.filter(pk=request.user.pk).exists():
        is_favorite = True
    return render(request, 'core/books_detail.html', {'book': book, "pk":pk, 'is_favorite': is_favorite})

def book_by_category(request, slug):
    category = Category.objects.get(slug=slug)
    book_by_category = Book.objects.filter(category=category)
    return render(request, 'core/books_list.html', {'books':book_by_category, 'category': category})

def books_oldest_first(request, slug):
    category = Category.objects.get(slug=slug)
    books = Book.objects.filter(category=category).order_by('date_added')
    return render(request, 'core/books_list.html', {'books': books, 'category': category})

def books_newest_first(request, slug):
    category = Category.objects.get(slug=slug)
    books = Book.objects.filter(category=category).order_by('-date_added')
    return render(request, 'core/books_list.html', {'books': books, 'category': category})

def favorite_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if book.favorite.filter(pk=request.user.pk).exists():
        book.favorite.remove(request.user)
    else:
        book.favorite.add(request.user)
    return render(request, 'core/books_detail.html', {'book': book, "pk":pk})