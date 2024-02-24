from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    isbn = models.CharField(max_length=20)
    publication_date = models.DateField()

    def __str__(self):
        return self.title
class Meta:
        app_label = 'books'