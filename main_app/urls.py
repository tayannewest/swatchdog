from django.urls import path
from . import views

urlpatterns = [
  path("", views.Home.as_view(), name="home"),
  path("about/", views.about, name="about"),
  path("artsupplies/", views.artsupplies_index, name="artsupplies_index"),
  path("accounts/signup/", views.signup, name="signup"),
  path("artsupplies/<int:artsupply_id>/", views.artsupplies_detail, name="artsupplies_detail"),
]