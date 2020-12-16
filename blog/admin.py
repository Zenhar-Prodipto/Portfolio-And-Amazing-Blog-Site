from django.contrib import admin
from .models import Blog, UserBlog, Category

# Register your models here.
admin.site.register(Blog)
admin.site.register(UserBlog)
admin.site.register(Category)