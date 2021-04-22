from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    # Blog
    path("", views.home, name="home"),
    path("<int:blog_id>/", views.details, name="details"),
    path("category/<int:category_id>/", views.category, name="category"),
    path("allblogs/", views.all_blogs, name="all_blogs"),
    path(
        "allblogs/all_blogs_ascending/",
        views.all_blogs_ascending,
        name="all_blogs_ascending",
    ),
]