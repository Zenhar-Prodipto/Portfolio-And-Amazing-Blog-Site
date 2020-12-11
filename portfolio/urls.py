from django.urls import path
from . import views

from .views import skills, aboutMe

app_name = "portfolio"

urlpatterns = [
    path("", views.home, name="home"),
    path("skills/", skills.as_view(), name="skills"),
    path("about/", aboutMe.as_view(), name="aboutMe"),
]