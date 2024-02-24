from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from books.views import BookSearchView  

urlpatterns = [
    path('', RedirectView.as_view(url='books/')),
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
    path('books/search/', BookSearchView.as_view(), name='book-search'),
]
