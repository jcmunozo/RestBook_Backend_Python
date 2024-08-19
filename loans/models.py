from django.db import models

from books.models import Book
from users.models import User

class Loan(models.Model):
    book=models.ForeignKey(Book, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    loan_date=models.DateField("Date of the book loaned", max_length=30)
    return_date=models.DateField("Date of the book returned")
