from django.db import models
from django.contrib.auth.models import User  # User Model

# Create your models here.

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextUploadingField(default="DEFAULT VALUE")
    created_on = models.DateTimeField()
    category = models.ManyToManyField("Category", related_name="+")
    images = models.ImageField(upload_to="portfolio/images/", blank=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)
    created_on = models.DateTimeField(null=True)

    def __str__(self):
        return self.name