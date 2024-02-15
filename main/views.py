from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Item, ToDoList
from .forms import CreateNewList

# Create your views here.

def index(response):
  return render(response, "main/base.html",{})

def home(response):
  return render(response, "main/home.html", {})

def getList(response, itemid):
  ls = ToDoList.objects.get(id=itemid)

  if ls in response.user.todolist.all():
    if response.method == "POST":
      # print(response.POST)
      # if the save button is clicked
      if response.POST.get("save"):
        # loop through all the items in the list
        for item in ls.item_set.all():
          if response.POST.get("c"+ str(item.id))=="clicked":
            item.complete = True
          else:
            item.complete = False
          item.save()

      elif response.POST.get("newItem"):
        txt = response.POST.get("new")
        if len(txt) > 2:
          ls.item_set.create(text=txt, complete=False)
        else:
          print("invalid")
    
    return render(response, "main/list.html", {
      "list": ls
    })

  else:
    return render(response, "main/view.html", {})

def getListByName(response, name):
  ls = ToDoList.objects.get(name=name)
  return HttpResponse(f"<h1>{ls.name}</h1>")

def create(response):
  # print(response.user)
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
      response.user.todolist.add(t)

    return HttpResponseRedirect(f"/{t.id}")
  else:
    form = CreateNewList()
  return render(response, "main/create.html", {
    "form": form
  })
  
def view(response):
  return render(response, "main/view.html", {})
