from django.urls import path, include
from . import views
from user_register import views as v

urlpatterns = [
    path("", view=views.home, name="home"),
    path("<int:itemid>", view=views.getList, name="getList"),
    # path("<str:name>", view=views.getListByName, name="itembyname"),
    path("create/", view=views.create, name="create"),
    
    path("register/", v.register, name="register"),
    path("", include("main.urls")),
    path("", include("django.contrib.auth.urls")),
]
