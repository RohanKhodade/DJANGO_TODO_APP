from django.urls import path
from .views import *
urlpatterns=[
    path("",home,name="todo"),
    path("register/",register,name="register"),
    path("login/",login_user,name="login_user"),
    path("delete_task/<str:name>",delete_task,name="delete_task"),
    path("update_task/<str:name>",update_task,name="update_task"),
    path("logoutview/",logoutview,name="logoutview")
    
]