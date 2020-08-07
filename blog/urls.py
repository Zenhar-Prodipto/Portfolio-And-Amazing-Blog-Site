from django.urls import path
from . import views

app_name="blog"

urlpatterns = [

    # Authentication
    path("signup/",views.signupUser, name="signupUser"), #Signup user er url 
    path("logout/",views.logoutUser, name="logoutUser"), #logout user er url 
    path("login/",views.loginUser, name="loginUser"), #login user er url 


    #Blog
    path("",views.home,name="home"),
    path("<int:blog_id>/",views.details,name="details"), #prottek taah blog details e niye jaabe
    path("allblogs/",views.all_blogs, name="all_blogs"), # shob blog ekshathey dekhbe
    path("allblogs/all_blogs_ascending/",views.all_blogs_ascending, name="all_blogs_ascending"), #shob blog ekshathe dekhbe but ascending order e
    path("userhome/",views.userhome, name="userhome"), #signup sheshe user jeikhane eshe land korbe
    path("create/",views.createBlogs,name="createBlogs"), #Create new blogs
    path("userhome/<int:user_blog_id>/",views.userBlogDetails,name="userBlogDetails"), #User's blog details
    path("userhome/userallblogs/",views.user_all_blogs, name="user_all_blogs"), #User's all blogs
    path("userhome/userallblogs/userallblogsascending/",views.user_all_blogs_ascending, name="user_all_blogs_ascending"), #Users blog ascending
    
    
    
    











    path("random/",views.random,name="random"), #it works so follow the pattern
    path("random/again/",views.again,name="again"),
  
]