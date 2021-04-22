from django.urls import path
from . import views

# from .views import skills, aboutMe
from .views import home

app_name = "portfolio"

urlpatterns = [
    path("", views.home, name="home"),
]