from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.home, name="home"),
    path("<int:itemid>", view=views.getList, name="getList"),
    # path("<str:name>", view=views.getListByName, name="itembyname"),
    path("create/", view=views.create, name="create"),
    path("view/", view=views.view, name="view"),
]
