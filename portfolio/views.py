from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Web_Project, ML_Project
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

# Create your views here.
def home(request):
    web_projects = Web_Project.objects.all()
    ml_projects = ML_Project.objects.all()
    context = {"web_projects": web_projects, "ml_projects": ml_projects}

    return render(request, "portfolio/home.html", context)


# We can use multiple models like this. this is my sample code.

# class about(ListView):
#     model = Web_Project
#     template_name = "portfolio/temp.html"
#     # queryset = Web_Project.objects.all()

#     def get_queryset(self):
#         return Web_Project.objects.all()

#     def get_context_data(self, **kwargs):
#         context = super(ListView, self).get_context_data(**kwargs)
#         context["web_projects"] = Web_Project.objects.all()
#         context["ml_projects"] = ML_Project.objects.all()
#         # And so on for more models
#         return context


# class skills(ListView):
#     template_name = "portfolio/skills.html"
#     queryset = Web_Project.objects.all()


# class aboutMe(ListView):
#     template_name = "portfolio/aboutMe.html"
#     queryset = Web_Project.objects.all()