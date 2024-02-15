from django.shortcuts import render, redirect
from .forms import UserRegisterForm

# Create your views here.
# 89s2Uu<;(p
def register(response):
  if response.method == "POST":
    form = UserRegisterForm(response.POST)
    if form.is_valid():
      form.save()
    return redirect("/")
  else:
    form = UserRegisterForm()

  return render(response, "user_register/register.html", {
    "form": form
  })

