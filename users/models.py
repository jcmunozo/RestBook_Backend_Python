from django.db import models

class User(models.Model):
    name=models.CharField("User name", max_length=40)
    email=models.CharField("User email", max_length=50)
    created=models.DateTimeField("Date of the registration", auto_now_add=True)
