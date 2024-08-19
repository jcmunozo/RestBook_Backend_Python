from django.db import models

class Book(models.Model):
    title=models.CharField("Book title", max_length=40)
    author=models.CharField("Author of the book", max_length=50)
    category=models.CharField("Category of the book", max_length=30)
    publication_date=models.DateField("Date of the publication")
    registered_date=models.DateTimeField("Date of the registration", auto_now_add=True)
