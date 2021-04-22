from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from .forms import LoginForm, RegistrationForm
from .models import Blog, Category


# Create your views here.
def home(request):
    # blogs = Blog.objects.all()
    blogs = Blog.objects.order_by("-created_on")
    category = Category.objects.all()
    return render(request, "blog/home.html", {"blogs": blogs, "category": category})


# Details view.
def details(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, "blog/details.html", {"blog": blog})


def category(request, category_id):
    blogs = Blog.objects.filter(category=category_id)
    category = get_object_or_404(Category, pk=category_id)
    all_category = Category.objects.all()
    return render(
        request,
        "blog/category.html",
        {"category": category, "blogs": blogs, "all_category": all_category},
    )


# descending order
def all_blogs(request):
    # blogs = Blog.objects.all()
    blogs = Blog.objects.order_by("-created_on")
    return render(request, "blog/all_blogs.html", {"blogs": blogs})


# ascending order
def all_blogs_ascending(request):
    # blogs = Blog.objects.all()
    blogs = Blog.objects.order_by("created_on")
    return render(request, "blog/all_blogs_ascending.html", {"blogs": blogs})
