from django.db import models
from django.utils import timezone
from django.contrib import auth

class Books(models.Model):
  title = models.CharField(max_length=300)
  isbn = models.CharField(max_length=32, blank=True)
  publisher = models.CharField(max_length=300, blank=True)
  author = models.CharField(max_length=200)
  opinion = models.TextField()
  pub_date = models.DateTimeField('date published')
  
  class Meta():
    verbose_name_plural = "Books"
    verbose_name = "Book"


  def save(self):
    if not self.pk:
      # this object is new, set pub_date
      self.pub_date = timezone.now()
    super(Books, self).save()
