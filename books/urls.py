from django.urls import path
from .views import BookListCreate, BookSearchView

urlpatterns = [
    path('', BookListCreate.as_view(), name='book-list-create'),
    path('search/', BookSearchView.as_view(), name='book-search'),
]
