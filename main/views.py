from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Item, ToDoList
from .forms import CreateNewList

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

def create(response):
  if response.method == "POST":
    # get the form data
    form = CreateNewList(response.POST)
    # check if the form is valid
    if form.is_valid():
      # get the name field from the form
      n = form.cleaned_data["name"]
      # create a new list with the name
      t = ToDoList(name=n)
      t.save()

    return HttpResponseRedirect(f"/{t.id}")
  else:
    form = CreateNewList()
  return render(response, "main/create.html", {
    "form": form
  })
