from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Book, Category, User, Favorite
# from .forms import BookForm

def books_list(request):
    books = Book.objects.all()
    favorite_book = get_favorite_for_user(request)
    return render(request, 'core/books_list.html', {'books': books, 'favorite_book': favorite_book})

def books_detail(request, pk):
    book = Book.objects.get(pk=pk)
    favorite_book = get_favorite_for_user(request)
    return render(request, 'core/books_detail.html', {'book': book, "pk":pk, 'favorite_book': favorite_book})

def book_by_category(request, slug):
    category = Category.objects.get(slug=slug)
    book_by_category = Book.objects.filter(category=category)
    favorite_book = get_favorite_for_user(request)
    return render(request, 'core/books_list.html', {'books':book_by_category, 'category': category, 'favorite_book': favorite_book})

def books_oldest_first(request, slug):
    category = Category.objects.get(slug=slug)
    books = Book.objects.filter(category=category).order_by('date_added')
    return render(request, 'core/books_list.html', {'books': books, 'category': category})

def books_newest_first(request, slug):
    category = Category.objects.get(slug=slug)
    books = Book.objects.filter(category=category).order_by('-date_added')
    return render(request, 'core/books_list.html', {'books': books, 'category': category})

def get_favorite_for_user(request):
    user = User.objects.get(username=request.user.username)
    favorite_book = [favorite.book for favorite in user.favorites.all()]
    return favorite_book