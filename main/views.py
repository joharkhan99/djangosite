from django.shortcuts import render
from django.http import HttpResponse
from .models import Item, ToDoList

# Create your views here.

def home(response):
  return HttpResponse("<h1> This   is the main app homepage </h1>")

def getItem(response, itemid):
  ls = ToDoList.objects.get(id=itemid)
  item = ls.item_set.get(id=1)
  return HttpResponse(f"<h1>{ls.name}</h1><p>{item.text}</p>")

def getItemByName(response, name):
  ls = ToDoList.objects.get(name=name)
  
  return HttpResponse(f"<h1>{ls.name}</h1>")