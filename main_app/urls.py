from django.urls import path
from . import views

urlpatterns = [
  path("", views.home, name="home"),
  path("about/", views.about, name="about"),
  path("artsupplies/", views.artsupplies_index, name="artsupplies_index"),
]