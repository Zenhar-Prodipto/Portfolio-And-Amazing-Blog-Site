from django.db import models
from django.contrib.auth.models import User #User Model

# Create your models here.

#My Admin Model
class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(default='DEFAULT VALUE')
    created_on = models.DateTimeField()

    def __str__(self):
        return self.title

#Models for users

class UserBlog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField ()
    created_on = models.DateTimeField(null=True)
    images = models.ImageField(upload_to="portfolio/images/",blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
