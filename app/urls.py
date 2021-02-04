from django.urls import path
from .views import *

urlpatterns = [
    path('',Login.as_view(),name="login"),
    path('home',Home.as_view(),name ="home"),
    path('signup',Singup.as_view(),name = "singup"),
    path('logout',Logout.as_view(),name="logout"),
    path('addnewartical',AddNewArticle.as_view(),name ="addnewartical"),
    path('searchblog',SearchBlog.as_view(),name = 'searchblog'),

]
