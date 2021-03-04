from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    # Authentication
    # path("signup/", views.signupUser, name="signupUser"),  # Signup user er url
    # path("logout/", views.logoutUser, name="logoutUser"),  # logout user er url
    # path("login/", views.loginUser, name="loginUser"),  # login user er url
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
    # ...
    # path("userhome/", views.userhome, name="userhome"),
    # path("create/", views.createBlogs, name="createBlogs"),  # Create new blogs
    # path("userhome/<int:user_blog_id>/", views.userBlogDetails, name="userBlogDetails"),
    # path("userhome/userallblogs/", views.user_all_blogs, name="user_all_blogs"),
    # path(
    #     "userhome/userallblogs/userallblogsascending/",
    #     views.user_all_blogs_ascending,
    #     name="user_all_blogs_ascending",
    # ),
    # # ...
    # path("userhome/<int:user_blog_id>/delete", views.deleteblog, name="deleteblog"),
    # path("userhome/<int:user_blog_id>/edit", views.editblog, name="editblog"),
]