from django.contrib.auth.models import User
from django.db import models  
from django.utils.text import slugify
from PIL import Image


class Book(models.Model):
   title = models.CharField(max_length=80)
   author = models.CharField(max_length=30)
   description = models.TextField(max_length=None)
   date_added = models.DateTimeField(auto_now_add=True)
   url = models.URLField(max_length=200)
   category = models.ForeignKey('Category', on_delete=models.DO_NOTHING, null=True, blank=True)
   img = models.ImageField(default='default.png')
   favorite = models.ManyToManyField(User, related_name='favorite', blank=True)
   
   def __str__(self):
      return f"Title: {self.title} Author: {self.author}"

class Category(models.Model):
   name = models.CharField(max_length=40)
   slug = models.SlugField(null=False, unique=True)

   def __str__(self):
      return f'{self.name}'

   def save(self, *args, **kwargs):
      if not self.slug:
         self.slug = slugify(self.name)
      return super().save(*args, **kwargs)


# class Favorite(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)