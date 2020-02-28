from django.db import models
from django.utils.text import slugify

class Book(models.Model):
   title = models.CharField(max_length=80)
   author = models.CharField(max_length=30)
   description = models.TextField(max_length=None)
   date_added = models.DateTimeField(auto_now_add=True)
   url = models.URLField(max_length=200)
   
   def __str__(self):
        return f"Title: {self.title} Author: {self.author}"
