from django.urls import path
from . import views

from .views import skillsAndAbout

app_name = "portfolio"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", skillsAndAbout.as_view(), name="skillsAndAbout"),
]