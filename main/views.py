from django.shortcuts import render
from django.http import HttpResponse
from .models import Item, ToDoList

# Create your views here.

def index(response):
  return render(response, "main/base.html",{})

def home(response):
  return render(response, "main/home.html", {})

def getItem(response, itemid):
  ls = ToDoList.objects.get(id=itemid)
  return render(response, "main/list.html", {
    "list": ls
  })

def getItemByName(response, name):
  ls = ToDoList.objects.get(name=name)
  
  return HttpResponse(f"<h1>{ls.name}</h1>")