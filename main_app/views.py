from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
  return HttpResponse("<h1>Cool stuff will go here later on GOD on god</h1>")

def about(request):
  return render(request, "about.html")

class Artsupply:
  def __init__(self, name, brand, media, familiarity, description, favorite):
    self.name = name
    self.brand = brand
    self.media = media
    self.familiarity = familiarity
    self.description = description
    self.favorite = favorite

artsupplies = [
  Artsupply("Pigma Micron", "Sakura", "Fineliner", 5, "So good", "true"),
]

def artsupplies_index(request):
  return render(request, "artsupplies/index.html", {"artsupplies": artsupplies})