from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Artsupply


# Create your views here.
class Home(LoginView):
  template_name = "home.html"

def about(request):
  return render(request, "about.html")

# class Artsupply:
#   def __init__(self, name, brand, media, familiarity, description, favorite):
#     self.name = name
#     self.brand = brand
#     self.media = media
#     self.familiarity = familiarity
#     self.description = description
#     self.favorite = favorite

# artsupplies = [
#   Artsupply("Pigma Micron", "Sakura", "Fineliner", 5, "So good", "true"),
# ]

def artsupplies_index(request):
  artsupplies = Artsupply.objects.all()
  return render(request, "artsupplies/index.html", {"artsupplies": artsupplies})

def signup(request):
  error_message = ""
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect("artsupplies_index")
    else:
      error_message = "Invalid sign up - please try again"
  form = UserCreationForm()
  context = {"form": form, "error_message": error_message}
  return render(request, "signup.html", context)

def artsupplies_detail(request, artsupply_id):
  artsupply = Artsupply.objects.get(id=artsupply_id)
  return render(request, "artsupplies/detail.html", {"artsupply": artsupply})