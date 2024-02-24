from rest_framework import generics
from rest_framework import filters
from .models import Book
from .serializers import BookSerializer

class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookSearchView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author']

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        return Book.objects.filter(title__icontains=query) | Book.objects.filter(author__icontains=query)
