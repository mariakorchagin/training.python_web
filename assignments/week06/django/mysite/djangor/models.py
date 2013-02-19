from django.db import models
from django.utils import timezone
from django.contrib import auth

# Create your models here.

# class Poll(models.Model):
#   question = models.CharField(max_length=200)
#   def __unicode__(self):
#     return self.question
#   def published_today(self):
#     now = timezone.now()
#     time_delta = now - self.pub_date
#     return time_delta.days == 0
# 
# class Choice(models.Model):
#   poll = models.ForeignKey(Poll)
#   choice = models.CharField(max_length=200)
#   votes = models.IntegerField(default=0)
#   def __unicode__(self):
#     return self.choice

class Books(models.Model):
  title = models.CharField(max_length=300)
  isbn = models.CharField(max_length=32)
  publisher = models.CharField(max_length=300)
  author = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')
#   owner = models.CharField(max_length=300)

