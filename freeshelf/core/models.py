from django.db import models
from django.utils.text import slugify


class Book(models.Model):
   title = models.CharField(max_length=80)
   author = models.CharField(max_length=30)
   description = models.TextField(max_length=None)
   date_added = models.DateTimeField(auto_now_add=True)
   url = models.URLField(max_length=200)
   tag = models.ForeignKey('Tag', on_delete=models.DO_NOTHING, null=True, blank=True)
   
   def __str__(self):
      return f"Title: {self.title} Author: {self.author}"

class Tag(models.Models):
   name = models.Charfield(max_length=40)
   slug = models.SlugField(null=False, unique=True)

   def __str__(self):
      return f'{self.name}'

   def save(self, *args, **kwargs):
      if not self.slug:
         self.slug: = slugify(self.name)
      return super().save(*args, **kwargs)


