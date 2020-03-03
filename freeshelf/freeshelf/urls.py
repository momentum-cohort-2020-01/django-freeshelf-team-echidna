"""freeshelf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.books_list, name = 'books-list'),
    path('books/<int:pk>/', views.books_detail, name = 'books-detail'),
    path('admin/', admin.site.urls),
    path('books/<slug:slug>/', views.book_by_category, name='book-by-category'),
    path('books/<slug:slug>/oldfirst/', views.books_oldest_first, name = 'books-oldest-first'),
    path('books/<slug:slug>/newfirst/', views.books_newest_first, name = 'books-newest-first'),
    path('accounts/', include('registration.backends.default.urls'), name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
