from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Web_Project, ML_Project

# Create your views here.
def home(request):
    web_projects = Web_Project.objects.all()
    ml_projects = ML_Project.objects.all()

    return render(
        request,
        "portfolio/home.html",
        {"web_projects": web_projects, "ml_projects": ml_projects},
    )
