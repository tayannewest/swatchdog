from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Artsupply, Photo
import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'swatchdog'

# Create your views here.
class Home(LoginView):
  template_name = "home.html"

def about(request):
  return render(request, "about.html")

def profile(request):
  artsupplies = Artsupply.objects.all().order_by("-pk")
  return render(request, "profile.html", {"artsupplies": artsupplies})

@login_required
def artsupplies_index(request):
  artsupplies = Artsupply.objects.all().order_by("-pk")
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

@login_required
def artsupplies_detail(request, artsupply_id):
  artsupply = Artsupply.objects.get(id=artsupply_id)
  return render(request, "artsupplies/detail.html", {"artsupply": artsupply})

class ArtsupplyCreate(LoginRequiredMixin, CreateView):
  model = Artsupply
  fields = ["name", "brand", "medium", "familiarity", "description", "favorite"]

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class ArtsupplyUpdate(LoginRequiredMixin, UpdateView):
  model =Artsupply
  fields = ["familiarity", "description", "favorite"]
    
class ArtsupplyDelete(LoginRequiredMixin, DeleteView):
  model = Artsupply
  success_url = "/artsupplies/"

@login_required
def add_photo(request, artsupply_id):
  photo_file = request.FILES.get("photo-file", None)
  print(photo_file)
  if photo_file:
    s3 = boto3.client("s3")
    key = uuid.uuid4().hex + photo_file.name[photo_file.name.rfind("."):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, artsupply_id=artsupply_id)
      photo.save()
    except Exception as err:
      print("An error occurred uploading file to S3: %s" % err)
  return redirect("artsupplies_detail", artsupply_id=artsupply_id)

