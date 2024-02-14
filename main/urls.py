from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.home, name="home"),
    
    path("<int:itemid>", view=views.getItem, name="getitem"),
    path("<str:name>", view=views.getItemByName, name="itembyname"),
    
    
]
