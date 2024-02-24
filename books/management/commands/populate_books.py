import json
from django.core.management.base import BaseCommand
from books.models import Book
from datetime import datetime

class Command(BaseCommand):
    help = 'Populates the Book model with initial data'

    def handle(self, *args, **kwargs):
        data = [
            {
                "title": "The Little Prince",
                "author": "Antoine de Saint-Exupéry",
                "description": "An aviator crashes in the desert and meets a little prince who has traveled from a distant asteroid.",
                "isbn": "978-2-07-057428-9",
                "publication_date": "1943-04-01"
            },
            {
                "title": "One Hundred Years of Solitude",
                "author": "Gabriel García Márquez",
                "description": "The story of the Buendía family over seven generations in Macondo, a fictional village in Colombia.",
                "isbn": "978-84-264-1828-6",
                "publication_date": "1967-05-30"
            },
            {
                "title": "1984",
                "author": "George Orwell",
                "description": "A man lives in a dystopian society where the government constantly monitors him.",
                "isbn": "978-84-663-1632-9",
                "publication_date": "1949-06-08"
            }
        ]

        for item in data:
            Book.objects.create(
                title=item['title'],
                author=item['author'],
                description=item['description'],
                isbn=item['isbn'],
                publication_date=datetime.strptime(item['publication_date'], '%Y-%m-%d').date()
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated the Book model with initial data'))
