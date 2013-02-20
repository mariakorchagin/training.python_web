from django.db import models
from django.utils import timezone
from django.contrib import auth

class Books(models.Model):
  title = models.CharField(max_length=300)
  isbn = models.CharField(max_length=32)
  publisher = models.CharField(max_length=300)
  author = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')
#  opinion = models.CharField(max_length=30000)
#   owner = models.CharField(max_length=300)

